Summary:	Simplistic XML parser for OCaml
Summary(pl):	Prosty parser XML dla OCamla
Name:		ocaml-tony
Version:	0.8
Release:	1
License:	BSD
Group:		Libraries
Vendor:		Christian Lindig <lindig@ips.cs.tu-bs.de>
URL:		http://www.cs.tu-bs.de/softech/people/lindig/software/tony.html
Source0:	http://www.cs.tu-bs.de/softech/people/lindig/software/download/tony-%{version}.tar.gz
BuildRequires:	ocaml >= 3.04-7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tony is a simple XML parser and pretty printer. The parser is non
validating and does neither comply fully to the standard nor does it
use the DOM for internal representation of a parsed XML file.

%description -l pl
Tony jest prostym parserem XML. Mo¿e te¿ drukowaæ XML z wciêciami.
Parser nie sprawdza wej¶cia wzglêdem DTD, nie jest te¿ w pe³ni
kompatybilny ze standardem, nie u¿ywa nawet DOM jak wewnêtrznej
reprezentacji.

%package devel
Summary:	Simplistic XML parser for OCaml
Summary(pl):	Prosty parser XML dla OCamla
Group:		Development/Libraries
%requires_eq	ocaml

%description devel
Tony is a simple XML parser and pretty printer. The parser is non
validating and does neither comply fully to the standard nor does it
use the DOM for internal representation of a parsed XML file.

%description devel -l pl
Tony jest prostym parserem XML. Mo¿e te¿ drukowaæ XML z wciêciami.
Parser nie sprawdza wej¶cia wzglêdem DTD, nie jest te¿ w pe³ni
kompatybilny ze standardem, nie u¿ywa nawet DOM jak wewnêtrznej
reprezentacji.

%prep
%setup -q -n tony-%{version}

%build
%{__make} clean
%{__make}
%{__make} all.opt
ocamlc -a -o tony.cma \
	error.cmo mylib/{lc,pp,std}.cmo xml.cmo xmlstate.cmo \
	xmlparse.cmo xmlscan.cmo
ocamlopt -a -o tony.cmxa \
	error.cmx mylib/{lc,pp,std}.cmx xml.cmx xmlstate.cmx \
	xmlparse.cmx xmlscan.cmx

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/tony
install *.cm[ixa]* *.a $RPM_BUILD_ROOT%{_libdir}/ocaml/tony

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -r main.ml this.ml $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/tony
cat > $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/tony/META <<EOF
# Specifications for the "tony" library:
requires = ""
version = "%{version}"
directory = "+tony"
archive(byte) = "tony.cma"
archive(native) = "tony.cmxa"
linkopts = ""
EOF

gzip -9nf *.mli README CHANGES mylib/{lc,pp,std}.mli mylib/COPYING

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc *.gz */*.gz
%dir %{_libdir}/ocaml/tony
%{_libdir}/ocaml/tony/*.cm[ixa]*
%{_libdir}/ocaml/tony/*.a
%{_examplesdir}/%{name}-%{version}
%{_libdir}/ocaml/site-lib/tony

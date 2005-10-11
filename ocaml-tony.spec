Summary:	Simplistic XML parser for OCaml
Summary(pl):	Prosty analizator sk³adniowy XML-a dla OCamla
Name:		ocaml-tony
Version:	0.9
Release:	4
License:	BSD
Group:		Libraries
Vendor:		Christian Lindig <lindig@ips.cs.tu-bs.de>
URL:		http://www.st.cs.uni-sb.de/~lindig/src/index.html
Source0:	http://www.st.cs.uni-sb.de/~lindig/src/ocaml-tony/tony-%{version}.tar.gz
# Source0-md5:	4dbf125c149a491f1c8dffef91792cb5
BuildRequires:	ocaml >= 3.07
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tony is a simple XML parser and pretty printer. The parser is non
validating and does neither comply fully to the standard nor does it
use the DOM for internal representation of a parsed XML file.

%description -l pl
Tony jest prostym analizatorem sk³adniowym XML-a. Mo¿e te¿ drukowaæ
XML z wciêciami. Analizator nie sprawdza wej¶cia wzglêdem DTD, nie jest
te¿ w pe³ni kompatybilny ze standardem, nie u¿ywa nawet DOM jako
wewnêtrznej reprezentacji.

%package devel
Summary:	Simplistic XML parser for OCaml - development part
Summary(pl):	Prosty analizator sk³adniowy XML-a dla OCamla - cze¶æ programistyczna
Group:		Development/Libraries
%requires_eq	ocaml

%description devel
Tony is a simple XML parser and pretty printer. The parser is non
validating and does neither comply fully to the standard nor does it
use the DOM for internal representation of a parsed XML file.

This package contains files needed to develop OCaml programs using
the Tony library.

%description devel -l pl
Tony jest prostym analizatorem sk³adniowym XML-a. Mo¿e te¿ drukowaæ
XML z wciêciami. Parser nie sprawdza wej¶cia wzglêdem DTD, nie jest
te¿ w pe³ni kompatybilny ze standardem, nie u¿ywa nawet DOM jako
wewnêtrznej reprezentacji.

Pakiet ten zawiera pliki niezbêdne do tworzenia programów u¿ywaj±cych
biblioteki Tony.

%prep
%setup -q -n tony-%{version}

%build
rm -f mylib/rc_scan.ml
%{__make} clean
%{__make}
%{__make} all.opt
ocamlc -a -o tony.cma \
	error.cmo mylib/{lc,pp,std,pc}.cmo xml.cmo xmlstate.cmo \
	xmlparse.cmo xmlscan.cmo
ocamlopt -a -o tony.cmxa \
	error.cmx mylib/{lc,pp,std,pc}.cmx xml.cmx xmlstate.cmx \
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

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc *.mli README CHANGES mylib/{lc,pp,std}.mli mylib/COPYING
%dir %{_libdir}/ocaml/tony
%{_libdir}/ocaml/tony/*.cm[ixa]*
%{_libdir}/ocaml/tony/*.a
%{_examplesdir}/%{name}-%{version}
%{_libdir}/ocaml/site-lib/tony

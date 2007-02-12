%define		ocaml_ver	1:3.09.2
Summary:	Simplistic XML parser for OCaml
Summary(pl.UTF-8):   Prosty analizator składniowy XML-a dla OCamla
Name:		ocaml-tony
Version:	0.9
Release:	8
License:	BSD
Group:		Libraries
URL:		http://www.st.cs.uni-sb.de/~lindig/src/index.html
Source0:	http://www.st.cs.uni-sb.de/~lindig/src/ocaml-tony/tony-%{version}.tar.gz
# Source0-md5:	4dbf125c149a491f1c8dffef91792cb5
BuildRequires:	ocaml >= %{ocaml_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tony is a simple XML parser and pretty printer. The parser is non
validating and does neither comply fully to the standard nor does it
use the DOM for internal representation of a parsed XML file.

%description -l pl.UTF-8
Tony jest prostym analizatorem składniowym XML-a. Może też drukować
XML z wcięciami. Analizator nie sprawdza wejścia względem DTD, nie
jest też w pełni kompatybilny ze standardem, nie używa nawet DOM jako
wewnętrznej reprezentacji.

%package devel
Summary:	Simplistic XML parser for OCaml - development part
Summary(pl.UTF-8):   Prosty analizator składniowy XML-a dla OCamla - cześć programistyczna
Group:		Development/Libraries
%requires_eq	ocaml

%description devel
Tony is a simple XML parser and pretty printer. The parser is non
validating and does neither comply fully to the standard nor does it
use the DOM for internal representation of a parsed XML file.

This package contains files needed to develop OCaml programs using the
Tony library.

%description devel -l pl.UTF-8
Tony jest prostym analizatorem składniowym XML-a. Może też drukować
XML z wcięciami. Parser nie sprawdza wejścia względem DTD, nie jest
też w pełni kompatybilny ze standardem, nie używa nawet DOM jako
wewnętrznej reprezentacji.

Pakiet ten zawiera pliki niezbędne do tworzenia programów używających
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

Name:		texlive-statistik
Version:	20334
Release:	1
Summary:	Store statistics of a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/statistik
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/statistik.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/statistik.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/statistik.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package counts the numbers of pages per chapter, and stores
the results in a separate file; the format of the file is
selectable.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/statistik/statistik.sty
%doc %{_texmfdistdir}/doc/latex/statistik/sta_cvs.tex
%doc %{_texmfdistdir}/doc/latex/statistik/sta_mytable.tex
%doc %{_texmfdistdir}/doc/latex/statistik/sta_tab.tex
%doc %{_texmfdistdir}/doc/latex/statistik/sta_textable.tex
%doc %{_texmfdistdir}/doc/latex/statistik/sta_xml.tex
%doc %{_texmfdistdir}/doc/latex/statistik/statistik.pdf
#- source
%doc %{_texmfdistdir}/source/latex/statistik/statistik.dtx
%doc %{_texmfdistdir}/source/latex/statistik/statistik.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

# revision 20334
# category Package
# catalog-ctan /macros/latex/contrib/statistik
# catalog-date 2010-11-05 12:45:12 +0100
# catalog-license gpl
# catalog-version 0.03
Name:		texlive-statistik
Version:	0.03
Release:	1
Summary:	Store statistics of a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/statistik
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/statistik.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/statistik.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/statistik.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package counts the numbers of pages per chapter, and stores
the results in a separate file; the format of the file is
selectable.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}

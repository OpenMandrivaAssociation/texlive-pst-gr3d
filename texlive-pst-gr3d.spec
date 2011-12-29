# revision 15878
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-gr3d
# catalog-date 2006-12-19 19:38:44 +0100
# catalog-license lppl
# catalog-version 1.34
Name:		texlive-pst-gr3d
Version:	1.34
Release:	1
Summary:	Three dimensional grids with PSTricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-gr3d
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-gr3d.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-gr3d.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-gr3d.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This PSTricks package provides a command \PstGridThreeD that
will draw a three dimensional grid, offering a number of
options for its appearance.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/pst-gr3d/pst-gr3d.tex
%{_texmfdistdir}/tex/latex/pst-gr3d/pst-gr3d.sty
%doc %{_texmfdistdir}/doc/generic/pst-gr3d/Changes
%doc %{_texmfdistdir}/doc/generic/pst-gr3d/README
%doc %{_texmfdistdir}/doc/generic/pst-gr3d/pst-gr3d.pdf
#- source
%doc %{_texmfdistdir}/source/latex/pst-gr3d/pst-gr3d.dtx
%doc %{_texmfdistdir}/source/latex/pst-gr3d/pst-gr3d.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

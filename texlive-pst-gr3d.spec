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
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This PSTricks package provides a command \PstGridThreeD that
will draw a three dimensional grid, offering a number of
options for its appearance.

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
%{_texmfdistdir}/tex/generic/pst-gr3d/pst-gr3d.tex
%{_texmfdistdir}/tex/latex/pst-gr3d/pst-gr3d.sty
%doc %{_texmfdistdir}/doc/generic/pst-gr3d/Changes
%doc %{_texmfdistdir}/doc/generic/pst-gr3d/README
%doc %{_texmfdistdir}/doc/generic/pst-gr3d/pst-gr3d.pdf
#- source
%doc %{_texmfdistdir}/source/latex/pst-gr3d/pst-gr3d.dtx
%doc %{_texmfdistdir}/source/latex/pst-gr3d/pst-gr3d.ins
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

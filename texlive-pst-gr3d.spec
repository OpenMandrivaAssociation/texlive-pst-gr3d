%global tl_name pst-gr3d
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.34
Release:	%{tl_revision}.1
Summary:	Three dimensional grids with PSTricks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-gr3d
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-gr3d.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-gr3d.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-gr3d.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This PSTricks package provides a command \PstGridThreeD that will draw a
three dimensional grid, offering a number of options for its appearance.


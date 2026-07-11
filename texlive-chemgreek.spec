%global tl_name chemgreek
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1a
Release:	%{tl_revision}.1
Summary:	Upright Greek letters in chemistry
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/chemgreek
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chemgreek.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chemgreek.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides upright Greek letters in support of other chemistry
packages (such as chemmacros). The package used to be distributed as a
part of chemmacros.


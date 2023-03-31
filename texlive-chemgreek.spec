Name:		texlive-chemgreek
Version:	53437
Release:	2
Summary:	Upright Greek letters in chemistry
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chemgreek
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemgreek.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemgreek.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides upright Greek letters in support of other
chemistry packages (such as chemmacros). The package used to be
distributed as a part of chemmacros.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/chemgreek
%doc %{_texmfdistdir}/doc/latex/chemgreek

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

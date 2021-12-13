Summary:	A simple library for font loading and glyph rasterization
Name:		fcft
Version:	2.5.1
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	https://codeberg.org/dnkl/fcft/archive/%{version}.tar.gz
# Source0-md5:	19b2f122d28c90832418fdf94baec5d4
URL:		https://codeberg.org/dnkl/fcft
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 2
BuildRequires:	harfbuzz-devel
BuildRequires:	libutf8proc-devel
BuildRequires:	meson >= 0.54.0
BuildRequires:	ninja
BuildRequires:	pixman-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	scdoc
BuildRequires:	tllist-devel >= 1.0.1
BuildRequires:	wayland-devel
BuildRequires:	wayland-protocols
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fcft is a small font loading and glyph rasterization library built
on-top of FontConfig, FreeType2 and pixman.

It can load and cache fonts from a fontconfig-formatted name string,
e.g. Monospace:size=12, optionally with user configured fallback
fonts.

After a font has been loaded, you can rasterize glyphs. When doing so,
the primary font is first considered. If it does not have the
requested glyph, the user configured fallback fonts (if any) are
considered. If none of the user configured fallback fonts has the
requested glyph, the FontConfig generated list of fallback fonts are
checked.

%package devel
Summary:	Header files for the fcft library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for the fcft library.

%package static
Summary:	Static fcft library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static fcft library.

%prep
%setup -q -n %{name}

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md README.md
%attr(755,root,root) %{_libdir}/libfcft.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libfcft.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfcft.so
%dir %{_includedir}/fcft
%{_includedir}/fcft/fcft.h
%{_includedir}/fcft/stride.h
%{_pkgconfigdir}/fcft.pc
%{_mandir}/man3/fcft_*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libfcft.a
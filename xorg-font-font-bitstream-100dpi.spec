Summary:	bitstream-100dpi font
Summary(pl):	Font bitstream-100dpi
Name:		xorg-font-font-bitstream-100dpi
Version:	0.99.1
Release:	0.1
License:	MIT
Group:		Fonts
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC3/font/font-bitstream-100dpi-%{version}.tar.bz2
# Source0-md5:	31892d08774016a55f58a57f4e5e95be
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-util-util-macros
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/100dpi
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bitstream-100dpi font.

%description -l pl
Font bitstream-100dpi.

%prep
%setup -q -n font-bitstream-100dpi-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-fontdir=%{_fontsdir}/100dpi

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst 100dpi

%postun
fontpostinst 100dpi

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%{_fontsdir}/100dpi/*.pcf.gz

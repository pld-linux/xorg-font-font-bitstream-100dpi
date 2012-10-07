Summary:	Bitstream 100dpi bitmap fonts
Summary(pl.UTF-8):	Fonty bitmapowe 100dpi Bitstream
Name:		xorg-font-font-bitstream-100dpi
Version:	1.0.3
Release:	2
License:	MIT
Group:		Fonts
Source0:	http://xorg.freedesktop.org/releases/individual/font/font-bitstream-100dpi-%{version}.tar.bz2
# Source0-md5:	6b223a54b15ecbd5a1bc52312ad790d8
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-font-font-util >= 1.2
BuildRequires:	xorg-util-util-macros >= 1.3
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/100dpi
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bitstream 100dpi bitmap fonts: Charter and Terminal.

%description -l pl.UTF-8
Fonty bitmapowe 100dpi Bitstream: Charter i Terminal.

%prep
%setup -q -n font-bitstream-100dpi-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--build=%{_host} \
	--host=%{_host} \
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
%doc COPYING ChangeLog README
%{_fontsdir}/100dpi/char*.pcf.gz
%{_fontsdir}/100dpi/tech*.pcf.gz
%{_fontsdir}/100dpi/term*.pcf.gz

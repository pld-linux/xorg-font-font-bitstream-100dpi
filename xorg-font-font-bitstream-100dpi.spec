# $Rev: 3202 $, $Date: 2005-08-15 12:17:57 $
#
Summary:	font-bitstream-100dpi
Summary(pl):	font-bitstream-100dpi
Name:		xorg-font-font-bitstream-100dpi
Version:	0.99.0
Release:	0.01
License:	MIT
Group:		X11
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/font/font-bitstream-100dpi-%{version}.tar.bz2
# Source0-md5:	d5f1ac2764b3bc7e4fdd7ef6c3078af2
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-font-font-util
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/font-bitstream-100dpi-%{version}-root-%(id -u -n)

%description
font-bitstream-100dpi

%description -l pl
font-bitstream-100dpi


%prep
%setup -q -n font-bitstream-100dpi-%{version}


%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%{_libdir}/X11/fonts/100dpi/*

Summary:	Win32 DLLs plugin for XMPS
Summary(pl.UTF-8):	Obsługa Win32 DLL dla odtwarzacza XMPS
Name:		xmps-win32-plugin
Version:	0.0.4
Release:	2
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	14a4677fca132d326dde36277f8f912c
Requires:	xmps
Requires:	w32codec
BuildRequires:	xmps-devel >= 0.2.0
BuildRequires:	libstdc++-devel
BuildRequires:	mawk
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
The XMPS win32 plugin will allow XMPS to use the windows dlls to
decode various video formats, including Intel Indeo 5.0 and DivX ;-).

%description -l pl.UTF-8
Wtyczka win32 umożliwiająca odtwarzaczowi XMPS używanie windowsowych
bibliotek dll do dekodowania formatów wideo włączając w to Intel Indeo
5.0 oraz DivX ;-).

%prep
%setup  -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	--enable-static=no

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/xmps/*/*/*.so

Summary:	Win32 DLLs plugin for XMPS
Summary(pl):	Obs³uga Win32 DLL dla odtwarzacza XMPS
Name:		xmps-win32-plugin
Version:	0.0.4
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source0:	http://xmps.sourceforge.net/sources/%{name}-%{version}.tar.gz
URL:		http://xmps.sourceforge.net/plugins.php3
Requires:	xmps
Requires:	avi-codecs
BuildRequires:	xmps-devel >= 0.2.0
BuildRequires:	libstdc++-devel
BuildRequires:	mawk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
The XMPS win32 plugin will allow XMPS to use the windows dlls to
decode various video formats, including Intel Indeo 5.0 and DivX ;-).

%description -l pl
Wtyczka win32 umo¿liwiaj±ca odtwarzaczowi XMPS u¿ywanie windowsowych
bibliotek dll do dekodowania formatów wideo w³±czaj±c w to Intel Indeo
5.0 oraz DivX ;-).

%prep
%setup  -q

%build
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

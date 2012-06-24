%define		_sc_ver	0.5.9
%define	_pre	pre1
Summary:	Stand-alone SoftCAM
Summary(pl):	Stand-alone SoftCAM
Name:		sasc
Version:	0.6
Release:	0.%{_pre}.1
License:	- (enter GPL/GPL v2/LGPL/BSD/BSD-like/other license name here)
Group:		Applications
Source0:	http://www.oldskools.org/%{name}-%{version}.%{_pre}.tar.bz2
# Source0-md5:	d8f1c71d644bd7acc40ee6c2491a17e4
Source1:	http://207.44.152.197/vdr-sc-%{_sc_ver}.tar.gz
# Source1-md5:	cbd648dd4b7e9f8d08d86fc75a6681b0
#Patch0: %{name}-DESTDIR.patch
Requires:	vdr-sc = %{_sc_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sasc is an application that allows using the vdr 'sc' plugin as a
stand alone executable. This gives you the capability to use the
powerful softCam library in programs other than vdr.

%description -l pl
sasc pozwala na u�ywanie wtyczki 'sc' przeznaczonej dla vdr jako
niezale�nej aplikacji. To daje mo�liwosc ko�ystania z biblioteki
softCam w programach innych niz vdr.

%package vdr-sc
Summary:	SoftCAM plugin for VDR
Summary(pl):	Wtyczka SoftCAM dla VDR
Group:		Applications
Provides:	vdr-sc

%description vdr-sc
It's not legal to use this software in most countries of the world. SC
means softcam, which means a software CAM emulation.

%description vdr-sc -l pl
U�ywanie tego oprogramowania jest nielegalne we wi�kszo�ci kraj�w
�wiata. SC znaczy softcam, co oznacza programowa emulacje CAM.

%prep
%setup -q -n %{name}-%{version}.%{_pre}
cd PLUGINS/src/
/bin/gzip -dc %{SOURCE1} | tar -xf -
patch -p0 < ../../patches/sc-%{_sc_ver}-mecm.patch

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_libdir}
install %{name} $RPM_BUILD_ROOT%{_bindir}
install PLUGINS/lib/lib*.so.* $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	vdr-sc -p /sbin/ldconfig
%postun	vdr-sc -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Changelog README
%attr(755,root,root) %{_bindir}/*

%files vdr-sc
%defattr(644,root,root,755)
%doc PLUGINS/src/sc-%{_sc_ver}/HISTORY PLUGINS/src/sc-%{_sc_ver}/README
%attr(755,root,root) %{_libdir}

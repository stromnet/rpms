# $Id$
# Authority: dag

# ExcludeDist: el2 rh7 rh9 el3 el4

### Disable stripping
%define __spec_install_post /usr/lib/rpm/brp-compress

%define real_name libflashplayer

Summary: Macromedia Flash Player
Name: flash-plugin
Version: 10.0.22.87
Release: 1
License: Commercial
Group: Applications/Internet
URL: http://www.macromedia.com/downloads/

Source: http://download.macromedia.com/pub/labs/flashplayer10/libflashplayer-%{version}.linux-x86_64.so.tar.gz
Source1: README
Source2: LICENSE
Source3: homecleanup
Source4: setup64
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: x86_64
Obsoletes: mozilla-flash <= %{version}-%{release}
#Requires: %{_libdir}/mozilla/plugins/

%description
Macromedia Flash Player

By downloading and installing this package you agree to the included LICENSE.

%prep
%setup -c
%{__install} -Dp -m0644 %{SOURCE1} LICENSE
%{__install} -Dp -m0644 %{SOURCE2} README

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 libflashplayer.so %{buildroot}%{_libdir}/flash-plugin/libflashplayer.so
%{__install} -Dp -m0644 %{SOURCE1} %{buildroot}%{_libdir}/flash-plugin/LICENSE
%{__install} -Dp -m0644 %{SOURCE2} %{buildroot}%{_libdir}/flash-plugin/README
%{__install} -Dp -m0755 %{SOURCE3} %{buildroot}%{_libdir}/flash-plugin/homecleanup
%{__install} -Dp -m0755 %{SOURCE4} %{buildroot}%{_libdir}/flash-plugin/setup

%post
if [ $1 -eq 1 ]; then
    %{_libdir}/flash-plugin/setup install
elif [ $1 -eq 2 ]; then
    %{_libdir}/flash-plugin/setup upgrade
fi

%preun
if [ $1 -eq 0 ]; then
    %{_libdir}/flash-plugin/setup preun
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README
%{_libdir}/flash-plugin/

%changelog
* Thu Apr 16 2009 Dag Wieers <dag@wieers.com> - 10.0.22.87.
- Updated to release 10.0.22.87.

* Fri Dec 19 2008 Dag Wieers <dag@wieers.com> - 10.0.d21.1-1
- Initial test-release for x86_64.

* Thu Dec 18 2008 Dag Wieers <dag@wieers.com> - 10.0.15.3-1
- Updated to release 10.0.15.3.

* Mon Nov 03 2008 Dag Wieers <dag@wieers.com> - 10.0.12.36-2
- Include setup and homecleanup like upstream.

* Tue Oct 28 2008 Dag Wieers <dag@wieers.com> - 10.0.12.36-1
- Updated to release 10.0.12.36.

* Wed Apr 23 2008 Dag Wieers <dag@wieers.com> - 9.0.124.0-1
- Updated to release 9.0.124.0.

* Wed Dec 05 2007 Dag Wieers <dag@wieers.com> - 9.0.115.0-1
- Updated to release 9.0.115.0.

* Thu Jul 19 2007 Dag Wieers <dag@wieers.com> - 9.0.48.0-1
- Updated to release 9.0.48.0.

* Wed Jan 17 2007 Dag Wieers <dag@wieers.com> - 9.0.31.0-1
- Updated to release 9.0.31.0.

* Wed Jan 10 2007 Dag Wieers <dag@wieers.com> - 7.0.69-1
- Updated to release 7.0.69.

* Tue Sep 12 2006 Dag Wieers <dag@wieers.com> - 7.0.68-1
- Updated to release 7.0.68.
- Renamed package from mozilla-flash to flash-plugin.

* Wed Mar 15 2006 Dag Wieers <dag@wieers.com> - 7.0.63-1
- Updated to release 7.0.63.

* Sat Nov 26 2005 Dag Wieers <dag@wieers.com> - 7.0.61-1
- Updated to release 7.0.61.

* Sun Jun 27 2004 Dag Wieers <dag@wieers.com> - 7.0.25-1
- Initial package. (using DAR)

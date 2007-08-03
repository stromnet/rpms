# $Id$
# Authority: dag
# Upstream: Andy Armstrong <andy$hexten,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name CGI-Simple

Summary: Perl module that implements a CGI.pm compliant CGI interface
Name: perl-CGI-Simple
Version: 0.080
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CGI-Simple/

Source: http://www.cpan.org/modules/by-module/CGI/CGI-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)
Requires: perl

%description
CGI-Simple is a perl module that implements a CGI.pm compliant CGI interface.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README SIGNATURE
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/CGI/
%{perl_vendorlib}/CGI/Simple/
%{perl_vendorlib}/CGI/Simple.pm

%changelog
* Sun Apr 29 2007 Dag Wieers <dag@wieers.com> - 0.080-1
- Initial package. (using DAR)

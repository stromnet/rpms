# $Id$
# Authority: dag
# Upstream: Fergal Daly <fergal$esatclear,ie>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Tester

Summary: Perl module to ease testing test modules built with Test::Builder
Name: perl-Test-Tester
Version: 0.104
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Tester/

Source: http://www.cpan.org/modules/by-module/Test/Test-Tester-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
perl-Test-Tester is a Perl module to ease testing test modules
built with Test::Builder.

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
%doc ARTISTIC CHANGES MANIFEST META.yml README TODO
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Test/
%{perl_vendorlib}/Test/Tester/
%{perl_vendorlib}/Test/Tester.pm

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.104-1
- Initial package. (using DAR)

# $Id$
# Authority: dag
# Upstream: Simon Cozens <simon$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-DBI-Plugin-Type

Summary: Perl module to determine type information for columns
Name: perl-Class-DBI-Plugin-Type
Version: 0.02
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-DBI-Plugin-Type/

Source: http://www.cpan.org/modules/by-module/Class/Class-DBI-Plugin-Type-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)
Requires: perl

%description
Class-DBI-Plugin-Type is a Perl module to determine type information
for columns.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Class::DBI::Plugin::Type.3pm*
%dir %{perl_vendorlib}/Class/
%dir %{perl_vendorlib}/Class/DBI/
%dir %{perl_vendorlib}/Class/DBI/Plugin/
%{perl_vendorlib}/Class/DBI/Plugin/Type.pm

%changelog
* Mon Apr 30 2007 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)

# $Id$
# Authority: dries

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name YAML-Active

Summary: Combine data and logic in YAML
Name: perl-YAML-Active
Version: 1.100810
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/YAML-Active/

Source: http://search.cpan.org/CPAN/authors/id/M/MA/MARCEL/YAML-Active-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl(Carp)
BuildRequires: perl(Class::Accessor::Complex)
BuildRequires: perl(English)
BuildRequires: perl(Exporter)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Scalar::Util)
#BuildRequires: perl(Test::More) >= 0.88
BuildRequires: perl(Test::More)
BuildRequires: perl(YAML::XS)
BuildRequires: perl(constant)
BuildRequires: perl >= 5.008
Requires: perl(Carp)
Requires: perl(Class::Accessor::Complex)
Requires: perl(English)
Requires: perl(Exporter)
Requires: perl(File::Find)
Requires: perl(File::Temp)
Requires: perl(Scalar::Util)
#Requires: perl(Test::More) >= 0.88
Requires: perl(Test::More)
Requires: perl(YAML::XS)
Requires: perl(constant)
Requires: perl >= 5.008

%filter_from_requires /^perl*/d
%filter_setup

%description
YAML is an intuitive way to describe nested data structures. This module
extends YAML's capabilities so that it ceases to be a static data
structure and become something more active, with data and logic
combined. This makes the logic reusable since it is bound to the data
structure. Without "YAML::Active", you have to load the YAML data, then
process it in some way. The logic describing which parts of the data
have to be processed and how was separated from the data. Using
"YAML::Active", the description of how to process the data can be
encapsulated in the data structure itself.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" --skipdeps
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
%doc %{_mandir}/man3/YAML::Active*.3pm*
%dir %{perl_vendorlib}/YAML/
%{perl_vendorlib}/YAML/Active/
%{perl_vendorlib}/YAML/Active.pm

%changelog
* Fri Mar 26 2010 Christoph Maser <cmr@financial.com> - 1.100810-1
- Updated to version 1.100810.

* Fri May 29 2009 Christoph Maser <cmr@financial.com> - 1.08-1
- Updated to version 1.08.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 1.06-1
- Updated to release 1.06.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.00-1
- Initial package.

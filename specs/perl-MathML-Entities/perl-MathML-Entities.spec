# $Id$
# Authority: dries
# Upstream: Jacques Distler <distler$golem,ph,utexas,edu>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MathML-Entities

Summary: Convert XHTML+MathML Named Entities to Numeric Character References
Name: perl-MathML-Entities
Version: 0.17
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MathML-Entities/

Source: http://www.cpan.org/modules/by-module/MathML/MathML-Entities-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
MathML::Entities a content conversion filter for named XHTML+MathML
entities.

%prep
%setup -n %{real_name}

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
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/MathML/Entities.pm

%changelog
* Fri Dec 11 2009 Christoph Maser <cmr@financial.com> - 0.17-1
- Updated to version 0.17.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.13-1.2
- Rebuild for Fedora Core 5.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.13-1
- Initial package.

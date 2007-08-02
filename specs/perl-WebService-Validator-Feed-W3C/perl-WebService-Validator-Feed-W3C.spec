# $Id$
# Authority: dries
# Upstream: Olivier Thereaux <ot$w3,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name WebService-Validator-Feed-W3C

Summary: Find errors in feeds
Name: perl-WebService-Validator-Feed-W3C
Version: 0.5
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WebService-Validator-Feed-W3C/

Source: http://search.cpan.org/CPAN/authors/id/O/OL/OLIVIERT/WebService/WebService-Validator-Feed-W3C-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
This module is an experimental interface to the W3C Feed Validation online
service <http://validator.w3.org/feed/>, based on its experimental
SOAP 1.2 support. It helps to find errors in RSS or ATOM feeds.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/WebService/Validator/Feed/W3C.pm

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.5-1
- Updated to release 0.5.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.3-1
- Updated to release 0.3.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.2-1
- Updated to release 0.2.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.1-1.2
- Rebuild for Fedora Core 5.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.1-1
- Initial package.

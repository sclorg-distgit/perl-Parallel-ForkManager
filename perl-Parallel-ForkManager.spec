%{?scl:%scl_package perl-Parallel-ForkManager}

# Control optional test
%if ! (0%{?rhel}) && ! (0%{?scl:1})
%bcond_without perl_Parallel_ForkManager_enables_optional_test
%else
%bcond_with perl_Parallel_ForkManager_enables_optional_test
%endif

Name:           %{?scl_prefix}perl-Parallel-ForkManager
Version:        1.20
Release:        2%{?dist}
Summary:        Simple parallel processing fork manager
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            https://metacpan.org/release/Parallel-ForkManager
Source0:        https://cpan.metacpan.org/authors/id/Y/YA/YANICK/Parallel-ForkManager-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl-interpreter
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(warnings)
BuildRequires:  sed
# Run-time
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(File::Path)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(File::Temp)
BuildRequires:  %{?scl_prefix}perl(POSIX)
BuildRequires:  %{?scl_prefix}perl(Storable)
# Tests
BuildRequires:  %{?scl_prefix}perl(CPAN::Meta)
BuildRequires:  %{?scl_prefix}perl(IO::Handle)
BuildRequires:  %{?scl_prefix}perl(IPC::Open3)
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.94
BuildRequires:  %{?scl_prefix}perl(Test::Warn)
%if %{with perl_Parallel_ForkManager_enables_optional_test}
# Optional tests
BuildRequires:  %{?scl_prefix}perl(utf8::all)
%endif


Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))

%description
This module is intended for use in operations that can be done in parallel
where the number of processes to be forked off should be limited. Typical
use is a downloader which will be retrieving hundreds/thousands of files.

%prep
%setup -q -n Parallel-ForkManager-%{version}

# Prepare the example scripts for inclusion as documentation, as they are not
# generally useful and have additional dependencies.
sed -i -e '1d' examples/*.pl
chmod 644 examples/*.pl

i=lib/Parallel/ForkManager.pm
iconv -f iso-8859-1 -t utf-8 < $i > $i. && touch -r $i $i. && mv -f $i. $i

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install PERL_INSTALL_ROOT=%{buildroot}%{?scl:'}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc Changes examples/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jan 03 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.20-2
- SCL

* Thu Jul 19 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.20-1
- Update to 1.20.
- Add CPAN::Meta build dependency.
- Fix RHEL conditional to be version-limited.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.19-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.19-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Aug 26 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.19-1
- 1.19 bump

* Mon Jun 27 2016 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.18-5
- Oops, wrong build dep.

* Thu Jun 23 2016 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.18-4
- Change build dependencies to new recommended usage.

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.18-3
- Perl 5.24 rebuild

* Thu Mar 31 2016 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.18-2
- Run iconv on the right file.

* Tue Mar 29 2016 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.18-1
- Update to 1.18.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.17-2
- Remove pointless %%defattr statement.

* Wed Dec 02 2015 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.17-1
- Update to 1.17.

* Thu Oct 08 2015 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.16-1
- Update to 1.16; rhbz#1270082.  Add new Test::Warn build dep.

* Fri Aug 07 2015 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.15-2
- Add a couple of build dependencies that dropped out of the dep tree.

* Wed Jul 08 2015 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.15-1
- Update to latest upstream version.

* Tue Jun 23 2015 Marianne Lombard <jehane@fedoraproject.org> - 1.14
- Update to latest upstream version

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.12-2
- Perl 5.22 rebuild

* Tue Feb 24 2015 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.12-1
- Update to latest upstream version.
- Use most direct download location.

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.05-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 17 2013 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.05-1
- Update to 1.05; new source location, additional build deps.  Should fix the
  longstanding security bug, 751886.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.7.9-8
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.7.9-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.7.9-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 24 2011 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.7.9-1
- Update to current upstream version.
- Handle new upstream treatment of the examples.
- Update to modern packaging guidelines.

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.7.5-7
- 661697 rebuild for fixing problems with vendorach/lib

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.7.5-6
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.7.5-5
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.7.5-2
Rebuild for new perl

* Wed Jan 16 2008 Jason Tibbitts <tibbs@math.uh.edu> 0.7.5-1
- Specfile autogenerated by cpanspec 1.74.
- Make the .pl files documentation instead of installing them to avoid
  additional dependencies.  Also remove their shebang lines to quiet rpmlint.

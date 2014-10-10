%define upstream_name    Socket-GetAddrInfo
%define upstream_version 0.22

%define debug_package %{nil}

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	2

Summary:    RFC 2553's C<getaddrinfo> and C<getnameinfo>
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://search.cpan.org/CPAN/authors/id/P/PE/PEVANS/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::CBuilder)
BuildRequires: perl-ExtUtils-CChecker
BuildRequires: perl(Module::Build)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl-devel
BuildRequires: perl-Test-Warn
#gw for getaddrinfo:
Conflicts: ruli-tools

%description
The RFC 2553 functions 'getaddrinfo' and 'getnameinfo' provide an
abstracted way to convert between a pair of host name/service name and
socket addresses, or vice versa. 'getaddrinfo' converts names into a set of
arguments to pass to the 'socket()' and 'connect()' syscalls, and
'getnameinfo' converts a socket address back into its host name/service
name pair.

These functions provide a useful interface for performing either of these
name resolution operation, without having to deal with IPv4/IPv6
transparency, or whether the underlying host can support IPv6 at all, or
other such issues. However, not all platforms can support the underlying
calls at the C layer, which means a dilema for authors wishing to write
forward-compatible code. Either to support these functions, and cause the
code not to work on older platforms, or stick to the older "legacy"
resolvers such as 'gethostbyname()', which means the code becomes more
portable.

This module attempts to solve this problem, by detecting at compiletime
whether the underlying OS will support these functions, and only compiling
the XS code if it can. At runtime, when the module is loaded, if the XS
implementation is not available, emulations of the functions using the
legacy resolver functions instead. The emulations support the same
interface as the real functions, and behave as close as is resonably
possible to emulate using the legacy resolvers. See below for details on
the limits of this emulation.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%{_mandir}/man1/*
%perl_vendorlib/*
%_bindir/getaddrinfo
%_bindir/getnameinfo




%changelog
* Mon Jun 04 2012 Götz Waschk <waschk@mandriva.org> 0.220.0-1
+ Revision: 802297
- update to new version 0.22

* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.210.0-2
+ Revision: 768358
- mass rebuild of perl extensions against perl 5.14.2

* Fri Apr 22 2011 Götz Waschk <waschk@mandriva.org> 0.210.0-1
+ Revision: 656659
- update to new version 0.21

* Sat Jan 29 2011 Götz Waschk <waschk@mandriva.org> 0.200.0-1
+ Revision: 633864
- new version
- update file list
- add conflict with ruli-tools

* Sat Oct 16 2010 Götz Waschk <waschk@mandriva.org> 0.190.0-1mdv2011.0
+ Revision: 585999
- update to new version 0.19

* Thu Sep 16 2010 Götz Waschk <waschk@mandriva.org> 0.180.0-1mdv2011.0
+ Revision: 578820
- update to new version 0.18

* Wed Sep 15 2010 Götz Waschk <waschk@mandriva.org> 0.170.0-1mdv2011.0
+ Revision: 578427
- update to new version 0.17

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.160.0-2mdv2011.0
+ Revision: 556145
- rebuild for perl 5.12

* Fri Jul 16 2010 Jérôme Quelin <jquelin@mandriva.org> 0.160.0-1mdv2011.0
+ Revision: 553974
- update to 0.16

* Sat Jan 30 2010 Götz Waschk <waschk@mandriva.org> 0.150.0-1mdv2010.1
+ Revision: 498481
- new version
- update deps

* Fri Dec 25 2009 Götz Waschk <waschk@mandriva.org> 0.140.0-1mdv2010.1
+ Revision: 482201
- new version
- fix source URL

  + Jérôme Quelin <jquelin@mandriva.org>
    - update to 0.13

* Mon Sep 14 2009 Götz Waschk <waschk@mandriva.org> 0.130.0-1mdv2010.0
+ Revision: 439392
- update build deps
- update to new version 0.13

* Mon Jun 29 2009 Götz Waschk <waschk@mandriva.org> 0.120.0-1mdv2010.0
+ Revision: 390466
- import perl-Socket-GetAddrInfo


* Mon Jun 29 2009 cpan2dist 0.12-1mdv
- initial mdv release, generated with cpan2dist


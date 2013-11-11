%define upstream_name	 Catalyst-Plugin-Static-Simple
%define upstream_version 0.31

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Make serving static pages painless
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Catalyst/Catalyst-Plugin-Static-Simple-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst) >= 5.70
BuildRequires:	perl(Class::Data::Inheritable)
BuildRequires:	perl(MIME::Types) >= 1.15
BuildRequires:	perl(MRO::Compat)
BuildArch:	noarch

%description
The Static::Simple plugin is designed to make serving static content
in your application during development quick and easy, without
requiring a single line of code from you.

This plugin detects static files by looking at the file extension in
the URL (such as B<.css> or B<.png> or B<.js>). The plugin uses the
lightweight L<MIME::Types> module to map file extensions to
IANA-registered MIME types, and will serve your static files with the
correct MIME type directly to the browser, without being processed
through Catalyst.


%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL installdirs=vendor --skipdeps
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/*/*
%{perl_vendorlib}/Catalyst


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.290.0-2mdv2011.0
+ Revision: 680765
- mass rebuild

* Tue Feb 02 2010 Jérôme Quelin <jquelin@mandriva.org> 0.290.0-1mdv2011.0
+ Revision: 499484
- update to 0.29

* Tue Jan 05 2010 Jérôme Quelin <jquelin@mandriva.org> 0.280.0-1mdv2010.1
+ Revision: 486306
- update to 0.28

* Mon Jan 04 2010 Jérôme Quelin <jquelin@mandriva.org> 0.270.0-1mdv2010.1
+ Revision: 486116
- update to 0.27

* Mon Dec 07 2009 Jérôme Quelin <jquelin@mandriva.org> 0.260.0-1mdv2010.1
+ Revision: 474408
- update to 0.26

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.250.0-1mdv2010.1
+ Revision: 461736
- update to 0.25

* Mon Aug 31 2009 Jérôme Quelin <jquelin@mandriva.org> 0.220.0-1mdv2010.0
+ Revision: 422887
- update to 0.22

* Sun Aug 02 2009 Jérôme Quelin <jquelin@mandriva.org> 0.210.0-1mdv2010.0
+ Revision: 407513
- adding missing buildrequires:
- rebuild using %%perl_convert_version

* Mon May 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.21-1mdv2010.0
+ Revision: 371667
- update to new version 0.21

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.20-3mdv2009.0
+ Revision: 255571
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Oct 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.20-1mdv2008.1
+ Revision: 97373
- update to new version 0.20

* Tue Jul 03 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.19-1mdv2008.0
+ Revision: 47625
- update to new version 0.19

* Mon Jul 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.18-1mdv2008.0
+ Revision: 47031
- update to new version 0.18

* Sun May 20 2007 Olivier Thauvin <nanardon@mandriva.org> 0.17-1mdv2008.0
+ Revision: 28824
- 0.17

* Mon Apr 30 2007 Olivier Thauvin <nanardon@mandriva.org> 0.15-1mdv2008.0
+ Revision: 19701
- 0.15


* Thu Jun 29 2006 Scott Karns <scott@karnstech.com> 0.14-1mdv2007.0
- Initial Mandriva RPM





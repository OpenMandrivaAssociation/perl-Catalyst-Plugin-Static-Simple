%define upstream_name	 Catalyst-Plugin-Static-Simple
%define upstream_version 0.27

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Make serving static pages painless
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Catalyst) >= 5.70
BuildRequires:	perl(Class::Data::Inheritable)
BuildRequires:	perl(MIME::Types) >= 1.15
BuildRequires:	perl(MRO::Compat)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

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
%__perl Makefile.PL installdirs=vendor --skipdeps
%make

%check
make test

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/*/*
%{perl_vendorlib}/Catalyst

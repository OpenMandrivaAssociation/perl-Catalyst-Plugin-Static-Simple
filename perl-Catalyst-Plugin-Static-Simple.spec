%define upstream_name	 Catalyst-Plugin-Static-Simple
%define upstream_version 0.38

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1

Summary:	Make serving static pages painless

License:	Artistic/GPL
Group:		Development/Perl
Url:		https://github.com/perl-catalyst/Catalyst-Plugin-Static-Simple
Source0:	https://cpan.metacpan.org/authors/id/E/ET/ETHER/Catalyst-Plugin-Static-Simple-%{upstream_version}.tar.gz

BuildRequires:	make
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




%define module	Catalyst-Plugin-Static-Simple
%define name	perl-%{module}
%define	modprefix Catalyst

%define version	0.21
%define release	%mkrel 1

Summary:	Make serving static pages painless
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{module}-%{version}.tar.gz
BuildRequires:	perl(Catalyst) >= 5.70
BuildRequires:	perl(MIME::Types) >= 1.15
BuildRequires:	perl(MRO::Compat)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version}

%build
%__perl Makefile.PL installdirs=vendor --skipdeps
%make

%check
make test

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/*/*
%{perl_vendorlib}/Catalyst

%clean
rm -rf %{buildroot}


#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-XML-Dumper
Version  : 0.81
Release  : 1
URL      : https://cpan.metacpan.org/authors/id/M/MI/MIKEWONG/XML-Dumper-0.81.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MI/MIKEWONG/XML-Dumper-0.81.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-XML-Dumper-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(XML::Parser)

%description
======================
XML::Dumper dumps Perl data to a structured XML format.
XML::Dumper can also read XML data that was previously dumped
by the module and convert it back to Perl.

%package dev
Summary: dev components for the perl-XML-Dumper package.
Group: Development
Provides: perl-XML-Dumper-devel = %{version}-%{release}
Requires: perl-XML-Dumper = %{version}-%{release}

%description dev
dev components for the perl-XML-Dumper package.


%package perl
Summary: perl components for the perl-XML-Dumper package.
Group: Default
Requires: perl-XML-Dumper = %{version}-%{release}

%description perl
perl components for the perl-XML-Dumper package.


%prep
%setup -q -n XML-Dumper-0.81
cd %{_builddir}/XML-Dumper-0.81

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/XML::Dumper.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/XML/Dumper.pm

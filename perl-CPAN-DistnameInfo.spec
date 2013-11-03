#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
Summary:	Extract distribution name and version from a distribution filename
Name:		perl-CPAN-DistnameInfo
Version:	0.12
Release:	1
License:	GPL+ or Artistic
Group:		Development/Libraries
Source0:	http://www.cpan.org/authors/id/G/GB/GBARR/CPAN-DistnameInfo-%{version}.tar.gz
# Source0-md5:	06bc803c0e4fb7735ddc7282163f1cc3
URL:		http://search.cpan.org/dist/CPAN-DistnameInfo/
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(Test::More)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Many online services that are centered around CPAN attempt to
associate multiple uploads by extracting a distribution name from the
filename of the upload. For most distributions this is easy as they
have used ExtUtils::MakeMaker or Module::Build to create the
distribution, which results in a uniform name. But sadly not all
uploads are created in this way.

CPAN::DistnameInfo uses heuristics that have been learnt by
<http://search.cpan.org/> to extract the distribution name and version
from filenames and also report if the version is to be treated as a
developer release.

%prep
%setup -q -n CPAN-DistnameInfo-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/CPAN/DistnameInfo/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/CPAN/DistnameInfo.pm
%{_mandir}/man3/CPAN::DistnameInfo.3pm*

%include	/usr/lib/rpm/macros.php
%define		_class		Validate
%define		_subclass	NL
%define		_status		alpha
%define		_pearname	Validate_NL
Summary:	%{_pearname} - Validation class for NL
Summary(pl.UTF-8):	%{_pearname} - Klasa sprawdzająca poprawność dla Holandii
Name:		php-pear-%{_pearname}
Version:	0.5.2
Release:	2
License:	New BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	8fa910866ad96db1bd1cc6ecfca55740
URL:		http://pear.php.net/package/Validate_NL/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.2.0
Requires:	php-pear
Obsoletes:	php-pear-Validate_NL-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Package containes locale validation for NL such as:
- SSN
- Postal Code
- Phone Number
- Bank Account Number (based on 11proef)

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet do sprawdzania poprawności dla Holandii danych takich jak:
- numer ubezpieczenia społecznego (SSN)
- kod pocztowy
- numer telefonu
- numer konta bankowego (na podstawie 11proef)

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Validate/NL.php

%{php_pear_dir}/data/Validate_NL

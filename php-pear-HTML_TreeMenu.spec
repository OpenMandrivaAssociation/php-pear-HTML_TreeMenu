%define		_class		HTML
%define		_subclass	TreeMenu
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

%define		_requires_exceptions pear(../HTML_TreeMenu/TreeMenu.php)\\|pear(../TreeMenu.php)

Summary:	%{_pearname} - provides an api to create a HTML tree
Name:		php-pear-%{_pearname}
Version:	1.2.0
Release:	%mkrel 7
License:	PHP License
Group:		Development/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tar.bz2
URL:		http://pear.php.net/package/HTML_TreeMenu/
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	dos2unix
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
PHP based API creates a tree structure using a couple of small PHP
classes. This can then be converted to javascript using the
printMenu() method. The tree should be dynamic in IE 4 or higher and
NN6/Mozilla, and in IE 5 or higher it maintains state (the
collapsed/expanded status of the branches). Has only been tested under
IE6 however. Other browsers display the tree fully expanded. Each node
can have an optional link and icon. An example of this in action is
available at http://www.phpguru.org/treemenu.php .

In PEAR status of this package is: %{_status}.

%prep

%setup -q -c

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

# strip away annoying ^M
find -type f | grep -v ".gif" | grep -v ".png" | grep -v ".jpg" | xargs dos2unix -U

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/pear/%{_class}/{images,imagesAlt{,2}}

install %{_pearname}-%{version}/*.{php,js} %{buildroot}%{_datadir}/pear/%{_class}/
install %{_pearname}-%{version}/images/* %{buildroot}%{_datadir}/pear/%{_class}/images
install %{_pearname}-%{version}/imagesAlt/* %{buildroot}%{_datadir}/pear/%{_class}/imagesAlt
install %{_pearname}-%{version}/imagesAlt2/* %{buildroot}%{_datadir}/pear/%{_class}/imagesAlt2

install -d %{buildroot}%{_datadir}/pear/packages
install -m0644 package.xml %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

%post
if [ "$1" = "1" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi
if [ "$1" = "2" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi

%preun
if [ "$1" = 0 ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear uninstall --nodeps -r %{_pearname}
	fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/docs/*
%dir %{_datadir}/pear/%{_class}/images
%dir %{_datadir}/pear/%{_class}/imagesAlt
%dir %{_datadir}/pear/%{_class}/imagesAlt2
%{_datadir}/pear/%{_class}/*.php
%{_datadir}/pear/%{_class}/*.js
%{_datadir}/pear/%{_class}/images/*
%{_datadir}/pear/%{_class}/imagesAlt/*
%{_datadir}/pear/%{_class}/imagesAlt2/*

%{_datadir}/pear/packages/%{_pearname}.xml



%define		_class		HTML
%define		_subclass	TreeMenu
%define		upstream_name	%{_class}_%{_subclass}

%define		_requires_exceptions pear(../HTML_TreeMenu/TreeMenu.php)\\|pear(../TreeMenu.php)

Name:		php-pear-%{upstream_name}
Version:	1.2.2
Release:	%mkrel 3
Summary:	Provides an api to create a HTML tree
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/HTML_TreeMenu/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
PHP based API creates a tree structure using a couple of small PHP
classes. This can then be converted to javascript using the
printMenu() method. The tree should be dynamic in IE 4 or higher and
NN6/Mozilla, and in IE 5 or higher it maintains state (the
collapsed/expanded status of the branches). Has only been tested under
IE6 however. Other browsers display the tree fully expanded. Each node
can have an optional link and icon. An example of this in action is
available at http://www.phpguru.org/treemenu.php .

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{upstream_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{upstream_name}
%{_datadir}/pear/packages/%{upstream_name}.xml




%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-3mdv2012.0
+ Revision: 742006
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-2
+ Revision: 679357
- mass rebuild

* Sun Nov 07 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.2-1mdv2011.0
+ Revision: 594489
- update to new version 1.2.2

* Sat Dec 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.1-4mdv2010.1
+ Revision: 477891
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.2.1-3mdv2010.0
+ Revision: 441182
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-2mdv2009.1
+ Revision: 322124
- rebuild

* Tue Sep 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.1-1mdv2009.0
+ Revision: 278922
- update to new version 1.2.1

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-8mdv2009.0
+ Revision: 236883
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 1.2.0-7mdv2008.1
+ Revision: 136407
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-7mdv2007.0
+ Revision: 81719
- Import php-pear-HTML_TreeMenu

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-1mdk
- initial Mandriva package (PLD import)


%define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")

%define name ztc
%define version 12.01.1

%define release 1

Summary: Zabbix Template Collection
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
Source0: https://bitbucket.org/rvs/ztc/downloads/%{name}-%{version}.tar.gz
License: GNU GPL 3
Group: Applications/Internet
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Vladimir Rusinov <vladimir@greenmice.info>
Url: https://bitbucket.org/rvs/ztc/
Requires: zabbix-agent
Requires: smartmontools
%{?el5:Requires: kmod-coretemp}
Requires: lm_sensors
BuildRequires: python-setuptools

%description
ZTC is a collection of templates and UserScripts for zabbix monitoring system.

%prep
%setup -n %{name}-%{version}

%build
python setup.py build

%install
%{__python} setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
%{__python} -c 'import setuptools; execfile("setup.py")' install --skip-build --root %{buildroot}

%clean
rm -rf $RPM_BUILD_ROOT

%post
test -e /etc/init.d/zabbix-agent && /etc/init.d/zabbix-agent status && /etc/init.d/zabbix-agent restart

%files
%defattr(-,root,root)
/opt/ztc/bin/*.py*
/opt/ztc/templates/*.xml
/opt/ztc/lib/*.jar
/opt/ztc/doc/*
/opt/ztc/contrib/*
/etc/zabbix-agent.d/*
%config(noreplace) /etc/ztc/*
/%{python_sitelib}/ztc/*
/%{python_sitelib}/ztc-%{version}-py*.egg-info

%changelog
* Thu Jan 26 2012 Vladimir Rusinov <vladimir@team.wrike.com> 12.01-1
- new version

* Tue Jan 17 2012 Vladimir Rusinov <vladimir@greenmice.info> 11.11.2-1
- version bump (bugfix release)

* Mon Nov 28 2011 Vladimir Rusinov <vladimir@greenmice.info> 11.11.1-1
- version bump (bugfix release)

* Thu Nov 24 2011 Vladimir Rusinov <vladimir@greenmice.info> 11.11-2
- using python_sitelib in files section, hopefully fixing issue #6 in ztc

* Mon Nov 14 2011 Vladimir Rusinov <vladimir@greenmice.info> 11.11-1
- added lm_sensors dependency

* Sat Nov 05 2011 Vladimir Rusinov <vladimir@greenmice.info> 11.11
- version bump

* Sat Nov 05 2011 Vladimir Rusinov <vladimir@greenmice.info> 11.07.3
- version bump

* Thu Oct 06 2011 Vladimir Rusinov <vladimir@greenmice.info> 11.07.2
- version bump

* Thu Sep 22 2011 Vladimir Rusinov <vladimir.rusinov@muranosoft.com> 11.07.1
- version bump

* Tue Jun 23 2011 Vladimir Rusinov <vladimir.rusinov@muransooft.com> 11.06.2
- version bump
- added dependency for kmod-coretemp on el5

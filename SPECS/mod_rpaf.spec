%define debug_package %{nil}

Summary:	Reverse proxy add forward module for Apache
Name:		mod_rpaf
Version:	0.6
Release:	1.vortex%{?dist}
Vendor:		Vortex RPM
License:	ASL 1.0
Group:		System Environment/Daemons
URL:		http://stderr.net/apache/rpaf/
Source0:	http://stderr.net/apache/rpaf/download/%{name}-%{version}.tar.gz
Requires:	httpd
BuildRequires:	httpd-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
rpaf is for backend Apache servers what mod_proxy_add_forward is for
frontend Apache servers. It does excactly the opposite of 
mod_proxy_add_forward written by Ask Bjørn Hansen. It will also work with
mod_proxy in Apache starting with release 1.3.25 and mod_proxy that is
distributed with Apache2 from version 2.0.36.

%prep
%setup -q -n %{name}-%{version}

%build
/usr/sbin/apxs -c -n mod_rpaf-2.0.so mod_rpaf-2.0.c

%install
rm -rf %{buildroot}
install -D -p -m 0755 .libs/mod_rpaf-2.0.so %{buildroot}%{_libdir}/httpd/modules/mod_rpaf-2.0.so
touch rpaf.conf
%ifarch x86_64
echo "LoadModule rpaf_module /usr/lib64/httpd/modules/mod_rpaf-2.0.so" >> rpaf.conf
echo "RPAFenable On" >> rpaf.conf
echo "RPAFproxy_ips 127.0.0.1" >> rpaf.conf
%endif
%ifarch i386
echo "LoadModule rpaf_module /usr/lib/httpd/modules/mod_rpaf-2.0.so" >> rpaf.conf
echo "RPAFenable On" >> rpaf.conf
echo "RPAFproxy_ips 127.0.0.1" >> rpaf.conf
%endif
install -D -p -m 0644 rpaf.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/rpaf.conf

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc CHANGES README
%config(noreplace) %{_sysconfdir}/httpd/conf.d/rpaf.conf
%{_libdir}/httpd/modules/mod_rpaf-2.0.so

%changelog
* Tue Aug 11 2011  Ilya A. Otyutskiy <sharp@thesharp.ru> 0.6-1.vortex
- Initial packaging for CentOS (Closes LP: #824523)


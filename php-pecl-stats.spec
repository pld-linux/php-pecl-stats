%define		_modname	stats
%define		_status		stable
Summary:	%{_modname} - extension with routines for statistical computation
Summary(pl.UTF-8):   %{_modname} - rozszerzenie z funkcjami do wykonywania obliczeń statystycznych
Name:		php-pecl-%{_modname}
Version:	1.0.2
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	96f105be1e76fbc5dca424057066e4d8
URL:		http://pecl.php.net/package/stats/
BuildRequires:	php-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.344
%{?requires_php_extension}
Requires:	php-common >= 4:5.0.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Extension that provides few dozens routines for statistical
computation, such as stats_absolute_deviation(), stats_covariance(),
harmonic_mean() and others.

In PECL status of this extension is: %{_status}.

%description -l pl.UTF-8
To rozszerzenie dostarcza wiele różnych funkcji do wykonywania
obliczeń statystycznych, takich jak stats_absolute_deviation(),
stats_covariance(), harmonic_mean() i inne.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{_modname}.ini
; Enable %{_modname} extension module
extension=%{_modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%doc %{_modname}-%{version}/{CREDITS,TODO}
%doc %{_modname}-%{version}/tests
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{_modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{_modname}.so

%define		php_name	php%{?php_suffix}
%define		modname	stats
%define		status		stable
Summary:	%{modname} - extension with routines for statistical computation
Summary(pl.UTF-8):	%{modname} - rozszerzenie z funkcjami do wykonywania obliczeń statystycznych
Name:		%{php_name}-pecl-%{modname}
Version:	1.0.2
Release:	4
License:	PHP 3.01
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
# Source0-md5:	96f105be1e76fbc5dca424057066e4d8
URL:		http://pecl.php.net/package/stats/
BuildRequires:	%{php_name}-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.650
%{?requires_php_extension}
Requires:	php(core) >= 5.0.4
Provides:	php(%{modname}) = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Extension that provides few dozens routines for statistical
computation, such as stats_absolute_deviation(), stats_covariance(),
harmonic_mean() and others.

In PECL status of this extension is: %{status}.

%description -l pl.UTF-8
To rozszerzenie dostarcza wiele różnych funkcji do wykonywania
obliczeń statystycznych, takich jak stats_absolute_deviation(),
stats_covariance(), harmonic_mean() i inne.

To rozszerzenie ma w PECL status: %{status}.

%prep
%setup -qc
mv %{modname}-%{version}/* .

%build
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}
install -p modules/%{modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{modname}.ini
; Enable %{modname} extension module
extension=%{modname}.so
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
%doc CREDITS TODO
%doc tests
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{modname}.so

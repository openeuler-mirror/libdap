Name:          libdap
Version:       3.19.1
Release:       3
Summary:       The DAP++ SDK
License:       LGPLv2+
URL:           http://www.opendap.org/
Source0:       http://www.opendap.org/pub/source/%{name}-%{version}.tar.gz

Patch0000:     https://raw.githubusercontent.com/funtoo/science-kit/master/sci-libs/libdap/files/libdap-3.19.1-use-libtirpc.patch

BuildRequires: bison >= 3.0 cppunit-devel curl-devel doxygen flex gcc-c++ graphviz libtirpc-devel
BuildRequires: libtool libuuid-devel libxml2-devel openssl-devel pkgconfig valgrind

Provides:      bundled(gnulib)

%description
A C++ SDK which contains an implemention of DAP2.0 and DAP4.0.This includes both Client-side and
Server-side support classes.

%package       devel
Summary:       Development and header files from libdap
Requires:      %{name} = %{version}-%{release} automake curl-devel libxml2-devel pkgconfig

%description   devel
The package provides documents for applications which developed with %{name}.

%package       help
Summary:       Help documents for %{name}
Provides:      %{name}-doc = %{version}-%{release}
Obsoletes:     %{name}-doc < %{version}-%{release}

%description   help
Man pages and other help documents for %{name}.

%prep
%autosetup -n %{name}-%{version} -p1

%build
autoreconf -f -i
%configure --disable-dependency-tracking --disable-static
%make_build
make docs

%install
%make_install INSTALL="%{__install} -p"
mkdir -p $RPM_BUILD_ROOT%{_libdir}/libdap
mv $RPM_BUILD_ROOT%{_libdir}/libtest-types.a $RPM_BUILD_ROOT%{_libdir}/libdap/
mv $RPM_BUILD_ROOT%{_bindir}/dap-config-pkgconfig $RPM_BUILD_ROOT%{_bindir}/dap-config
rm -rf __dist_docs
cp -pr html __dist_docs
rm -f __dist_docs/*.map __dist_docs/*.md5
touch -r ChangeLog __dist_docs/*

%check
make check || :

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYRIGHT_W3C COPYING COPYRIGHT_URI
%{_bindir}/getdap*
%{_libdir}/*.so.*
%exclude %{_libdir}/*.la

%files devel
%{_bindir}/dap-config
%{_libdir}/*.so
%{_libdir}/libdap/
%{_libdir}/pkgconfig/libdap*.pc
%{_includedir}/libdap/
%{_datadir}/aclocal/*

%files help
%doc README README.dodsrc NEWS
%doc __dist_docs/
%{_mandir}/man1/*

%changelog
* Fri Mar 6 2020 zhouyihang<zhouyihang1@huawei.com> - 3.19.1-3
- Pakcage init

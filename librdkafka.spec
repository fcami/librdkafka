Name:		librdkafka
Version:	0.11.4
Release:	1%{?dist}
Summary:	The Apache Kafka C library

Group:		Development/Libraries
License:	BSD
URL:		https://github.com/edenhill/librdkafka
Source0:	https://github.com/edenhill/librdkafka/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	python2
BuildRequires:	openssl-devel
BuildRequires:	cyrus-sasl-devel
BuildRequires:	lz4-devel

%description
Librdkafka is a C/C++ library implementation of the Apache Kafka protocol,
containing both Producer and Consumer support.
It was designed with message delivery reliability and high performance in mind,
current figures exceed 800000 messages/second for the producer and 3 million
messages/second for the consumer.

%package	devel
Summary:	The Apache Kafka C library (Development Environment)
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
librdkafka is a C/C++ library implementation of the Apache Kafka protocol,
containing both Producer and Consumer support.
This package contains headers and libraries required to build applications
using librdkafka.

%prep
%setup -q

%build
%configure	--enable-lz4 \
		--enable-ssl \
		--enable-sasl

%make_build

%check
make check

%install
%make_install
find %{buildroot} -name '*.a' -delete -print
find %{buildroot} -name 'rdkafka*static.pc' -delete -print

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%{_libdir}/librdkafka.so.*
%{_libdir}/librdkafka++.so.*
%doc README.md CONFIGURATION.md INTRODUCTION.md
%license LICENSE LICENSE.pycrc LICENSE.snappy

%files		devel
%dir %{_includedir}/librdkafka
%attr(0644,root,root) %{_includedir}/librdkafka/*
%attr(0755,root,root) %{_libdir}/librdkafka.so
%attr(0755,root,root) %{_libdir}/librdkafka++.so
%{_libdir}/pkgconfig/rdkafka.pc
%{_libdir}/pkgconfig/rdkafka++.pc



%changelog
* Tue Apr 17 2018 François Cami <fcami@fedoraproject.org> - 0.11.4-1
- Update to upstream 0.11.4

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.11.3-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Michal Luscon <mluscon@gmail.com> - 0.11.1-3
- Update to upstream 0.11.3

* Thu Nov 02 2017 Michal Luscon <mluscon@gmail.com> - 0.11.1-1
- Update to upstream 0.11.1

* Thu Aug 31 2017 Michal Luscon <mluscon@gmail.com> - 0.11.0-1
- Update to 0.11.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 22 2017 Radovan Sroka <rsroka@redhat.com> - 0.9.5-1
- Update to 0.9.4

* Sat Mar 11 2017 Michal Luscon <mluscon@gmail.com> - 0.9.4-1
- Update to 0.9.4
- enable lz4, ssl, sasl

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild


* Fri Nov 11 2016 Radovan Sroka <rsroka@redhat.com> 0.9.2-1
- 0.9.2 release
- package created

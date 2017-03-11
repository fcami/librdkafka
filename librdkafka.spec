Name:		librdkafka
Version:	0.9.4
Release:	1%{?dist}
Summary:	The Apache Kafka C library

Group:		Development/Libraries
License:	BSD
URL:		https://github.com/edenhill/librdkafka
Source0:	https://github.com/edenhill/librdkafka/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	python
BuildRequires:  openssl-devel
BuildRequires:  cyrus-sasl-devel
BuildRequires:  lz4-devel

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
%configure --enable-lz4 \
           --enable-ssl \
           --enable-sasl

%make_build

%check
make check

%install
%make_install
find %{buildroot} -name '*.a' -delete -print

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%{_libdir}/librdkafka.so.*
%{_libdir}/librdkafka++.so.*
%doc README.md CONFIGURATION.md INTRODUCTION.md
%license LICENSE LICENSE.pycrc LICENSE.snappy

%files devel
%dir %{_includedir}/librdkafka
%attr(0644,root,root) %{_includedir}/librdkafka/*
%attr(0755,root,root) %{_libdir}/librdkafka.so
%attr(0755,root,root) %{_libdir}/librdkafka++.so
%{_libdir}/pkgconfig/rdkafka.pc
%{_libdir}/pkgconfig/rdkafka++.pc



%changelog
* Sat Mar 11 2017 Michal Luscon <mluscon@gmail.com> - 0.9.4-1
- Update to 0.9.4
- enable lz4, ssl, sasl

* Sat Mar 11 2016 Michal Luscon <mluscon@gmail.com> 0.9.2-1
- epel package import

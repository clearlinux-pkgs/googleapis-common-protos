#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : googleapis-common-protos
Version  : 1.52.0
Release  : 6
URL      : https://files.pythonhosted.org/packages/95/3f/a1282d82def57e0c28bab597d25785774a4e64433aac9cc136e65c500da8/googleapis-common-protos-1.52.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/95/3f/a1282d82def57e0c28bab597d25785774a4e64433aac9cc136e65c500da8/googleapis-common-protos-1.52.0.tar.gz
Summary  : Common protobufs used in Google APIs
Group    : Development/Tools
License  : Apache-2.0
Requires: googleapis-common-protos-python = %{version}-%{release}
Requires: googleapis-common-protos-python3 = %{version}-%{release}
Requires: grpcio
Requires: protobuf
BuildRequires : buildreq-distutils3
BuildRequires : grpcio
BuildRequires : protobuf

%description
# Google APIs common protos

%package python
Summary: python components for the googleapis-common-protos package.
Group: Default
Requires: googleapis-common-protos-python3 = %{version}-%{release}

%description python
python components for the googleapis-common-protos package.


%package python3
Summary: python3 components for the googleapis-common-protos package.
Group: Default
Requires: python3-core
Provides: pypi(googleapis_common_protos)
Requires: pypi(protobuf)

%description python3
python3 components for the googleapis-common-protos package.


%prep
%setup -q -n googleapis-common-protos-1.52.0
cd %{_builddir}/googleapis-common-protos-1.52.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1596513093
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

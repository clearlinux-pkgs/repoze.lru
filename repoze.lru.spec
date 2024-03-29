#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : repoze.lru
Version  : 0.7
Release  : 48
URL      : https://files.pythonhosted.org/packages/12/bc/595a77c4b5e204847fdf19268314ef59c85193a9dc9f83630fc459c0fee5/repoze.lru-0.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/12/bc/595a77c4b5e204847fdf19268314ef59c85193a9dc9f83630fc459c0fee5/repoze.lru-0.7.tar.gz
Summary  : A tiny LRU cache implementation and decorator
Group    : Development/Tools
License  : ZPL-2.1
Requires: repoze.lru-license = %{version}-%{release}
Requires: repoze.lru-python = %{version}-%{release}
Requires: repoze.lru-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description


%package license
Summary: license components for the repoze.lru package.
Group: Default

%description license
license components for the repoze.lru package.


%package python
Summary: python components for the repoze.lru package.
Group: Default
Requires: repoze.lru-python3 = %{version}-%{release}

%description python
python components for the repoze.lru package.


%package python3
Summary: python3 components for the repoze.lru package.
Group: Default
Requires: python3-core
Provides: pypi(repoze.lru)

%description python3
python3 components for the repoze.lru package.


%prep
%setup -q -n repoze.lru-0.7
cd %{_builddir}/repoze.lru-0.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603403335
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/repoze.lru
cp %{_builddir}/repoze.lru-0.7/LICENSE.txt %{buildroot}/usr/share/package-licenses/repoze.lru/1c2024cb6cdcf19ca3e2c81c82936bc7596799c7
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/repoze.lru/1c2024cb6cdcf19ca3e2c81c82936bc7596799c7

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

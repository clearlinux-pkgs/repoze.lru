#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : repoze.lru
Version  : 0.6
Release  : 22
URL      : http://pypi.debian.net/repoze.lru/repoze.lru-0.6.tar.gz
Source0  : http://pypi.debian.net/repoze.lru/repoze.lru-0.6.tar.gz
Summary  : A tiny LRU cache implementation and decorator
Group    : Development/Tools
License  : ZPL-2.1
Requires: repoze.lru-python
Requires: Sphinx
Requires: coverage
Requires: nose
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
==========
        
        ``repoze.lru`` is a LRU (least recently used) cache implementation.  Keys and
        values that are not used frequently will be evicted from the cache faster
        than keys and values that are used frequently.  It works under Python 2.5,
        Python 2.6, Python 2.7, and Python 3.2.
        
        Please see ``docs/index.rst`` for detailed documentation.
        
        
        Changelog
        =========
        
        0.6 (2012-07-12)
        ----------------

%package python
Summary: python components for the repoze.lru package.
Group: Default

%description python
python components for the repoze.lru package.


%prep
%setup -q -n repoze.lru-0.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1503078006
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test
%install
export SOURCE_DATE_EPOCH=1503078006
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*

#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : repoze.lru
Version  : 0.6
Release  : 15
URL      : https://pypi.python.org/packages/source/r/repoze.lru/repoze.lru-0.6.tar.gz
Source0  : https://pypi.python.org/packages/source/r/repoze.lru/repoze.lru-0.6.tar.gz
Summary  : A tiny LRU cache implementation and decorator
Group    : Development/Tools
License  : ZPL-2.1
Requires: repoze.lru-python
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
repoze.lru
==========
``repoze.lru`` is a LRU (least recently used) cache implementation.  Keys and
values that are not used frequently will be evicted from the cache faster
than keys and values that are used frequently.  It works under Python 2.5,
Python 2.6, Python 2.7, and Python 3.2.

%package python
Summary: python components for the repoze.lru package.
Group: Default

%description python
python components for the repoze.lru package.


%prep
%setup -q -n repoze.lru-0.6

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
python2 setup.py test
%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*

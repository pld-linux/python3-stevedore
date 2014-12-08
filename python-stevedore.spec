#
# Conditional build:
%bcond_with	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module

%define 	module	stevedore
Summary:	Manage dynamic plugins for Python applications
Name:		python-%{module}
Version:	1.1.0
Release:	1
License:	Apache v2.0
Group:		Development/Languages
Source0:	http://pypi.python.org/packages/source/s/stevedore/stevedore-%{version}.tar.gz
# Source0-md5:	b7f30055c32410f8f9b6cf1b55bdc68a
URL:		https://github.com/dreamhost/stevedore
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%if %{with python2}
BuildRequires:	python-setuptools
%if %{with tests}
#BuildRequires:  python-discover
BuildRequires:	python-mock
#BuildRequires:  python-oslotest
BuildRequires:	python-pbr
BuildRequires:	python-six
BuildRequires:	python-testrepository
%endif
%endif
%if %{with python3}
BuildRequires:	python3-devel
#BuildRequires:  python3-discover
BuildRequires:	python3-mock
#BuildRequires:  python3-oslotest
BuildRequires:	python3-pbr
BuildRequires:	python3-setuptools
BuildRequires:	python3-six
#BuildRequires:  python3-testrepository
%endif
Requires:	python-setuptools
Requires:	python-six
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Manage dynamic plugins for Python applications

%package -n python3-stevedore
Summary:	Manage dynamic plugins for Python applications
Group:		Development/Libraries
Requires:	python3-setuptools
Requires:	python3-six

%description -n python3-stevedore
Manage dynamic plugins for Python applications

%prep
%setup -q -n stevedore-%{version}

%build
%if %{with python2}
%{__python} setup.py build --build-base build-2

%if %{with tests}
PYTHONPATH=. nosetests-%{py_ver}
%endif
%endif

%if %{with python3}
%{__python3} setup.py build --build-base build-3 %{?with_tests:test}

%if %{with tests}
PYTHONPATH=. nosetests-%{py3_ver}
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%{__python} setup.py \
	build --build-base build-2 \
	install --skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean
%endif

%if %{with python3}
%{__python3} setup.py \
	build --build-base build-3 \
	install --skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst LICENSE
%{py_sitescriptdir}/stevedore
%{py_sitescriptdir}/stevedore-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-stevedore
%defattr(644,root,root,755)
%doc README.rst LICENSE
%{py3_sitescriptdir}/stevedore
%{py3_sitescriptdir}/stevedore-%{version}-py*.egg-info
%endif

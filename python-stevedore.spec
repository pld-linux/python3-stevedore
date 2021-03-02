#
# Conditional build:
%bcond_with	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	stevedore
Summary:	Manage dynamic plugins for Python applications
Name:		python-%{module}
Version:	1.25.0
Release:	4
License:	Apache v2.0
Group:		Development/Languages
Source0:	https://pypi.python.org/packages/08/58/e21f4691e8e75a290bdbfa366f06b9403c653642ef31f879e07f6f9ad7db/stevedore-1.25.0.tar.gz
# Source0-md5:	8de5610a69f8066191d3e4b9af82c437
URL:		https://pypi.python.org/pypi/stevedore
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%if %{with python2}
BuildRequires:	python-setuptools
BuildRequires:	python-pbr >= 2.0.0
%if %{with tests}
BuildRequires:	python-six >= 1.9.0
BuildRequires:  python-pillow >= 2.4.0
BuildRequires:	sphinx-pdg-2 >= 1.6.2
BuildRequires:	python-mock >= 2.0
BuildRequires:  python-coverage >=4.0
BuildRequires:  python-testrepository >= 0.0.18
BuildRequires:	python-openstackdocstheme >=1.11.0
BuildRequires:	python-reno >=1.8.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-setuptools
BuildRequires:	python3-pbr >= 2.0.0
%if %{with tests}
BuildRequires:	python3-six >= 1.9.0
BuildRequires:  python3-pillow >= 2.4.0
BuildRequires:	sphinx-pdg-3 >= 1.6.2
BuildRequires:	python3-mock >= 2.0
BuildRequires:  python3-coverage >=4.0
BuildRequires:  python3-testrepository >= 0.0.18
BuildRequires:	python3-openstackdocstheme >=1.11.0
BuildRequires:	python3-reno >=1.8.0
%endif
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
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/stevedore/tests
%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/stevedore/example

%py_postclean
%endif

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/stevedore/tests
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/stevedore/example
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

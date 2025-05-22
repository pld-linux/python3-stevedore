#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests

%define 	module	stevedore
Summary:	Manage dynamic plugins for Python applications
Summary(pl.UTF-8):	Zarządzanie dynamicznymi wtyczkami dla aplikacji Pythona
Name:		python3-%{module}
Version:	5.4.1
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/stevedore/
Source0:	https://files.pythonhosted.org/packages/source/s/stevedore/stevedore-%{version}.tar.gz
# Source0-md5:	d8ce49d9a513d454bec0e897ce10062b
URL:		https://pypi.org/project/stevedore/
BuildRequires:	python3-pbr >= 2.0.0
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with tests}
BuildRequires:	python3-coverage >= 4.0
#BuildRequires:	python3-mock >= 2.0.0
BuildRequires:	python3-six >= 1.10.0
BuildRequires:	python3-stestr >= 2.0.0
BuildRequires:	sphinx-pdg-3 >= 1.7.0
%endif
%if %{with doc}
BuildRequires:	python3-openstackdocstheme >= 1.11.0
BuildRequires:	python3-reno >= 2.5.0
BuildRequires:	sphinx-pdg-3 >= 1.7.0
%endif
Requires:	python3-modules >= 1:3.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Manage dynamic plugins for Python applications.

%description -l pl.UTF-8
Zarządzanie dynamicznymi wtyczkami dla aplikacji Pythona.

%package apidocs
Summary:	API documentation for Python stevedore module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona stevedore
Group:		Documentation

%description apidocs
API documentation for Python stevedore module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona stevedore.

%prep
%setup -q -n stevedore-%{version}

%build
%py3_build %{?with_tests:test}

%if %{with doc}
PYTHONPATH=$(pwd) \
sphinx-build-3 -b html doc/source doc/source/_build/html
%endif

%install

rm -rf $RPM_BUILD_ROOT

%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/stevedore/tests
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/stevedore/example

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CONTRIBUTING.rst ChangeLog README.rst
%{py3_sitescriptdir}/stevedore
%{py3_sitescriptdir}/stevedore-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/source/_build/html/{_images,_static,install,reference,user,*.html,*.js}
%endif

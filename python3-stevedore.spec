#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests

%define 	module	stevedore
Summary:	Manage dynamic plugins for Python applications
Summary(pl.UTF-8):	Zarządzanie dynamicznymi wtyczkami dla aplikacji Pythona
Name:		python3-%{module}
Version:	5.9.1
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/stevedore/
Source0:	https://files.pythonhosted.org/packages/source/s/stevedore/stevedore-%{version}.tar.gz
# Source0-md5:	72a197823cb696dce7dd577529deecc6
URL:		https://pypi.org/project/stevedore/
BuildRequires:	python3-pbr >= 6.1.1
BuildRequires:	python3-modules >= 1:3.11
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-Sphinx >= 2.0.0
BuildRequires:	python3-coverage >= 4.0
BuildRequires:	python3-stestr >= 2.0.0
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-openstackdocstheme >= 2.2.1
# actually not used
#BuildRequires:	python3-reno >= 3.1.0
BuildRequires:	sphinx-pdg-3 >= 2.0.0
%endif
Requires:	python3-modules >= 1:3.11
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
%py3_build

%if %{with tests}
stestr run stevedore/tests
%endif

%if %{with doc}
PYTHONPATH=$(pwd) \
sphinx-build-3 -b html doc/source doc/source/_build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/stevedore/tests
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/stevedore/example
# imports the removed stevedore.example
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/stevedore/example2

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

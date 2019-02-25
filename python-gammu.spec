%bcond_without python2

Summary:	Python bindings for the Gammu library
Name:		python-gammu
Version:	2.12
Release:	2
Group:		Communications
License:	GPLv2+
URL:		https://www.gammu.org/%{name}
Source0:	https://dl.cihar.com/%{name}/%{name}-%{version}.tar.bz2

BuildRequires:	pkgconfig(gammu)
BuildRequires:	pkgconfig(python)
BuildRequires:	python3egg(setuptools)
%if %with python2
BuildRequires:	pkgconfig(python2)
BuildRequires:	pythonegg(setuptools)
%endif
#for tests: Solve DBI failed to initialize!
#BuildRequires:  libdbi-dbd-sqlite

%description
Python bindings for the Gammu library.

%files
%{python3_sitearch}/gammu
%{python3_sitearch}/python_gammu-*.egg-info
%doc AUTHORS COPYING NEWS.rst README.rst

#--------------------------------------------------------------
%if %with python2
%package -n python2-gammu
Summary:	%{summary}

%description -n python2-gammu
Python2 bindings for the Gammu library.

%files -n python2-gammu
%{python2_sitearch}/gammu
%{python2_sitearch}/python_gammu-*.egg-info
%doc AUTHORS COPYING NEWS.rst README.rst
%endif
#--------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
%py3_build
%if %with python2
%py2_build
%endif

%install
%py3_install
%if %with python2
%py2_install
%endif

%check
%{__python3} setup.py test || :
%if %with python2
%{__python2} setup.py test || :
%endif


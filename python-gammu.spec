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

%build
CFLAGS="$RPM_OPT_FLAGS" SKIPWXCHECK=yes %{__python3} setup.py build
%if %with python2
CFLAGS="$RPM_OPT_FLAGS" SKIPWXCHECK=yes %{__python2} setup.py build
%endif

%install
SKIPWXCHECK=yes %{__python3} setup.py install --root=$RPM_BUILD_ROOT
%if %with python2
SKIPWXCHECK=yes %{__python2} setup.py install --root=$RPM_BUILD_ROOT
%endif

%check
%{__python3} setup.py test || :
%if %with python2
%{__python2} setup.py test || :
%endif


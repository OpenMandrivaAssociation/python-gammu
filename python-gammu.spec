%global	module	gammu
%define mod %(m=%{name}; echo ${m:0:1})

%bcond_without	test

Summary:	Python bindings for the Gammu library
Name:		python-%{module}
Version:	3.2.4
Release:	1
Group:		Communications
License:	GPLv2+
URL:		https://www.gammu.org/%{name}
#Source0:	https://dl.cihar.com/%{name}/%{name}-%{version}.tar.gz
Source0:	https://pypi.io/packages/source/%mod/%{name}/%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(gammu)
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(setuptools)
%{?with_test:
BuildRequires:	libdbi-drivers-dbd-sqlite3
}

#Requires:	libdbi-drivers-dbd-sqlite3

%description
Python bindings for the Gammu library.

%files
%license COPYING
%doc AUTHORS NEWS.rst README.rst
%{py_platsitedir}/%{module}
%{py_platsitedir}/python_%{module}-%{version}-py%{py_ver}.egg-info

#--------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%py3_build

%install
%py3_install

%{?with_test:
%check
%{__python3} setup.py test || :
}


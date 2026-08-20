%define major %(echo %{version} |cut -d. -f1-2)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

%define libname %mklibname KF6Mime
%define devname %mklibname KF6Mime -d

Name:		kf6-kmime
Version:	6.29.0
Release:	1
Source0:	https://download.kde.org/%{stable}/frameworks/%{major}/kmime-%{version}.tar.xz
Summary:	Library for handling MIME data
URL:		https://invent.kde.org/frameworks/kmime
License:	LGPLv2+
Group:		System/Libraries
BuildRequires:	cmake
BuildRequires:	cmake(ECM)
BuildRequires:	python
BuildRequires:	gettext
BuildRequires:	doxygen
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6ToolsTools)
BuildRequires:	cmake(KF6Codecs)
Requires:	%{libname} = %{EVRD}
# Moved from Gear into Frameworks 6.27+
%rename		kmime
BuildSystem:	cmake
BuildOption:	-DBUILD_QCH:BOOL=ON
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
KMime is a library for handling mail messages and other MIME data.

%package -n %{libname}
Summary:	Library for handling MIME data
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libname}
KMime is a library for handling mail messages and other MIME data.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files (headers, CMake config) for %{name}.

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/kmime.*

%files -n %{libname}
%{_libdir}/libKF6Mime.so.*

%files -n %{devname}
%{_includedir}/KF6/KMime
%{_libdir}/cmake/KF6Mime
%{_libdir}/libKF6Mime.so

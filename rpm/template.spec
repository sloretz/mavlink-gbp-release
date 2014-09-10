Name:           ros-hydro-mavlink
Version:        2014.09.10
Release:        0%{?dist}
Summary:        ROS mavlink package

Group:          Development/Libraries
License:        LGPLv3
URL:            http://qgroundcontrol.org/mavlink/
Source0:        %{name}-%{version}.tar.gz

Requires:       python-devel
Requires:       ros-hydro-catkin
BuildRequires:  cmake
BuildRequires:  python-devel

%description
MAVLink message marshaling library. This package provides C-headers and
pymavlink library.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Wed Sep 10 2014 Vladimir Ermakov <vooon341@gmail.com> - 2014.09.10-0
- Autogenerated by Bloom

* Sat Aug 09 2014 Vladimir Ermakov <vooon341@gmail.com> - 1.0.9-7
- Autogenerated by Bloom

* Mon Aug 25 2014 Vladimir Ermakov <vooon341@gmail.com> - 1.0.9-8
- Autogenerated by Bloom

* Fri Aug 08 2014 Vladimir Ermakov <vooon341@gmail.com> - 1.0.9-6
- Autogenerated by Bloom


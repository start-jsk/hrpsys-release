Name:           ros-jade-hrpsys
Version:        315.9.0
Release:        0%{?dist}
Summary:        ROS hrpsys package

Group:          Development/Libraries
License:        EPL
URL:            http://ros.org/wiki/hrpsys
Source0:        %{name}-%{version}.tar.gz

Requires:       SDL-devel
Requires:       blt
Requires:       freeglut-devel
Requires:       irrlicht-devel
Requires:       libXmu-devel
Requires:       libxml2-devel
Requires:       qhull-devel
Requires:       ros-jade-cv-bridge
Requires:       ros-jade-openhrp3
Requires:       tcl
Requires:       tix
Requires:       tk
BuildRequires:  SDL-devel
BuildRequires:  blt
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  freeglut-devel
BuildRequires:  git
BuildRequires:  glew-devel
BuildRequires:  graphviz
BuildRequires:  irrlicht-devel
BuildRequires:  libXmu-devel
BuildRequires:  libxml2-devel
BuildRequires:  pkgconfig
BuildRequires:  qhull-devel
BuildRequires:  ros-jade-cv-bridge
BuildRequires:  ros-jade-mk
BuildRequires:  ros-jade-openhrp3
BuildRequires:  tcl
BuildRequires:  tix
BuildRequires:  tk

%description
An OpenRTM-aist-based robot controller. This package is the most tailored for
humanoid (dual-arm and/or biped) robots for historical reason. hrpsys package
does not only wraps but build and installs the code from its mainstream
repository (github.com/fkanehiro/hrpsys-base). The package version number is
synchronized to that of mainstream, based on this decision. Its semantics:
MAJOR: Synchronized with OpenHRP3 MINOR: Indicate IDL compatibility (packages
with different version numbers in this section are NOT compatible) PATCH:
Packages with different version numbers in this section ARE compatible. API
document is auto-generated on github.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Wed Apr 20 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 315.9.0-0
- Autogenerated by Bloom

* Mon Apr 18 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 315.8.0-0
- Autogenerated by Bloom


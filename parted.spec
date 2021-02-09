#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x117E8C168EFE3A7F (bcl@redhat.com)
#
Name     : parted
Version  : 3.4
Release  : 38
URL      : https://mirrors.kernel.org/gnu/parted/parted-3.4.tar.xz
Source0  : https://mirrors.kernel.org/gnu/parted/parted-3.4.tar.xz
Source1  : https://mirrors.kernel.org/gnu/parted/parted-3.4.tar.xz.sig
Summary  : The GNU disk partition manipulation program
Group    : Development/Tools
License  : GPL-3.0
Requires: parted-bin = %{version}-%{release}
Requires: parted-info = %{version}-%{release}
Requires: parted-lib = %{version}-%{release}
Requires: parted-license = %{version}-%{release}
Requires: parted-locales = %{version}-%{release}
Requires: parted-man = %{version}-%{release}
BuildRequires : LVM2-dev
BuildRequires : glibc-locale
BuildRequires : ncurses-dev
BuildRequires : perl
BuildRequires : perl(Digest::CRC)
BuildRequires : pkgconfig(check)
BuildRequires : readline-dev
Patch1: 0001-Make-partition-table-sync-warning-instead-of-error.patch
Patch2: 0002-Fix-build.patch
Patch3: 0003-Add-missing-dep-for-libparted-fs-resize.pc.patch

%description
The GNU Parted program allows you to create, destroy, resize, move,
and copy hard disk partitions. Parted can be used for creating space
for new operating systems, reorganizing disk usage, and copying data
to new hard disks.

%package bin
Summary: bin components for the parted package.
Group: Binaries
Requires: parted-license = %{version}-%{release}

%description bin
bin components for the parted package.


%package dev
Summary: dev components for the parted package.
Group: Development
Requires: parted-lib = %{version}-%{release}
Requires: parted-bin = %{version}-%{release}
Provides: parted-devel = %{version}-%{release}
Requires: parted = %{version}-%{release}

%description dev
dev components for the parted package.


%package info
Summary: info components for the parted package.
Group: Default

%description info
info components for the parted package.


%package lib
Summary: lib components for the parted package.
Group: Libraries
Requires: parted-license = %{version}-%{release}

%description lib
lib components for the parted package.


%package license
Summary: license components for the parted package.
Group: Default

%description license
license components for the parted package.


%package locales
Summary: locales components for the parted package.
Group: Default

%description locales
locales components for the parted package.


%package man
Summary: man components for the parted package.
Group: Default

%description man
man components for the parted package.


%prep
%setup -q -n parted-3.4
cd %{_builddir}/parted-3.4
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1612891092
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
%configure --disable-static --enable-nls \
--enable-shared
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1612891092
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/parted
cp %{_builddir}/parted-3.4/COPYING %{buildroot}/usr/share/package-licenses/parted/e31db874e5b375f0592b02e3e450c9e94086e661
%make_install
%find_lang parted

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/parted
/usr/bin/partprobe

%files dev
%defattr(-,root,root,-)
/usr/include/parted/constraint.h
/usr/include/parted/debug.h
/usr/include/parted/device.h
/usr/include/parted/disk.h
/usr/include/parted/exception.h
/usr/include/parted/filesys.h
/usr/include/parted/geom.h
/usr/include/parted/natmath.h
/usr/include/parted/parted.h
/usr/include/parted/timer.h
/usr/include/parted/unit.h
/usr/lib64/libparted-fs-resize.so
/usr/lib64/libparted.so
/usr/lib64/pkgconfig/libparted-fs-resize.pc
/usr/lib64/pkgconfig/libparted.pc

%files info
%defattr(0644,root,root,0755)
/usr/share/info/parted.info

%files lib
%defattr(-,root,root,-)
/usr/lib64/libparted-fs-resize.so.0
/usr/lib64/libparted-fs-resize.so.0.0.3
/usr/lib64/libparted.so.2
/usr/lib64/libparted.so.2.0.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/parted/e31db874e5b375f0592b02e3e450c9e94086e661

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/parted.8
/usr/share/man/man8/partprobe.8

%files locales -f parted.lang
%defattr(-,root,root,-)


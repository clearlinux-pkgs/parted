#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : parted
Version  : 3.2
Release  : 21
URL      : http://ftp.gnu.org/gnu/parted/parted-3.2.tar.xz
Source0  : http://ftp.gnu.org/gnu/parted/parted-3.2.tar.xz
Summary  : The GNU disk partition manipulation program
Group    : Development/Tools
License  : GFDL-1.3 GPL-3.0
Requires: parted-bin
Requires: parted-lib
Requires: parted-doc
Requires: parted-locales
BuildRequires : LVM2-dev
BuildRequires : ncurses-dev
BuildRequires : perl
BuildRequires : pkgconfig(check)
BuildRequires : readline-dev
Patch1: 0001-Use-en_US.UTF-8-available-UTF-8-locale.patch
Patch2: 0002-Make-partition-table-sync-warning-instead-of-error.patch

%description
The GNU Parted program allows you to create, destroy, resize, move,
and copy hard disk partitions. Parted can be used for creating space
for new operating systems, reorganizing disk usage, and copying data
to new hard disks.

%package bin
Summary: bin components for the parted package.
Group: Binaries

%description bin
bin components for the parted package.


%package dev
Summary: dev components for the parted package.
Group: Development
Requires: parted-lib
Requires: parted-bin
Provides: parted-devel

%description dev
dev components for the parted package.


%package doc
Summary: doc components for the parted package.
Group: Documentation

%description doc
doc components for the parted package.


%package lib
Summary: lib components for the parted package.
Group: Libraries

%description lib
lib components for the parted package.


%package locales
Summary: locales components for the parted package.
Group: Default

%description locales
locales components for the parted package.


%prep
%setup -q -n parted-3.2
%patch1 -p1
%patch2 -p1

%build
%configure --disable-static --enable-nls \
--enable-shared
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
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
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*
%doc /usr/share/man/man8/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*

%files locales -f parted.lang 
%defattr(-,root,root,-)


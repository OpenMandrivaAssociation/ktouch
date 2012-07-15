Name: ktouch
Summary: A program for learning touch typing
Version: 4.8.97
Release: 1
Group: Graphical desktop/KDE
License: GPLv2 GFDL
URL: http://edu.kde.org/ktouch
Source: ftp://ftp.kde.org/pub/kde/unstable/%version/src/%name-%version.tar.xz
BuildRequires: kdelibs4-devel >= 2:%{version}

%description
KTouch is a program for learning touch typing. KTouch is a way to learn
to type on a keyboard quickly and correctly. Every finger has its place
on the keyboard with associated keys to press.

KTouch helps you learn to touch typing by providing you with something
to write. KTouch can also help you to remember what fingers to use.

%files
%doc COPYING COPYING.DOC ChangeLog AUTHORS
%_kde_appsdir/ktouch
%_kde_bindir/ktouch
%_kde_iconsdir/*/*/apps/ktouch.*
%_kde_datadir/applications/kde4/ktouch.desktop
%_kde_datadir/config.kcfg/ktouch.kcfg
%_kde_docdir/HTML/*/ktouch
%_kde_mandir/man1/ktouch.1.*

#----------------------------------------------------------------------

%prep
%setup -q
%apply_patches


%build
%cmake_kde4 
%make

%install
%makeinstall_std -C build


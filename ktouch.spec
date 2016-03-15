Summary:	A program for learning touch typing
Name:		ktouch
Version:	15.12.3
Release:	1
License:	GPLv2+ and GFDL
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/ktouch
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs-devel
BuildRequires:	pkgconfig(xkbfile)
Requires:	kqtquickcharts

%description
KTouch is a program for learning touch typing. KTouch is a way to learn
to type on a keyboard quickly and correctly. Every finger has its place
on the keyboard with associated keys to press.

KTouch helps you learn to touch typing by providing you with something
to write. KTouch can also help you to remember what fingers to use.

%files
%doc COPYING COPYING.DOC AUTHORS
%doc %{_docdir}/HTML/*/ktouch
%{_datadir}/applications/kde4/ktouch.desktop
%{_datadir}/apps/ktouch
%{_bindir}/ktouch
%{_datadir}/appdata/ktouch.appdata.xml
%{_datadir}/config.kcfg/ktouch.kcfg
%{_iconsdir}/*/*/apps/ktouch.*
%{_mandir}/man1/ktouch.1.*

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 \
	-DCMAKE_MINIMUM_REQUIRED_VERSION=3.1
%make

%install
%makeinstall_std -C build


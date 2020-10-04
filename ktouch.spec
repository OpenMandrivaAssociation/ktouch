%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Summary:	A program for learning touch typing
Name:		ktouch
Version:	20.08.1
Release:	2
License:	GPLv2+ and GFDL
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/ktouch
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(xkbfile)
BuildRequires:	pkgconfig(xcb-xkb)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5QuickWidgets)
BuildRequires:	cmake(Qt5Script)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5X11Extras)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5XmlPatterns)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5ItemViews)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5TextWidgets)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5XmlGui)

%description
KTouch is a program for learning touch typing. KTouch is a way to learn
to type on a keyboard quickly and correctly. Every finger has its place
on the keyboard with associated keys to press.

KTouch helps you learn to touch typing by providing you with something
to write. KTouch can also help you to remember what fingers to use.

%files -f %{name}.lang
%{_datadir}/applications/org.kde.ktouch.desktop
%{_datadir}/ktouch
%{_bindir}/ktouch
%{_datadir}/metainfo/*.xml
%{_datadir}/config.kcfg/ktouch.kcfg
%{_iconsdir}/*/*/apps/ktouch.*
%{_mandir}/man1/ktouch.1.*

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build
%find_lang %{name} --with-html --with-man

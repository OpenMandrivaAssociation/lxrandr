%define git 0

Summary:	Simple monitor config tool for LXDE
Name:     	lxrandr
Version:	0.3.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		http://lxde.sourceforge.net/
Source0: 	http://sourceforge.net/lxde/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	pkgconfig(gtk+-x11-2.0)
Requires:	xrandr

%description
This is a very basic monitor config tool utilizing XRandR. It can let you
change the screen resolution on the fly. Besides, when you run lxrandr
with external monitor connected, its GUI will change, and show you some 
quick options to get your projector working correctly.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_mandir}/man1/*.1*


# git snapshot
%global snapshot 1
%if 0%{?snapshot}
	%global commit		a78873f6727a826423eab55be1e4edb69f660cdf
	%global commitdate	20230917
	%global shortcommit	%(c=%{commit}; echo ${c:0:7})
%endif

Summary:	Simple monitor config tool for LXDE
Name:     	lxrandr
Version:	0.3.2
Release:	3
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		https://lxde.sourceforge.net/
#Source0: 	http://sourceforge.net/lxde/%{name}-%{version}.tar.xz
Source0:	https://github.com/lxde/lxrandr/archive/%{?snapshot:%{commit}}%{!?snapshot:%{version}}/%{name}-%{?snapshot:%{commit}}%{!?snapshot:%{version}}.tar.gz

BuildRequires:	intltool
BuildRequires:	pkgconfig(gtk+-3.0)
Requires:	xrandr

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_mandir}/man1/*.1*

#---------------------------------------------------------------------------

%description
This is a very basic monitor config tool utilizing XRandR. It can let you
change the screen resolution on the fly. Besides, when you run lxrandr
with external monitor connected, its GUI will change, and show you some 
quick options to get your projector working correctly.

%prep
%autosetup -p1 -n %{name}-%{?snapshot:%{commit}}%{!?snapshot:%{version}}

%build
sh ./autogen.sh
%configure \
	--enable-gtk3
%make_build

%install
%make_install

# locales
%find_lang %{name}


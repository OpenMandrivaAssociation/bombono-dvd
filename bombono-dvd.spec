Name:		bombono-dvd
Version:	0.5.2
Release:	%mkrel 1
Summary:	DVD authoring program with nice and clean GUI
License:	GPLv2
Group:		Video
URL:		http://www.bombono.org
Source0:	http://prdownloads.sourceforge.net/bombono/%{name}-%{version}.tar.bz2
Patch0:		bombono-dvd-0.5.2-twolame-instead-of-toolame.patch
BuildRequires:	scons 
BuildRequires:	libdvdread-devel 
BuildRequires:	libgtkmm2.4-devel 
BuildRequires:	libxml++2.6-devel 
BuildRequires:	libmjpegtools1.9_0-devel 
BuildRequires:	libgraphicsmagick-devel
Requires:	dvdauthor mjpegtools dvd+rw-tools twolame
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
 Bombono DVD is easy to use program for making DVD-Video.
 The main features of Bombono DVD are:
  * excellent MPEG viewer: Timeline and Monitor
  * real WYSIWYG Menu Editor with live thumbnails
  * comfortable Drag-N-Drop support
  * you can author to folder, make ISO-image or burn directly to DVD
  * reauthoring: you can import video from DVD discs.

%prep
%setup -q	
%patch0 -p1

%build
scons  CFLAGS='-Wno-extra' PREFIX=%{_prefix} DESTDIR=%{buildroot}

%install
rm -rf %{buildroot}

scons install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/bombono
%{_datadir}/applications/bombono-dvd.desktop
%{_datadir}/pixmaps/bombono-dvd.png

Name:		bombono-dvd
Version:	0.6.0
Release:	%mkrel 1
Summary:	DVD authoring program with nice and clean GUI
License:	GPLv2
Group:		Video
URL:		http://www.bombono.org
Source0:	http://prdownloads.sourceforge.net/bombono/%{name}-%{version}.tar.bz2
BuildRequires:	scons 
BuildRequires:	libdvdread-devel 
BuildRequires:	gtkmm2.4-devel
BuildRequires:	libxml++2.6-devel
BuildRequires:	libmjpegtools-devel 
BuildRequires:	graphicsmagick-devel
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

%build
scons  CFLAGS='-Wno-extra' PREFIX=%{_prefix} DESTDIR=%{buildroot}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/applications
scons install
%find_lang %name

cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Bombono DVD
Comment=Easy to use DVD authoring tool
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Video;
EOF

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/bombono
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop 

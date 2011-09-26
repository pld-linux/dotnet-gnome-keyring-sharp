#
%include	/usr/lib/rpm/macros.mono
#
Summary:	A fully managed implementation of libgnome-keyring
Summary(pl.UTF-8):	W pełni zarządzana implementacja libgnome-keyring
Name:		dotnet-gnome-keyring-sharp
Version:	1.0.2
Release:	1
License:	X11/MIT
Group:		Libraries
Source0:	http://www.go-mono.com/archive/gnome-keyring-sharp/gnome-keyring-sharp-%{version}.tar.gz
# Source0-md5:	f9a48319f3fe6123017b000d714d68b1
#URL:		http://gtk-sharp.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-gtk-sharp2-devel
BuildRequires:	libtool
BuildRequires:	mono-csharp >= 1.1.16.1
BuildRequires:	monodoc >= 2.6
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(monoautodeps)
Requires:	mono >= 1.1.16.1
ExclusiveArch:	%{ix86} %{x8664} arm hppa ia64 ppc s390 s390x sparc sparcv9 sparc64
ExcludeArch:	i386
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a fully managed implementation of
libgnome-keyring.

%description -l pl.UTF-8
Pakiet ten dostarcza w pełni zarządzaną implementację biblioteki
libgnome-keyring.

%package devel
Summary:	Development part of gnome-keyring-sharp
Summary(pl.UTF-8):	Część gnome-keyring-sharp dla programistów
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	monodoc >= 2.6
Requires:	which
Obsoletes:	dotnet-gtk-sharp2-gnome-devel
Obsoletes:	gtk-sharp2-devel

%description devel
Developement files and documentation for developing applications using
gnome-keyring-sharp.

%description devel -l pl.UTF-8
Pliki programistyczne i dokumentacja dla gnome-keyring-sharp.

%prep
%setup -q -n gnome-keyring-sharp-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	docsdir=%{_prefix}/lib/monodoc/sources

ln -s %{_pkgconfigdir}/gnome-keyring-sharp-1.0.pc $RPM_BUILD_ROOT%{_pkgconfigdir}/gnome-keyring-sharp.pc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%{_prefix}/lib/mono/gac/*
%{_libdir}/libgnome-keyring-sharp-glue.so
%exclude %{_prefix}/lib/mono/gac/Gnome.Keyring/*/*.mdb

%files devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gac/Gnome.Keyring/*/*.mdb
%{_prefix}/lib/mono/gnome-keyring-sharp-1.0
%{_pkgconfigdir}/*.pc
%{_prefix}/lib/monodoc/sources/Gnome.Keyring.*

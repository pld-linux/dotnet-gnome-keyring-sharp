#
#
%include	/usr/lib/rpm/macros.mono
#
Summary:	A fully managed implementation of libgnome-keyring
Summary(pl.UTF-8):	W pełni zarządzana implementacja libgnome-keyring
Name:		dotnet-gnome-keyring-sharp
Version:	96902
Release:	1
License:	LGPL
Group:		Libraries
Source0:	gnome-keyring-sharp-r%{version}.tar.bz2
# Source0-md5:	99d688281bf6cefbb343107bab646e18
#URL:		http://gtk-sharp.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-ndesk-dbus-sharp-devel >= 0.6.0
BuildRequires:	mono-csharp >= 1.1.16.1
BuildRequires:	monodoc >= 1.1.16
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
Requires:	monodoc
Requires:	which
Obsoletes:	dotnet-gtk-sharp2-gnome-devel
Obsoletes:	gtk-sharp2-devel

%description devel
Developement files and documentation for developing applications using
gnome-keyring-sharp.

%description devel -l pl.UTF-8
Pliki programistyczne i dokumentacja dla gnome-keyring-sharp.

%prep
%setup -q -n gnome-keyring-sharp

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
	monodocdir=%{_libdir}/monodoc/sources


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%{_prefix}/lib/mono/gac/*
%exclude %{_prefix}/lib/mono/gac/Gnome.Keyring/*/*.mdb

%files devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gac/Gnome.Keyring/*/*.mdb
%{_prefix}/lib/mono/gnome-keyring-sharp-1.0
%{_pkgconfigdir}/*.pc
%{_libdir}/monodoc/sources/Gnome.Keyring.*

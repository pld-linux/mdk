# TODO: separate gmixvm
Summary:	GNU MIX Development Kit
Summary(pl):	GNU MIX Development Kit - zestaw programistyczny dla j�zyka MIXAL
Name:		mdk
Version:	1.2.3
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://ftp.gnu.org/gnu/mdk/v1.2.3/%{name}-%{version}.tar.gz
# Source0-md5:	1c74ec62c847792706be412289c8152b
URL:		http://www.gnu.org/software/mdk/mdk.html
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	guile-devel
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
# for GUI
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	pango-devel >= 1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MDK stands for MIX Development Kit, and provides tools for developing
and executing, in a MIX virtual machine, MIXAL programs.

The MIX is Donald Knuth's mythical computer, described in the first
volume of The Art of Computer Programming, which is programmed using
MIXAL, the MIX assembly language.

MDK includes a MIXAL assembler (mixasm) and a MIX virtual machine
(mixvm) with a command line interface. In addition, a GTK+ GUI to
mixvm, called gmixvm, is provided; and, for Emacs guy, exists emacs
mode, which allows running mixvm inside an Emacs GUD buffer.

%description -l pl
MDK oznacza MIX Development Kit (zestaw programistyczny MIX) i
dostarcza narz�dzia do tworzenia i wykonywania program�w w j�zyku
MIXAL na wirtualnej maszynie MIX.

MIX to mityczny komputer Donalda Knutha opisany w pierwszej cz�ci
"The Art of Computer Programming", kt�r� programuje si� w j�zyku
asemblera MIXAL (MIX assembly language).

MDK zawiera asembler MIXAL (mixasm) oraz maszyn� wirtualn� MIX (mixvm)
z interfejsem linii polece�. Ponadto dostarczony jest graficzny
interfejs GTK+ do mixvm o nazwie gmixvm; a dla emacsowc�w istnieje
tryb Emacsa pozwalaj�cy na uruchomienie mixvm wewn�trz bufora GUD
Emacsa.

%prep
%setup -q

%build
%configure
%{__make}
ln -s doc/img
%{__make} -C doc html

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}
rm img/Makefile*

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc doc/mdk.html doc/img AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_infodir}/*.info*

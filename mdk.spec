# TODO: separate gmixvm
Summary:	GNU MIX Development Kit
Summary(pl.UTF-8):	GNU MIX Development Kit - zestaw programistyczny dla języka MIXAL
Name:		mdk
Version:	1.2.4
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://ftp.gnu.org/gnu/mdk/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	a1dd320fa5f8a791db7e66155200ee55
Patch0:		%{name}-pmake.patch
URL:		http://www.gnu.org/software/mdk/mdk.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools >= 0.14
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	guile-devel
BuildRequires:	intltool >= 0.30
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
# for GUI
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	libglade2-devel >= 1:2.0.0
BuildRequires:	pango-devel >= 1:1.4
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

%description -l pl.UTF-8
MDK oznacza MIX Development Kit (zestaw programistyczny MIX) i
dostarcza narzędzia do tworzenia i wykonywania programów w języku
MIXAL na wirtualnej maszynie MIX.

MIX to mityczny komputer Donalda Knutha opisany w pierwszej części
"The Art of Computer Programming", którą programuje się w języku
asemblera MIXAL (MIX assembly language).

MDK zawiera asembler MIXAL (mixasm) oraz maszynę wirtualną MIX (mixvm)
z interfejsem linii poleceń. Ponadto dostarczony jest graficzny
interfejs GTK+ do mixvm o nazwie gmixvm; a dla emacsowców istnieje
tryb Emacsa pozwalający na uruchomienie mixvm wewnątrz bufora GUD
Emacsa.

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
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

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc doc/mdk.html doc/img AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/gmixvm
%attr(755,root,root) %{_bindir}/mixasm
%attr(755,root,root) %{_bindir}/mixguile
%attr(755,root,root) %{_bindir}/mixvm
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/mixal-mode.el
%{_datadir}/%{name}/mixvm.el
%{_datadir}/%{name}/mixguile*.scm
%{_datadir}/%{name}/mixgtk.glade
%{_infodir}/mdk.info*

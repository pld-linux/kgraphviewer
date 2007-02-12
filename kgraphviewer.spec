Summary:	GraphViz dot graph viewer for KDE
Summary(pl.UTF-8):   Przeglądarka grafów dot GraphViza dla KDE
Name:		kgraphviewer
Version:	1.0.2
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://svn.gna.org/daily/%{name}-snapshot.tar.gz
# Source0-md5:	d880eb8fe04523b075e20053421f49bf
URL:		http://gna.org/projects/kgraphviewer
BuildRequires:	graphviz
BuildRequires:	kdelibs-devel
BuildRequires:	python >= 1:2.3
BuildRequires:	scons >= 0.96
Requires:	graphviz
Requires:	kdelibs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KGraphViewer is a GraphViz dot graph viewer for KDE. KGraphViewer has
the following features:
- full featured printing
- zooming
- loading of several graphs in tabs
- saving of the recent files list
- manual and automatic reload of files
- display of a bird-eye view of the graph (can be disabled)
- moving of the graph by dragging
- (somewhat) perfect drawing of all graphviz (2.2.1) example graphs,
  some problems with 2.8
- automaticaly choose dot for directed graphs and neato for undirected
  and possibility to choose an arbitrary program generating xdot format
- open new instances as new tabs in the existing window (configurable)
- help system: run-time documentation and user guide
- internationalization (currently eng, fre)

%description -l pl.UTF-8
KGraphViewer jest przeznaczoną dla KDE przeglądarką grafów GraphViza
zapisanych w formacie dot. Ma następujące możliwości:
- drukowanie
- powiększanie
- ładowanie grafów do osobnych zakładek
- listę ostatnio otwieranych plików
- ponowne ładowanie plików ręczne i automatyczne
- widok z lotu ptaka
- przesuwanie grafu za pomocą przeciągania
- (prawie) perfekcyjną obsługę wszystkich grafów przykładowych z
  graphviza (w wersji 2.2.1), występują problemy z wersją 2.8
- automatyczny wybór "dot" dla grafów skierowanych i "neato" dla
  grafów nieskierowanych; możliwość wybrania dowolnego programu do
  utworzenia pliku w formacie xdot
- otwarcie nowej instancji jako nowej zakładki w istniejącym oknie
  (konfigurowalne)
- system pomocy: przewodnik użytkownika i pomoc w czasie działania
  programu
- umiędzynarodowiony (aktualnie języki angielski i francuski)

%prep
%setup -q -n %{name}

%build
./configure \
	prefix=%{_prefix} \
	execprefix=%{_exec_prefix} \
	datadir=%{_datadir} \
	libdir=%{_libdir} \
	kdeincludes=%{_includedir} \
	qtincludes=%{_includedir}/qt \
	kdelibs=%{_libdir} \
	qtlibs=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/services
mv -f $RPM_BUILD_ROOT%{_desktopdir}/kde/%{name}_part.desktop $RPM_BUILD_ROOT%{_datadir}/services/%{name}_part.desktop
rm -rf $RPM_BUILD_ROOT%{_desktopdir}/kde
mv -f $RPM_BUILD_ROOT%{_datadir}/applnk/Utilities/%{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
rm -rf $RPM_BUILD_ROOT%{_datadir}/applnk/Utilities

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS  ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/kde3/*
%{_desktopdir}/%{name}.desktop
%{_datadir}/apps/%{name}
%{_datadir}/apps/%{name}part
%{_datadir}/config.kcfg/*.kcfg
%{_datadir}/mimelnk/application/*.desktop
%{_datadir}/services/%{name}_part.desktop
%{_iconsdir}/hicolor/*x*/apps/%{name}.png

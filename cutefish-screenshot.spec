%define oname screenshot

Name:           cutefish-screenshot
Version:        0.5
Release:        1
Summary:        Screenshot tool
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Other
URL:            https://github.com/cutefishos/screenshot
Source:         https://github.com/cutefishos/screenshot/archive/refs/tags/%{version}/%{oname}-%{version}.tar.gz

BuildRequires:  qmake5
BuildRequires:  cmake
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  cmake(Qt5Widgets)

Requires:       qml(FishUI)
Requires:       qml(QtGraphicalEffects)
Requires:       %{_lib}qt5quick5
Requires:       qml(QtQuick.Controls)
#Requires:       qt5qmlimport(QtQuick.Layouts.1) >= 12
#Requires:       qt5qmlimport(QtQuick.Window.2) >= 12

%description
Screenshot tool for CutefishOS.


%prep
%autosetup -n %{oname}-%{version} -p1
sed -i 's/\(Name=\)\(Screenshot\)/\1Cutefish \2/' %{name}.desktop

%build
%cmake
%make_build

%install
%make_install -C build

%find_lang %{name} --with-qt --all-name

%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop

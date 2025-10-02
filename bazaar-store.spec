%global appid io.github.kolunmi.Bazaar

Name:           bazaar-store
Version:        0.5.2
Release:        1%{?dist}
Summary:        Flatpak-centric software center and app store

License:        GPL-3.0-only
URL:            https://github.com/kolunmi/bazaar
Source:         %{url}/archive/v%{version}/bazaar-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  systemd-rpm-macros
BuildRequires:  blueprint-compiler
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(xmlb)
BuildRequires:  pkgconfig(flatpak)
BuildRequires:  pkgconfig(libdex-1)
BuildRequires:  pkgconfig(yaml-0.1)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(glycin-2)
BuildRequires:  pkgconfig(glycin-gtk4-2)

%description
A new app store for GNOME with a focus on discovering and installing
applications and add-ons from Flatpak remotes, particularly Flathub.
It emphasizes supporting the developers who make the Linux desktop possible.

%prep
%autosetup -n bazaar-%{version}

%conf
%meson

%build
%meson_build

%install
%meson_install
%find_lang bazaar

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{appid}.desktop

%post
%systemd_user_post %{appid}.service

%preun
%systemd_user_preun %{appid}.service

%postun
%systemd_user_postun_with_restart %{appid}.service

%files -f bazaar.lang
%license COPYING
%doc README.md
%{_datadir}/applications/%{appid}.desktop
%{_bindir}/bazaar
%{_bindir}/bazaar-dl-worker
%{_userunitdir}/%{appid}.service
%{_datadir}/dbus-1/services/%{appid}.service
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/%{appid}.svg
%{_datadir}/icons/hicolor/symbolic/apps/%{appid}-symbolic.svg
%{_datadir}/metainfo/%{appid}.metainfo.xml
%{_datadir}/gnome-shell/search-providers/%{appid}.search-provider.ini

%changelog
* Mon Sep 08 2025 Kyle Gospodnetich <me@kylegospodneti.ch> - 0.4.8-1
- Initial release of the bazaar-store package

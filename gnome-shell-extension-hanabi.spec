%global uuid hanabi-extension@jeffshee.github.io

Name:          gnome-shell-extension-hanabi
Version:       {{{ git_dir_version }}}
Release:       1%{?dist}
Summary:       Live Wallpaper for GNOME 

Group:         User Interface/Desktops
License:       GPLv3
URL:           https://github.com/KyleGospo/gnome-ext-hanabi/
VCS:           {{{ git_dir_vcs }}}
Source:        {{{ git_dir_pack }}}
BuildArch:     noarch

Requires:      gnome-shell >= 3.12
Requires:      clapper

BuildRequires: glib2

%description
Live Wallpaper for GNOME

%prep
{{{ git_dir_setup_macro }}}
rm src/meson.build

%build
glib-compile-schemas src/schemas
mv src/metadata.json.in src/metadata.json
sed -i 's@\@settings_schema\@@io.github.jeffshee.hanabi-extension@g' src/metadata.json
sed -i 's@\@uuid\@@hanabi-extension\@jeffshee.github.io@g' src/metadata.json
sed -i 's@\@version\@@1.0@g' src/metadata.json

%install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
cp -r src/* %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/

%files
%license LICENSE
%{_datadir}/gnome-shell/extensions/%{uuid}/

%changelog
{{{ git_dir_changelog }}}
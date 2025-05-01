Name: MIDI-Player-GUI
Version: 1.1
Release: 3%{?dist}
#Release: %autorelease
Summary: MIDI-Player-GUI
License: CHANGE ME
URL: https://github.com/Mormacill/MIDI-Player-GUI
Source0: https://github.com/Mormacill/MIDI-Player-GUI/archive/refs/tags/%{version}.tar.gz
Patch0: port.patch

BuildArch: noarch

Requires: python3-tkinter
Requires: python3-mido
Requires: python3-rtmidi

%description
This is the MIDI Player GUI Package.

%prep
%autosetup

%build

%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 midi.py %{buildroot}/usr/bin/midiPG

%files
/usr/bin/midiPG

%changelog
%autochangelog

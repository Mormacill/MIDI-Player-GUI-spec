Name: MPG
Version: 1.0
Release: %autorelease
Summary: MIDI-Player-GUI
License: 
URL: https://github.com/Mormacill/MIDI-Player-GUI
Source0: https://github.com/Mormacill/MIDI-Player-GUI/archive/refs/tags/%{version}.tar.gz

Requires: python3-tkinter
Requires: python3-mido
Requires: python3-rtmidi

%description
This is the MIDI Player GUI Package.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 midi.py %{buildroot}/usr/bin/midiPG

%files
/usr/bin/midiPG

%changelog
%autochangelog

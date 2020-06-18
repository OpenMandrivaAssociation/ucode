Name:		ucode
Version:	0.20200618
Release:	1
Source0:	https://github.com/algernon/ucode/archive/master/%{name}-%{version}.tar.gz
# https://github.com/algernon/ucode/issues/2
Patch0:		ucode-20200618-issue-2.patch
Patch1:		ucode-another-way-out.patch
Group:		Toys
License:	LGPLv3+
Summary:	Tool for entering unicode characters
BuildRequires:	pkgconfig(x11)
BuildRequires:	xdotool-devel

%description
This program acts as a daemon, which grabs Ctrl+Shift+U key combination
and allows to enter Unicode character by typing its hexadecimal code.

Running ucode lets you enter Unicode characters in any application
by using this sequence:

1. Press and hold Ctrl and Shift
2. Press U
3. Release Ctrl, Shift and U
4. Type the hexadecimal code, e.g. 3b4 for Greek delta δ
5. Press space

%prep
%autosetup -p1 -n %{name}-master

%build
%{__cc} %{optflags} -std=c99 -o ucode ucode.c -lX11 -lxdo

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 ucode %{buildroot}%{_bindir}

# Not yet
%if 0
mkdir -p %{buildroot}%{_sysconfdir}/xdg/autostart
cat >%{buildroot}%{_sysconfdir}/xdg/autostart/ucode.desktop <<EOF
[Desktop Entry]
Name=Unicode character entry
GenericName=Unicode character entry
Exec=%{_bindir}/ucode
X-KDE-StartupNotify=false
Icon=openmandriva
Type=Application
Terminal=false
Categories=Utility;
EOF
%endif

%files
%{_bindir}/ucode
%if 0
%{_sysconfdir}/xdg/autostart/ucode.desktop
%endif

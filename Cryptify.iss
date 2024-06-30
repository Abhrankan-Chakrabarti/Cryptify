; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "Cryptify"
#define MyAppVersion "1.0.1"
#define MyAppPublisher "FoxHackerz"
#define MyAppExeName "Cryptify.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{50D0C873-BD0E-4A47-B01C-C266C20C4F45}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName=C:\Program Files\{#MyAppName}
DisableDirPage=yes
DisableProgramGroupPage=yes
LicenseFile=C:\Users\Admin\Desktop\Github\License.txt
; Uncomment the following line to run in non administrative install mode (install for current user only.)
;PrivilegesRequired=lowest
OutputDir=C:\Users\Admin\Desktop
OutputBaseFilename=CryptifySetup
SetupIconFile=C:\Users\Admin\Desktop\Github\Logo.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Program Files (x86)\Cryptify\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Program Files (x86)\Cryptify\bg2.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Program Files (x86)\Cryptify\branch.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Program Files (x86)\Cryptify\Cryptify.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Program Files (x86)\Cryptify\dlib-19.22.99-cp39-cp39-win_amd64.whl"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Program Files (x86)\Cryptify\Engine.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Program Files (x86)\Cryptify\face.pyc"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Program Files (x86)\Cryptify\fr1.pyc"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Program Files (x86)\Cryptify\fr2.pyc"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Program Files (x86)\Cryptify\Logo.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Program Files (x86)\Cryptify\main.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Program Files (x86)\Cryptify\main2.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Program Files (x86)\Cryptify\menu.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Program Files (x86)\Cryptify\newface.pyc"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Program Files (x86)\Cryptify\password_chooser_bg.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Program Files (x86)\Cryptify\req.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Program Files (x86)\Cryptify\UI.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Program Files (x86)\Cryptify\UI2.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Program Files (x86)\Cryptify\unins000.dat"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Program Files (x86)\Cryptify\unins000.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Program Files (x86)\Cryptify\UI\*"; DestDir: "{app}/UI"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent


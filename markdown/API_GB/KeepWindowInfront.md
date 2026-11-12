---
title: "Keeping Add-in Windows in the Foreground"
project: ""
interface: ""
member: ""
kind: "topic"
source: "API_GB/KeepWindowInfront.htm"
---

# Keeping Add-in Windows in the Foreground

When an add-in displays a dialog box, the add-in needs to keep the dialog box in front of whatever window launched it. Failure to do so may result in the dialog box disappearing and the user becoming confused.

### C++

To keep the dialog box in the foreground, you can specify a parent window handle when the new dialog box is created.

### VB.NET or C#

Window handling is supported in SOLIDWORKS PDM Professional 6.4 and later. In SOLIDWORKS PDM Professional 6.4 only, you must also enable the Multithreaded Add-ins Threading policy.

Unlike Visual Basic 6, VB.NET and C# allow you to create add-in modules that support multi-threading. When SOLIDWORKS PDM Professional runs a multi-threaded NET add-in, it executes it in the same thread as the parent window. Calls to [IEdmVault5::SetAddInWnd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~SetAddInWnd.html), which were previously recommended for Visual Basic 6, are no longer necessary.

To keep an add-in window in the foreground, call [IEdmVault8::GetWin32Window](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault8~GetWin32Window.html) in the .NET form of your add-in to specify the handle of the parent window.

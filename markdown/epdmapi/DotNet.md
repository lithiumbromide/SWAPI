---
title: "Using VB.NET"
project: ""
interface: ""
member: ""
kind: "topic"
source: "epdmapi/DotNet.htm"
---

# Using VB.NET

Versions of SOLIDWORKS PDM Professional before 2008 supported Visual Basic 6. SOLIDWORKS PDM Professional 2008, and later, support VB.NET. Users who want to port their Visual Basic 6 applications to VB.NET applications need to know how to:

- Create [stand-alone](StandAloneApp.htm) and [add-in](DotNetAddIns.htm) applications in VB.NET.
- Add dependencies **EPDM.Interop.epdm.dll** and **EPDM.Interop.EPDMResultCode.dll** by:

  1. Opening your project in Visual Studio.
  2. Right-clicking the project name in the Solution Explorer.
  3. Selecting **Add > Project Reference.**
  4. Clicking **Browse tab > Browse...** and navigating to the top folder of your SOLIDWORKS PDM Professional installation.
  5. Locating and selecting **EPDM.Interop.epdm.dll**.
  6. Clicking **Add** and **OK.**
  7. Repeating step 3.
  8. Locating and selecting **EPDM.Interop.EPDMResultCode.dll**.
  9. Repeating step 5.
- Obtain window handles:

  - Visual Basic 6 syntax:

```vb
 Me.hWnd
```

- VB.NET syntax:

```vb
 Me.Handle.ToInt32()
```

- [Keep add-in windows in the foreground](KeepWindowInfront.htm).

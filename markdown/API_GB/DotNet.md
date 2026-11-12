---
title: "Using VB.NET"
project: ""
interface: ""
member: ""
kind: "topic"
source: "API_GB/DotNet.htm"
---

# Using VB.NET

Versions of SOLIDWORKS PDM Professional before 2008 supported Visual Basic 6. SOLIDWORKS PDM Professional 2008, and later, support VB.NET. Users who want to port their Visual Basic 6 applications to VB.NET applications need to know how to:

- Create [stand-alone](StandAloneApp.htm) and [add-in](DotNetAddIns.htm) applications in VB.NET.
- Import the SOLIDWORKS PDM Professional primary interop assembly.

  In your open project in Microsoft Visual Studio:

  1. Right-click the project name in the Solution Explorer.
  2. Select **Add Reference**.
  3. Select **Framework** in the left-side panel.
  4. Browse to the top folder of your SOLIDWORKS PDM Professional installation.
  5. Locate and select **EPDM.Interop.epdm.dll**.
  6. Click **Open**
  7. Click **Add.**
  8. Click **Close**.
- Obtain window handles.

  - Visual Basic 6 syntax:

```vb
 Me.hWnd
```

- VB.NET syntax:

```vb
 Me.Handle.ToInt32()
```

- [Keep add-in windows in the foreground](KeepWindowInfront.htm).

---
title: "GetPrintRange Method (IPrintManager)"
project: ""
interface: "IPrintManager"
member: "GetPrintRange"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPrintManager~GetPrintRange.html"
---

# GetPrintRange Method (IPrintManager)

Gets the area to print.

## Syntax

### Visual Basic

```vb
Sub GetPrintRange( _
   ByRef PrintRange As dsPrintRange_e, _
   ByRef NamedView As System.String, _
   ByRef WithinSpecifiedWindow As System.Boolean, _
   ByRef WinXMin As System.Double, _
   ByRef WinYMin As System.Double, _
   ByRef WinXMax As System.Double, _
   ByRef WinYMax As System.Double _
)
```

### C#

```csharp
void GetPrintRange(
   out dsPrintRange_e PrintRange,
   out System.string NamedView,
   out System.bool WithinSpecifiedWindow,
   out System.double WinXMin,
   out System.double WinYMin,
   out System.double WinXMax,
   out System.double WinYMax
)
```

### JScript

```
function GetPrintRange(
   PrintRange : dsPrintRange_e,
   NamedView : System.String,
   WithinSpecifiedWindow : System.boolean,
   WinXMin : System.double,
   WinYMin : System.double,
   WinXMax : System.double,
   WinYMax : System.double
);
```

### Managed Extensions for C++

```
void GetPrintRange(
   [PARAMFLAG::Out] dsPrintRange_e PrintRange,
   [PARAMFLAG::Out] System.string* NamedView,
   [PARAMFLAG::Out] System.bool WithinSpecifiedWindow,
   [PARAMFLAG::Out] System.double WinXMin,
   [PARAMFLAG::Out] System.double WinYMin,
   [PARAMFLAG::Out] System.double WinXMax,
   [PARAMFLAG::Out] System.double WinYMax
)
```

### C++/CLI

```cpp
void GetPrintRange(
   [Out] dsPrintRange_e PrintRange,
   [Out] System.String^ NamedView,
   [Out] System.bool WithinSpecifiedWindow,
   [Out] System.double WinXMin,
   [Out] System.double WinYMin,
   [Out] System.double WinXMax,
   [Out] System.double WinYMax
)
```

### Parameters

- `PrintRange`: Area to print as defined in [dsPrintRange_e](Interop.dsAutomation~Interop.dsAutomation.dsPrintRange_e.html)
- `NamedView`: Name of the user-defined view to print (see **Remarks**)
- `WithinSpecifiedWindow`: True to print the area within the specified window, false to not (see **Remarks**)
- `WinXMin`: x coordinate of the lower-diagonal point of the window (see **Remarks**)
- `WinYMin`: y coordinate of the lower-diagonal point of the window (see **Remarks**)
- `WinXMax`: x coordinate of the upper-diagonal point of the window (see **Remarks**)
- `WinYMax`: y coordinate of the upper-diagonal point of the window (see **Remarks**)

## Remarks

| This parameter... | Depends on... |
| --- | --- |
| NamedView | PrintRange being dsPrintRange_e.dsPrintRange_NamedView |
| WithinSpecifiedWindow | PrintRange being: dsPrintRange_e.dsPrintRange_DrawingBoundary, dsPrintRange_e.dsPrintRange_CurrentView, dsPrintRange_e.dsPrintRange_NamedView, or dsPrintRange_e.dsPrintRange_SpecifyWindow |
| WinXMin, WinYMin, WinXMax, and WinYMax | WithinSpecifiedWindow being true |

## See Also

[IPrintManager Interface](Interop.dsAutomation~Interop.dsAutomation.IPrintManager.html)
[IPrintManager Members](Interop.dsAutomation~Interop.dsAutomation.IPrintManager_members.html)
[IPrintManager::SetPrintRange Method](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~SetPrintRange.html)

## Availability

DraftSight V1R1.1

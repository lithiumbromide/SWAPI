---
title: "SetPrintRange Method (IPrintManager)"
project: ""
interface: "IPrintManager"
member: "SetPrintRange"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPrintManager~SetPrintRange.html"
---

# SetPrintRange Method (IPrintManager)

Sets the area to print.

## Syntax

### Visual Basic

```vb
Sub SetPrintRange( _
   ByVal PrintRange As dsPrintRange_e, _
   ByVal NamedView As System.String, _
   ByVal WithinSpecifiedWindow As System.Boolean, _
   ByVal WinXMin As System.Double, _
   ByVal WinYMin As System.Double, _
   ByVal WinXMax As System.Double, _
   ByVal WinYMax As System.Double _
)
```

### C#

```csharp
void SetPrintRange(
   dsPrintRange_e PrintRange,
   System.string NamedView,
   System.bool WithinSpecifiedWindow,
   System.double WinXMin,
   System.double WinYMin,
   System.double WinXMax,
   System.double WinYMax
)
```

### JScript

```
function SetPrintRange(
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
void SetPrintRange(
   dsPrintRange_e PrintRange,
   System.string* NamedView,
   System.bool WithinSpecifiedWindow,
   System.double WinXMin,
   System.double WinYMin,
   System.double WinXMax,
   System.double WinYMax
)
```

### C++/CLI

```cpp
void SetPrintRange(
   dsPrintRange_e PrintRange,
   System.String^ NamedView,
   System.bool WithinSpecifiedWindow,
   System.double WinXMin,
   System.double WinYMin,
   System.double WinXMax,
   System.double WinYMax
)
```

### Parameters

- `PrintRange`: Area to print as defined in [dsPrintRange_e](Interop.dsAutomation~Interop.dsAutomation.dsPrintRange_e.html)
- `NamedView`: Name of a user-defined view to print (see **Remarks**)
- `WithinSpecifiedWindow`: True to print the area within the specified window, false to not
- `WinXMin`: x coordinate for the lower-diagonal point of the window (see **Remarks**)
- `WinYMin`: y coordinate for the lower-diagonal point of the window (see **Remarks**)
- `WinXMax`: x coordinate for the upper-diagonal point of the window (see **Remarks**)
- `WinYMax`: y coordinate for the upper-diagonal point of the window (see **Remarks**)

## Examples

See the [IPrintManager](Interop.dsAutomation~Interop.dsAutomation.IPrintManager.html) examples.

## Remarks

| To set this parameter... | Set... |
| --- | --- |
| NamedView | PrintRange to dsPrintRange_e.dsPrintRange_NamedView |
| WithinSpecifiedWindow | PrintRange to: dsPrintRange_e.dsPrintRange_DrawingBoundary, dsPrintRange_e.dsPrintRange_CurrentView, dsPrintRange_e.dsPrintRange_NamedView, or dsPrintRange_e.dsPrintRange_SpecifyWindow |
| WinXMin, WinYMin, WinXMax, and WinYMax | WithinSpecifiedWindow to true and PrintRange to dsPrintRange_e.dsPrintRange_SpecifyWindow |

If you set PrintRange to dsPrintRange_e.dsPrintRange_AllGeometry, then all other parameter values are ignored.

## See Also

[IPrintManager Interface](Interop.dsAutomation~Interop.dsAutomation.IPrintManager.html)
[IPrintManager Members](Interop.dsAutomation~Interop.dsAutomation.IPrintManager_members.html)
[IPrintManager::GetPrintRange Method](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~GetPrintRange.html)

## Availability

DraftSight V1R1.1

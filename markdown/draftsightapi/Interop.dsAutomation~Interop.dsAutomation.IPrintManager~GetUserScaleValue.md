---
title: "GetUserScaleValue Method (IPrintManager)"
project: ""
interface: "IPrintManager"
member: "GetUserScaleValue"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPrintManager~GetUserScaleValue.html"
---

# GetUserScaleValue Method (IPrintManager)

Gets the user-defined paper and drawing units (millimeters or inches) for printing.

## Syntax

### Visual Basic

```vb
Sub GetUserScaleValue( _
   ByRef PaperUnits As System.Double, _
   ByRef DrawingUnits As System.Double _
)
```

### C#

```csharp
void GetUserScaleValue(
   out System.double PaperUnits,
   out System.double DrawingUnits
)
```

### JScript

```
function GetUserScaleValue(
   PaperUnits : System.double,
   DrawingUnits : System.double
);
```

### Managed Extensions for C++

```
void GetUserScaleValue(
   [PARAMFLAG::Out] System.double PaperUnits,
   [PARAMFLAG::Out] System.double DrawingUnits
)
```

### C++/CLI

```cpp
void GetUserScaleValue(
   [Out] System.double PaperUnits,
   [Out] System.double DrawingUnits
)
```

### Parameters

- `PaperUnits`: User-defined paper units
- `DrawingUnits`: User-defined drawing units

## See Also

[IPrintManager Interface](Interop.dsAutomation~Interop.dsAutomation.IPrintManager.html)
[IPrintManager Members](Interop.dsAutomation~Interop.dsAutomation.IPrintManager_members.html)
[IPrintManager::SetUserScaleValue Method](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~SetUserScaleValue.html)
[IPrintManager::GetStandardScale Method](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~GetStandardScale.html)
[IPrintManager::SetStandardScale Method](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~SetStandardScale.html)
[IPrintManager::UserScale Property](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~UserScale.html)

## Availability

DraftSight V1R1.1

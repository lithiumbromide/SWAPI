---
title: "SetUserScaleValue Method (IPrintManager)"
project: ""
interface: "IPrintManager"
member: "SetUserScaleValue"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPrintManager~SetUserScaleValue.html"
---

# SetUserScaleValue Method (IPrintManager)

Sets the user-defined paper and drawing units (millimeters or inches) for printing.

## Syntax

### Visual Basic

```vb
Sub SetUserScaleValue( _
   ByVal PaperUnits As System.Double, _
   ByVal DrawingUnits As System.Double _
)
```

### C#

```csharp
void SetUserScaleValue(
   System.double PaperUnits,
   System.double DrawingUnits
)
```

### JScript

```
function SetUserScaleValue(
   PaperUnits : System.double,
   DrawingUnits : System.double
);
```

### Managed Extensions for C++

```
void SetUserScaleValue(
   System.double PaperUnits,
   System.double DrawingUnits
)
```

### C++/CLI

```cpp
void SetUserScaleValue(
   System.double PaperUnits,
   System.double DrawingUnits
)
```

### Parameters

- `PaperUnits`: User-defined paper units
- `DrawingUnits`: User-defined drawing units

## Remarks

To enable user-defined scaling, set:

- [IPrintManager::ScaleToFit](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~ScaleToFit.html) to false

- and -

- [IPrintManager::UserScale](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~UserScale.html) to true.

To set a standard scale, call [IPrintManager::SetStandardScale](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~SetStandardScale.html).

## See Also

[IPrintManager Interface](Interop.dsAutomation~Interop.dsAutomation.IPrintManager.html)
[IPrintManager Members](Interop.dsAutomation~Interop.dsAutomation.IPrintManager_members.html)
[IPrintManager::GetUserScaleValue Method](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~GetUserScaleValue.html)
[IPrintManager::GetStandardScale Method](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~GetStandardScale.html)

## Availability

DraftSight V1R1.1

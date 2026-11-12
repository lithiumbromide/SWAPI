---
title: "GetStandardScale Method (IPrintManager)"
project: ""
interface: "IPrintManager"
member: "GetStandardScale"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPrintManager~GetStandardScale.html"
---

# GetStandardScale Method (IPrintManager)

Gets the standard scale and value of the scale for printing.

## Syntax

### Visual Basic

```vb
Sub GetStandardScale( _
   ByRef StdScaleType As dsStandardPrintScale_e, _
   ByRef ScaleValue As System.Double _
)
```

### C#

```csharp
void GetStandardScale(
   out dsStandardPrintScale_e StdScaleType,
   out System.double ScaleValue
)
```

### JScript

```
function GetStandardScale(
   StdScaleType : dsStandardPrintScale_e,
   ScaleValue : System.double
);
```

### Managed Extensions for C++

```
void GetStandardScale(
   [PARAMFLAG::Out] dsStandardPrintScale_e StdScaleType,
   [PARAMFLAG::Out] System.double ScaleValue
)
```

### C++/CLI

```cpp
void GetStandardScale(
   [Out] dsStandardPrintScale_e StdScaleType,
   [Out] System.double ScaleValue
)
```

### Parameters

- `StdScaleType`: Type of standard scale as defined in [dsStandardPrintScale_e](Interop.dsAutomation~Interop.dsAutomation.dsStandardPrintScale_e.html)
- `ScaleValue`: Value of the scale

## See Also

[IPrintManager Interface](Interop.dsAutomation~Interop.dsAutomation.IPrintManager.html)
[IPrintManager Members](Interop.dsAutomation~Interop.dsAutomation.IPrintManager_members.html)
[IPrintManager::SetStandardScale Method](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~SetStandardScale.html)
[IPrintManager::GetUserScaleValue Method](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~GetUserScaleValue.html)
[IPrintManager::SetUserScaleValue Method](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~SetUserScaleValue.html)

## Availability

DraftSight V1R1.1

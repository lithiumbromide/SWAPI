---
title: "SetStandardScale Method (IPrintManager)"
project: ""
interface: "IPrintManager"
member: "SetStandardScale"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPrintManager~SetStandardScale.html"
---

# SetStandardScale Method (IPrintManager)

Sets the standard scale for printing.

## Syntax

### Visual Basic

```vb
Sub SetStandardScale( _
   ByVal StdScaleType As dsStandardPrintScale_e _
)
```

### C#

```csharp
void SetStandardScale(
   dsStandardPrintScale_e StdScaleType
)
```

### JScript

```
function SetStandardScale(
   StdScaleType : dsStandardPrintScale_e
);
```

### Managed Extensions for C++

```
void SetStandardScale(
   dsStandardPrintScale_e StdScaleType
)
```

### C++/CLI

```cpp
void SetStandardScale(
   dsStandardPrintScale_e StdScaleType
)
```

### Parameters

- `StdScaleType`: Type of standard scale as defined in [dsStandardPrintScale_e](Interop.dsAutomation~Interop.dsAutomation.dsStandardPrintScale_e.html)

## Remarks

This method is valid only if [IPrintManager::ScaleToFit](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~ScaleToFit.html) is set to false.

To set a user-defined scale, set [IPrintManager::UserScale](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~UserScale.html) to true and call [IPrintManager::SetUserScaleValue](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~SetUserScaleValue.html).

## See Also

[IPrintManager Interface](Interop.dsAutomation~Interop.dsAutomation.IPrintManager.html)
[IPrintManager Members](Interop.dsAutomation~Interop.dsAutomation.IPrintManager_members.html)
[IPrintManager::ScaleLineWeight Property](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~ScaleLineWeight.html)
[IPrintManager::GetStandardScale Method](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~GetStandardScale.html)
[IPrintManager::GetUserScaleValue Method](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~GetUserScaleValue.html)

## Availability

DraftSight V1R1.1

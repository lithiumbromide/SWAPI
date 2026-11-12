---
title: "SetCustomData Method (ISheet)"
project: ""
interface: "ISheet"
member: "SetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISheet~SetCustomData.html"
---

# SetCustomData Method (ISheet)

Sets the custom data for the Sheet.

## Syntax

### Visual Basic

```vb
Sub SetCustomData( _
   ByVal ApplicationName As System.String, _
   ByVal CustomData As CustomData _
)
```

### C#

```csharp
void SetCustomData(
   System.string ApplicationName,
   CustomData CustomData
)
```

### JScript

```
function SetCustomData(
   ApplicationName : System.String,
   CustomData : CustomData
);
```

### Managed Extensions for C++

```
void SetCustomData(
   System.string* ApplicationName,
   CustomData* CustomData
)
```

### C++/CLI

```cpp
void SetCustomData(
   System.String^ ApplicationName,
   CustomData^ CustomData
)
```

### Parameters

- `ApplicationName`: Name of the custom data's registered application (see **Remarks**)
- `CustomData`: [Custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html)

## Remarks

Call [IDocument::GetRegisteredApplications](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetRegisteredApplications.html) to find out the names of the document's existing custom data.

## See Also

[ISheet Interface](Interop.dsAutomation~Interop.dsAutomation.ISheet.html)
[ISheet Members](Interop.dsAutomation~Interop.dsAutomation.ISheet_members.html)
[ISheet::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ISheet~DeleteCustomData.html)
[ISheet::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ISheet~GetCustomData.html)
[ISheet::Handle Property](Interop.dsAutomation~Interop.dsAutomation.ISheet~Handle.html)

## Availability

DraftSight V1R1.2

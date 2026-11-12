---
title: "SetCustomData Method (ITolerance)"
project: ""
interface: "ITolerance"
member: "SetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITolerance~SetCustomData.html"
---

# SetCustomData Method (ITolerance)

Sets the custom data for the geometric Tolerance.

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

[ITolerance Interface](Interop.dsAutomation~Interop.dsAutomation.ITolerance.html)
[ITolerance Members](Interop.dsAutomation~Interop.dsAutomation.ITolerance_members.html)
[ITolerance::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ITolerance~DeleteCustomData.html)
[ITolerance::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ITolerance~GetCustomData.html)
[ITolerance::Handle Property](Interop.dsAutomation~Interop.dsAutomation.ITolerance~Handle.html)

## Availability

DraftSight V1R1.2

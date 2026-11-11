---
title: "SetCustomData Method (IInfiniteLine)"
project: ""
interface: "IInfiniteLine"
member: "SetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine~SetCustomData.html"
---

# SetCustomData Method (IInfiniteLine)

Sets the custom data for the InfiniteLine.

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

[IInfiniteLine Interface](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine.html)
[IInfiniteLine Members](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine_members.html)
[IInfiniteLine::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine~DeleteCustomData.html)
[IInfiniteLine::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine~GetCustomData.html)
[IInfiniteLine::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine~Handle.html)

## Availability

DraftSight V1R1.2

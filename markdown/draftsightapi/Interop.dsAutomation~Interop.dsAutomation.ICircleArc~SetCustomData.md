---
title: "SetCustomData Method (ICircleArc)"
project: ""
interface: "ICircleArc"
member: "SetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICircleArc~SetCustomData.html"
---

# SetCustomData Method (ICircleArc)

Sets the custom data for the Arc.

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

[ICircleArc Interface](Interop.dsAutomation~Interop.dsAutomation.ICircleArc.html)
[ICircleArc Members](Interop.dsAutomation~Interop.dsAutomation.ICircleArc_members.html)
[ICircleArc::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ICircleArc~DeleteCustomData.html)
[ICircleArc::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ICircleArc~GetCustomData.html)
[ICircleArc::Handle Property](Interop.dsAutomation~Interop.dsAutomation.ICircleArc~Handle.html)

## Availability

DraftSight V1R1.2

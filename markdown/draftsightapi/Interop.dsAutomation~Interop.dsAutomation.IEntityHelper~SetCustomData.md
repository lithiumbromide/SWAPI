---
title: "SetCustomData Method (IEntityHelper)"
project: ""
interface: "IEntityHelper"
member: "SetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~SetCustomData.html"
---

# SetCustomData Method (IEntityHelper)

Sets the specified custom data for the specified entity.

## Syntax

### Visual Basic

```vb
Sub SetCustomData( _
   ByVal Obj As System.Object, _
   ByVal ApplicationName As System.String, _
   ByVal CustomData As CustomData _
)
```

### C#

```csharp
void SetCustomData(
   System.object Obj,
   System.string ApplicationName,
   CustomData CustomData
)
```

### JScript

```
function SetCustomData(
   Obj : System.Object,
   ApplicationName : System.String,
   CustomData : CustomData
);
```

### Managed Extensions for C++

```
void SetCustomData(
   System.Object* Obj,
   System.string* ApplicationName,
   CustomData* CustomData
)
```

### C++/CLI

```cpp
void SetCustomData(
   System.Object^ Obj,
   System.String^ ApplicationName,
   CustomData^ CustomData
)
```

### Parameters

- `Obj`: Entity
- `ApplicationName`: Name of the custom data's registered application (see **Remarks**)
- `CustomData`: [Custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html)

## Remarks

Call [IDocument::GetRegisteredApplications](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetRegisteredApplications.html) to find out the names of the document's existing custom data.

## See Also

[IEntityHelper Interface](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper.html)
[IEntityHelper Members](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper_members.html)
[IEntityHelper::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~DeleteCustomData.html)
[IEntityHelper::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~GetCustomData.html)
[IEntityHelper::GetHandle Method](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~GetHandle.html)

## Availability

DraftSight V1R3.0

---
title: "DeleteCustomData Method (IEntityHelper)"
project: ""
interface: "IEntityHelper"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~DeleteCustomData.html"
---

# DeleteCustomData Method (IEntityHelper)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from the specified entity.

## Syntax

### Visual Basic

```vb
Sub DeleteCustomData( _
   ByVal Obj As System.Object, _
   ByVal ApplicationName As System.String _
)
```

### C#

```csharp
void DeleteCustomData(
   System.object Obj,
   System.string ApplicationName
)
```

### JScript

```
function DeleteCustomData(
   Obj : System.Object,
   ApplicationName : System.String
);
```

### Managed Extensions for C++

```
void DeleteCustomData(
   System.Object* Obj,
   System.string* ApplicationName
)
```

### C++/CLI

```cpp
void DeleteCustomData(
   System.Object^ Obj,
   System.String^ ApplicationName
)
```

### Parameters

- `Obj`: Entity
- `ApplicationName`: Name of the custom data's registered application (see **Remarks**)

## Remarks

Call [IDocument::GetRegisteredApplications](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetRegisteredApplications.html) to find out the names of the document's existing custom data.

## See Also

[IEntityHelper Interface](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper.html)
[IEntityHelper Members](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper_members.html)
[IEntityHelper::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~GetCustomData.html)
[IEntityHelper::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~SetCustomData.html)
[IEntityHelper::GetHandle Method](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~GetHandle.html)

## Availability

DraftSight V1R3.0

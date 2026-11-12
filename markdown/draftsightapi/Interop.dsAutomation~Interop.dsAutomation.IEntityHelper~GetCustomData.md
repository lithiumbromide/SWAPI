---
title: "GetCustomData Method (IEntityHelper)"
project: ""
interface: "IEntityHelper"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~GetCustomData.html"
---

# GetCustomData Method (IEntityHelper)

Gets the specified custom data for the specified entity.

## Syntax

### Visual Basic

```vb
Function GetCustomData( _
   ByVal Obj As System.Object, _
   ByVal ApplicationName As System.String _
) As CustomData
```

### C#

```csharp
CustomData GetCustomData(
   System.object Obj,
   System.string ApplicationName
)
```

### JScript

```
function GetCustomData(
   Obj : System.Object,
   ApplicationName : System.String
) : CustomData;
```

### Managed Extensions for C++

```
CustomData* GetCustomData(
   System.Object* Obj,
   System.string* ApplicationName
)
```

### C++/CLI

```cpp
CustomData^ GetCustomData(
   System.Object^ Obj,
   System.String^ ApplicationName
)
```

### Parameters

- `Obj`: Entity
- `ApplicationName`: Name of the custom data's registered application

### Return Value

[Custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html)

## Remarks

Call [IDocument::GetRegisteredApplications](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetRegisteredApplications.html) to find out the names of the document's existing custom data.

## See Also

[IEntityHelper Interface](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper.html)
[IEntityHelper Members](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper_members.html)
[IEntityHelper::DeleteCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~DeleteCustomData.html)
[IEntityHelper::GetHandle Method ()](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~GetHandle.html)
[IEntityHelper::SetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~SetCustomData.html)

## Availability

DraftSight V1R3.0

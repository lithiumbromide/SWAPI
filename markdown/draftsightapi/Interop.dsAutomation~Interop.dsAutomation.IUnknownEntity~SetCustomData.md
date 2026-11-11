---
title: "SetCustomData Method (IUnknownEntity)"
project: ""
interface: "IUnknownEntity"
member: "SetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IUnknownEntity~SetCustomData.html"
---

# SetCustomData Method (IUnknownEntity)

Sets the custom data for this unknown entity.

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

[IUnknownEntity Interface](Interop.dsAutomation~Interop.dsAutomation.IUnknownEntity.html)
[IUnknownEntity Members](Interop.dsAutomation~Interop.dsAutomation.IUnknownEntity_members.html)
[IUnknownEntity::DeleteCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IUnknownEntity~DeleteCustomData.html)
[IUnknownEntity::GetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IUnknownEntity~GetCustomData.html)
[IUnknownEntity::Handle Property ()](Interop.dsAutomation~Interop.dsAutomation.IUnknownEntity~Handle.html)

## Availability

DraftSight 2018 SP2

---
title: "DeleteCustomData Method (IUnknownEntity)"
project: ""
interface: "IUnknownEntity"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IUnknownEntity~DeleteCustomData.html"
---

# DeleteCustomData Method (IUnknownEntity)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from the unknown entity.

## Syntax

### Visual Basic

```vb
Sub DeleteCustomData( _
   ByVal ApplicationName As System.String _
)
```

### C#

```csharp
void DeleteCustomData(
   System.string ApplicationName
)
```

### JScript

```
function DeleteCustomData(
   ApplicationName : System.String
);
```

### Managed Extensions for C++

```
void DeleteCustomData(
   System.string* ApplicationName
)
```

### C++/CLI

```cpp
void DeleteCustomData(
   System.String^ ApplicationName
)
```

### Parameters

- `ApplicationName`: Name of the custom data's registered application (see **Remarks**)

## Remarks

Call [IDocument::GetRegisteredApplications](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetRegisteredApplications.html) to find out the names of the document's existing custom data.

## See Also

[IUnknownEntity Interface](Interop.dsAutomation~Interop.dsAutomation.IUnknownEntity.html)
[IUnknownEntity Members](Interop.dsAutomation~Interop.dsAutomation.IUnknownEntity_members.html)
[IUnknownEntity::GetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IUnknownEntity~GetCustomData.html)
[IUnknownEntity::SetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IUnknownEntity~SetCustomData.html)
[IUnknownEntity::Handle Property ()](Interop.dsAutomation~Interop.dsAutomation.IUnknownEntity~Handle.html)

## Availability

DraftSight 2018 SP2

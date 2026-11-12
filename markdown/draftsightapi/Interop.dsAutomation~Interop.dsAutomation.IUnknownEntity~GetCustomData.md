---
title: "GetCustomData Method (IUnknownEntity)"
project: ""
interface: "IUnknownEntity"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IUnknownEntity~GetCustomData.html"
---

# GetCustomData Method (IUnknownEntity)

Gets the specified custom data for this unknown entity.

## Syntax

### Visual Basic

```vb
Function GetCustomData( _
   ByVal ApplicationName As System.String _
) As CustomData
```

### C#

```csharp
CustomData GetCustomData(
   System.string ApplicationName
)
```

### JScript

```
function GetCustomData(
   ApplicationName : System.String
) : CustomData;
```

### Managed Extensions for C++

```
CustomData* GetCustomData(
   System.string* ApplicationName
)
```

### C++/CLI

```cpp
CustomData^ GetCustomData(
   System.String^ ApplicationName
)
```

### Parameters

- `ApplicationName`: Name of the custom data's registered application (see **Remarks**)

### Return Value

[Custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html)

## Remarks

Call [IDocument::GetRegisteredApplications](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetRegisteredApplications.html) to find out the names of the document's existing custom data.

## See Also

[IUnknownEntity Interface](Interop.dsAutomation~Interop.dsAutomation.IUnknownEntity.html)
[IUnknownEntity Members](Interop.dsAutomation~Interop.dsAutomation.IUnknownEntity_members.html)
[IUnknownEntity::DeleteCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IUnknownEntity~DeleteCustomData.html)
[IUnknownEntity::SetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IUnknownEntity~SetCustomData.html)
[IUnknownEntity::Handle Property ()](Interop.dsAutomation~Interop.dsAutomation.IUnknownEntity~Handle.html)

## Availability

DraftSight 2018 SP2

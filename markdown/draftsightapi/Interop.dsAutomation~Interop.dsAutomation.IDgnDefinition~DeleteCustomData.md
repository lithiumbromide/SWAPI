---
title: "DeleteCustomData Method (IDgnDefinition)"
project: ""
interface: "IDgnDefinition"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDgnDefinition~DeleteCustomData.html"
---

# DeleteCustomData Method (IDgnDefinition)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from the DGN definition.

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

[IDgnDefinition Interface](Interop.dsAutomation~Interop.dsAutomation.IDgnDefinition.html)
[IDgnDefinition Members](Interop.dsAutomation~Interop.dsAutomation.IDgnDefinition_members.html)
[IDgnDefinition::GetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IDgnDefinition~GetCustomData.html)
[IDgnDefinition::SetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IDgnDefinition~SetCustomData.html)
[IDgnDefinition::Handle Property ()](Interop.dsAutomation~Interop.dsAutomation.IDgnDefinition~Handle.html)

## Availability

DraftSight 2020 SP0

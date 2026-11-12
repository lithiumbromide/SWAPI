---
title: "DeleteCustomData Method (ISolid3D)"
project: ""
interface: "ISolid3D"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISolid3D~DeleteCustomData.html"
---

# DeleteCustomData Method (ISolid3D)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from this 3D solid.

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

[ISolid3D Interface](Interop.dsAutomation~Interop.dsAutomation.ISolid3D.html)
[ISolid3D Members](Interop.dsAutomation~Interop.dsAutomation.ISolid3D_members.html)
[ISolid3D::GetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.ISolid3D~GetCustomData.html)
[ISolid3D::SetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.ISolid3D~SetCustomData.html)

## Availability

DraftSight 2020 SP0

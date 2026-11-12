---
title: "DeleteCustomData Method (IPolyFaceMesh)"
project: ""
interface: "IPolyFaceMesh"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh~DeleteCustomData.html"
---

# DeleteCustomData Method (IPolyFaceMesh)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from the polygon face mesh.

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

[IPolyFaceMesh Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh.html)
[IPolyFaceMesh Members](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh_members.html)
[IPolyFaceMesh::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh~GetCustomData.html)
[IPolyFaceMesh::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh~SetCustomData.html)
[IPolyFaceMesh::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh~Handle.html)

## Availability

DraftSight V1R1.3

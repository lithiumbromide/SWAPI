---
title: "DeleteCustomData Method (IPolygonMesh)"
project: ""
interface: "IPolygonMesh"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh~DeleteCustomData.html"
---

# DeleteCustomData Method (IPolygonMesh)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from the PolygonMesh.

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

[IPolygonMesh Interface](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh.html)
[IPolygonMesh Members](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh_members.html)
[IPolygonMesh::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh~GetCustomData.html)
[IPolygonMesh::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh~SetCustomData.html)
[IPolygonMesh::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh~Handle.html)

## Availability

DraftSight V1R1.3

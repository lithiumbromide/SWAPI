---
title: "GetCustomData Method (IPolygonMesh)"
project: ""
interface: "IPolygonMesh"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh~GetCustomData.html"
---

# GetCustomData Method (IPolygonMesh)

Gets the specified custom data for the PolygonMesh.

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

[IPolygonMesh Interface](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh.html)
[IPolygonMesh Members](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh_members.html)
[IPolygonMesh::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh~DeleteCustomData.html)
[IPolygonMesh::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh~SetCustomData.html)
[IPolygonMesh::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh~Handle.html)

## Availability

DraftSight V1R1.3

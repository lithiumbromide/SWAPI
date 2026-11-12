---
title: "SetCustomData Method (IPolygonMesh)"
project: ""
interface: "IPolygonMesh"
member: "SetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh~SetCustomData.html"
---

# SetCustomData Method (IPolygonMesh)

Sets the custom data for the PolygonMesh.

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

[IPolygonMesh Interface](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh.html)
[IPolygonMesh Members](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh_members.html)
[IPolygonMesh::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh~DeleteCustomData.html)
[IPolygonMesh::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh~GetCustomData.html)
[IPolygonMesh::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh~Handle.html)

## Availability

DraftSight V1R1.3

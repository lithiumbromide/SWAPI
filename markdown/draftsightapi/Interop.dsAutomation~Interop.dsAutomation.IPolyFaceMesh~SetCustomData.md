---
title: "SetCustomData Method (IPolyFaceMesh)"
project: ""
interface: "IPolyFaceMesh"
member: "SetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh~SetCustomData.html"
---

# SetCustomData Method (IPolyFaceMesh)

Sets the custom data for the polygon face mesh.

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

[IPolyFaceMesh Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh.html)
[IPolyFaceMesh Members](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh_members.html)
[IPolyFaceMesh::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh~DeleteCustomData.html)
[IPolyFaceMesh::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh~GetCustomData.html)
[IPolyFaceMesh::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh~Handle.html)

## Availability

DraftSight V1R1.3

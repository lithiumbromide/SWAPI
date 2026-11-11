---
title: "GetCustomData Method (IPolyFaceMesh)"
project: ""
interface: "IPolyFaceMesh"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh~GetCustomData.html"
---

# GetCustomData Method (IPolyFaceMesh)

Gets the specified custom data for the polygon face mesh.

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

[IPolyFaceMesh Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh.html)
[IPolyFaceMesh Members](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh_members.html)
[IPolyFaceMesh::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh~Handle.html)
[IPolyFaceMesh::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh~SetCustomData.html)
[IPolyFaceMesh::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh~DeleteCustomData.html)

## Availability

DraftSight V1R1.3

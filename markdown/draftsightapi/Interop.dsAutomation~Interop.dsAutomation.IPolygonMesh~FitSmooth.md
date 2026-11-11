---
title: "FitSmooth Property (IPolygonMesh)"
project: ""
interface: "IPolygonMesh"
member: "FitSmooth"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh~FitSmooth.html"
---

# FitSmooth Property (IPolygonMesh)

Gets or sets the smoothing function to apply to the PolygonMesh.

## Syntax

### Visual Basic

```vb
Property FitSmooth As dsPolygonMeshFitSmooth_e
```

### C#

```csharp
dsPolygonMeshFitSmooth_e FitSmooth {get; set;}
```

### JScript

```
function get,set FitSmooth : dsPolygonMeshFitSmooth_e
```

### Managed Extensions for C++

```
__property dsPolygonMeshFitSmooth_e get_FitSmooth();
__property void set_FitSmooth(
   dsPolygonMeshFitSmooth_e value
);
```

### C++/CLI

```cpp
property dsPolygonMeshFitSmooth_e FitSmooth {
   dsPolygonMeshFitSmooth_e get();
   void set (    dsPolygonMeshFitSmooth_e value);
}
```

### Property Value

Smoothing function as defined in [dsPolygonMeshFitSmooth_e](Interop.dsAutomation~Interop.dsAutomation.dsPolygonMeshFitSmooth_e.html)

## Examples

[Create PolygonMesh (C#)](Create_PolygonMesh_Example_CSharp.htm)
[Create PolygonMesh (VB.NET)](Create_PolygonMesh_Example_VBNET.htm)
[Create PolygonMesh (VBA)](Create_PolygonMesh_Example_VBA.htm)

## See Also

[IPolygonMesh Interface](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh.html)
[IPolygonMesh Members](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh_members.html)

## Availability

DraftSight V1R1.3

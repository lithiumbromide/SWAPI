---
title: "LineWeight Property (IPolyFaceMesh)"
project: ""
interface: "IPolyFaceMesh"
member: "LineWeight"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh~LineWeight.html"
---

# LineWeight Property (IPolyFaceMesh)

Gets or sets the LineWeight for the polygon face mesh.

## Syntax

### Visual Basic

```vb
Property LineWeight As dsLineWeight_e
```

### C#

```csharp
dsLineWeight_e LineWeight {get; set;}
```

### JScript

```
function get,set LineWeight : dsLineWeight_e
```

### Managed Extensions for C++

```
__property dsLineWeight_e get_LineWeight();
__property void set_LineWeight(
   dsLineWeight_e value
);
```

### C++/CLI

```cpp
property dsLineWeight_e LineWeight {
   dsLineWeight_e get();
   void set (    dsLineWeight_e value);
}
```

### Property Value

LineWeight as defined in [dsLineWeight_e](Interop.dsAutomation~Interop.dsAutomation.dsLineWeight_e.html)

## Examples

[Create Polygon Face Mesh (C#)](Create_Polygon_Face_Mesh_Example_CSharp.htm)
[Create Polygon Face Mesh (VB.NET)](Create_Polygon_Face_Mesh_Example_VBNET.htm)
[Create Polygon Face Mesh (VBA)](Create_Polygon_Face_Mesh_Example_VBA.htm)

## See Also

[IPolyFaceMesh Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh.html)
[IPolyFaceMesh Members](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh_members.html)

## Availability

DraftSight V1R1.3

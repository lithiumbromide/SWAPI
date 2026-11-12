---
title: "Erased Property (IPolyFaceMesh)"
project: ""
interface: "IPolyFaceMesh"
member: "Erased"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh~Erased.html"
---

# Erased Property (IPolyFaceMesh)

Gets or sets whether to erase or restore the polygon face mesh.

## Syntax

### Visual Basic

```vb
Property Erased As System.Boolean
```

### C#

```csharp
System.bool Erased {get; set;}
```

### JScript

```
function get,set Erased : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_Erased();
__property void set_Erased(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool Erased {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to erase the polygon face mesh, false to restore it (see **Remarks**)

## Examples

[Create Polygon Face Mesh (C#)](Create_Polygon_Face_Mesh_Example_CSharp.htm)
[Create Polygon Face Mesh (VB.NET)](Create_Polygon_Face_Mesh_Example_VBNET.htm)
[Create Polygon Face Mesh (VBA)](Create_Polygon_Face_Mesh_Example_VBA.htm)

## Remarks

| If this property is set to true... | Then the polygon face mesh... |
| --- | --- |
| and the drawing remains open | is not displayed and can be restored by setting this property to false. |
| when the drawing is closed | is deleted from the drawing and cannot be restored. |

## See Also

[IPolyFaceMesh Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh.html)
[IPolyFaceMesh Members](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh_members.html)

## Availability

DraftSight V1R1.3

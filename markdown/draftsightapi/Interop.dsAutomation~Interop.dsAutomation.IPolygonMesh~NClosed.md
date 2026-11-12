---
title: "NClosed Property (IPolygonMesh)"
project: ""
interface: "IPolygonMesh"
member: "NClosed"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh~NClosed.html"
---

# NClosed Property (IPolygonMesh)

Gets or sets whether the PolygonMesh is closed in the row direction.

## Syntax

### Visual Basic

```vb
Property NClosed As System.Boolean
```

### C#

```csharp
System.bool NClosed {get; set;}
```

### JScript

```
function get,set NClosed : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_NClosed();
__property void set_NClosed(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool NClosed {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True if closed, false if open

## Examples

[Create PolygonMesh (C#)](Create_PolygonMesh_Example_CSharp.htm)
[Create PolygonMesh (VB.NET)](Create_PolygonMesh_Example_VBNET.htm)
[Create PolygonMesh (VBA)](Create_PolygonMesh_Example_VBA.htm)

## See Also

[IPolygonMesh Interface](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh.html)
[IPolygonMesh Members](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh_members.html)
[IPolygonMesh::MClosed Property](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh~MClosed.html)

## Availability

DraftSight V1R1.3

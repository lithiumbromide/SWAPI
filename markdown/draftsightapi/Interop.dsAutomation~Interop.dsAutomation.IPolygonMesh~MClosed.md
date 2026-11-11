---
title: "MClosed Property (IPolygonMesh)"
project: ""
interface: "IPolygonMesh"
member: "MClosed"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh~MClosed.html"
---

# MClosed Property (IPolygonMesh)

Gets or sets whether the PolygonMesh is closed in the column direction.

## Syntax

### Visual Basic

```vb
Property MClosed As System.Boolean
```

### C#

```csharp
System.bool MClosed {get; set;}
```

### JScript

```
function get,set MClosed : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_MClosed();
__property void set_MClosed(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool MClosed {
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
[IPolygonMesh::NClosed Property](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh~NClosed.html)

## Availability

DraftSight V1R1.3

---
title: "Erased Property (IPolygonMesh)"
project: ""
interface: "IPolygonMesh"
member: "Erased"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh~Erased.html"
---

# Erased Property (IPolygonMesh)

Gets or sets whether to erase or restore the PolygonMesh.

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

True to erase the PoygonMesh, false to restore it (see **Remarks**)

## Examples

[Create PolygonMesh (C#)](Create_PolygonMesh_Example_CSharp.htm)
[Create PolygonMesh (VB.NET)](Create_PolygonMesh_Example_VBNET.htm)
[Create PolygonMesh (VBA)](Create_PolygonMesh_Example_VBA.htm)

## Remarks

| If this property is set to true... | Then the PolygonMesh... |
| --- | --- |
| and the drawing remains open | is not displayed and can be restored by setting this property to false. |
| when the drawing is closed | is deleted from the drawing and cannot be restored. |

## See Also

[IPolygonMesh Interface](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh.html)
[IPolygonMesh Members](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh_members.html)

## Availability

DraftSight V1R1.3

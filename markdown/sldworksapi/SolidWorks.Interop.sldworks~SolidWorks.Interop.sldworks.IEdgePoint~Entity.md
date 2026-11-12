---
title: "Entity Property (IEdgePoint)"
project: "SOLIDWORKS API Help"
interface: "IEdgePoint"
member: "Entity"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgePoint~Entity.html"
---

# Entity Property (IEdgePoint)

Gets or sets edge or reference curve on which the point is located.

## Syntax

### Visual Basic (Declaration)

```vb
Property Entity As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IEdgePoint
Dim value As System.Object

instance.Entity = value

value = instance.Entity
```

### C#

```csharp
System.object Entity {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Entity {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) or [reference curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IReferenceCurve.html)

## VBA Syntax

See [EdgePoint::Entity](ms-its:sldworksapivb6.chm::/sldworks~EdgePoint~Entity.html).

## See Also

[IEdgePoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgePoint.html)
[IEdgePoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgePoint_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0

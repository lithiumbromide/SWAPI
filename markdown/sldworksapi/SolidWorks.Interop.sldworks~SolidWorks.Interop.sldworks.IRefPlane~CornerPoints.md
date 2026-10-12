---
title: "CornerPoints Property (IRefPlane)"
project: "SOLIDWORKS API Help"
interface: "IRefPlane"
member: "CornerPoints"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane~CornerPoints.html"
---

# CornerPoints Property (IRefPlane)

Gets the corner points of this reference plane.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CornerPoints As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IRefPlane
Dim value As System.Object

value = instance.CornerPoints
```

### C#

```csharp
System.object CornerPoints {get;}
```

### C++/CLI

```cpp
property System.Object^ CornerPoints {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of four (4) [IMathpoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) objects

## VBA Syntax

See [RefPlane::CornerPoints](ms-its:sldworksapivb6.chm::/sldworks~RefPlane~CornerPoints.html).

## Examples

[Get Corner Points of Reference Plane (VBA)](Get_Corner_Points_of_Reference_Plane_Example_VB.htm)
[Get Corner Points of Reference Plane (VB.NET)](Get_Corner_Points_of_Reference_Plane_Example_VBNET.htm)
[Get Corner Points of Reference Plane (C#)](Get_Corner_Points_of_Reference_Plane_Example_CSharp.htm)

## See Also

[IRefPlane Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html)
[IRefPlane Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane_members.html)
[IRefPlane::IGetCornerPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane~IGetCornerPoints.html)

## Availability

SOLIDWORKS 2009 SP5, Revision Number 17.5

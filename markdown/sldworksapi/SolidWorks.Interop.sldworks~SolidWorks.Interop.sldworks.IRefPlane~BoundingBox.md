---
title: "BoundingBox Property (IRefPlane)"
project: "SOLIDWORKS API Help"
interface: "IRefPlane"
member: "BoundingBox"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane~BoundingBox.html"
---

# BoundingBox Property (IRefPlane)

Gets the bounding box of the reference plane, the top-left and bottom-right points.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property BoundingBox As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IRefPlane
Dim value As System.Object

value = instance.BoundingBox
```

### C#

```csharp
System.object BoundingBox {get;}
```

### C++/CLI

```cpp
property System.Object^ BoundingBox {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array containing bounding box, always two (2) [IMathpoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) objects

## VBA Syntax

See [RefPlane::BoundingBox](ms-its:sldworksapivb6.chm::/sldworks~RefPlane~BoundingBox.html).

## Examples

[Get Coordinates of the Plane's Bounding Box (C#)](Get_Coordinates_of_the_Plane's_Bounding_Box_Example_CSharp.htm)
[Get Coordinates of the Plane's Bounding Box (VB.NET)](Get_Coordinates_of_the_Plane's_Bounding_Box_Example_VBNET.htm)
[Get Coordinates of the Plane's Bounding Box (VBA)](Get_Coordinates_of_the_Plane's_Bounding_Box_Example_VB.htm)

## See Also

[IRefPlane Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html)
[IRefPlane Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane_members.html)
[IRefPlane::IGetBoundingBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane~IGetBoundingBox.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0

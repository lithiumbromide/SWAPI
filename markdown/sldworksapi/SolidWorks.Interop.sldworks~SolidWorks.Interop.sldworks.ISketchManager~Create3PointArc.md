---
title: "Create3PointArc Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "Create3PointArc"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~Create3PointArc.html"
---

# Create3PointArc Method (ISketchManager)

Creates a 3-point arc.

## Syntax

### Visual Basic (Declaration)

```vb
Function Create3PointArc( _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal Z1 As System.Double, _
   ByVal X2 As System.Double, _
   ByVal Y2 As System.Double, _
   ByVal Z2 As System.Double, _
   ByVal X3 As System.Double, _
   ByVal Y3 As System.Double, _
   ByVal Z3 As System.Double _
) As SketchSegment
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim X1 As System.Double
Dim Y1 As System.Double
Dim Z1 As System.Double
Dim X2 As System.Double
Dim Y2 As System.Double
Dim Z2 As System.Double
Dim X3 As System.Double
Dim Y3 As System.Double
Dim Z3 As System.Double
Dim value As SketchSegment

value = instance.Create3PointArc(X1, Y1, Z1, X2, Y2, Z2, X3, Y3, Z3)
```

### C#

```csharp
SketchSegment Create3PointArc(
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2,
   System.double X3,
   System.double Y3,
   System.double Z3
)
```

### C++/CLI

```cpp
SketchSegment^ Create3PointArc(
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2,
   System.double X3,
   System.double Y3,
   System.double Z3
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X1`: X coordinate of point 1
- `Y1`: Y coordinate of point 1
- `Z1`: Z coordinate of point 1
- `X2`: X coordinate of point 2
- `Y2`: Y coordinate of point 2
- `Z2`: Z coordinate of point 2
- `X3`: X coordinate of point 3
- `Y3`: Y coordinate of point 3
- `Z3`: Z coordinate of point 3

### Return Value

[Sketch segment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html) for the 3-point arc

## VBA Syntax

See [SketchManager::Create3PointArc](ms-its:sldworksapivb6.chm::/Sldworks~SketchManager~Create3PointArc.html).

## Examples

[Create 3-Point Arc (VBA)](Create_3_Point_Arc_Example_VB.htm)
[Create 3-Point Arc (VB.NET)](Create_3_Point_Arc_Example_VBNET.htm)
[Create 3-Point Arc (C#)](Create_3_Point_Arc_Example_CSharp.htm)

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)
[ISketchManager::CreateArc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateArc.html)
[ISketchManager::CreateTangentArc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateTangentArc.html)
[IModelDoc2::CreateArcByCenter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateArcByCenter.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0

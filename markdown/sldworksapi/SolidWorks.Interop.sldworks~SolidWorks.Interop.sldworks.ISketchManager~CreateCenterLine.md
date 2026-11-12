---
title: "CreateCenterLine Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "CreateCenterLine"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateCenterLine.html"
---

# CreateCenterLine Method (ISketchManager)

Creates a center line between the specified points.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateCenterLine( _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal Z1 As System.Double, _
   ByVal X2 As System.Double, _
   ByVal Y2 As System.Double, _
   ByVal Z2 As System.Double _
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
Dim value As SketchSegment

value = instance.CreateCenterLine(X1, Y1, Z1, X2, Y2, Z2)
```

### C#

```csharp
SketchSegment CreateCenterLine(
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2
)
```

### C++/CLI

```cpp
SketchSegment^ CreateCenterLine(
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X1`: X coordinate of first end point, in meters
- `Y1`: Y coordinate of first end point, in meters
- `Z1`: Z coordinate of first end point, in meters
- `X2`: X coordinate of second end point, in meters
- `Y2`: Y coordinate of second end point, in meters
- `Z2`: Z coordinate of second end point, in meters

### Return Value

[Sketch segment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html) for the center line

## VBA Syntax

See [SketchManager::CreateCenterLine](ms-its:sldworksapivb6.chm::/Sldworks~SketchManager~CreateCenterLine.html).

## Examples

[Create 3D Sketch Plane (C#)](Create_3D_Sketch_Plane_Example_CSharp.htm)
[Create 3D Sketch Plane (VB.NET)](Create_3D_Sketch_Plane_Example_VBNET.htm)
[Create 3D Sketch Plane (VBA)](Create_3D_Sketch_Plane_Example_VB.htm)

## Remarks

You can also create centerline construction geometry using [ISketchManager::CreateLine](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~CreateLine.html) and [ISketchSegment::ConstructionGeometry](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment~ConstructionGeometry.html).

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0

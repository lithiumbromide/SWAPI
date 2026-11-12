---
title: "CreateCornerRectangle Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "CreateCornerRectangle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateCornerRectangle.html"
---

# CreateCornerRectangle Method (ISketchManager)

Creates a corner rectangle.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateCornerRectangle( _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal Z1 As System.Double, _
   ByVal X2 As System.Double, _
   ByVal Y2 As System.Double, _
   ByVal Z2 As System.Double _
) As System.Object
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
Dim value As System.Object

value = instance.CreateCornerRectangle(X1, Y1, Z1, X2, Y2, Z2)
```

### C#

```csharp
System.object CreateCornerRectangle(
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
System.Object^ CreateCornerRectangle(
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

- `X1`: Upper-left X coordinate for point 1
- `Y1`: Upper-left Y coordinate for point 1
- `Z1`: Upper-left Z coordinate for point 1
- `X2`: Lower-right X coordinate for point 2
- `Y2`: Lower-right Y coordinate for point 2
- `Z2`: Lower-right Z coordinate for point 2

### Return Value

Array of [sketch segments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html) that represent the edges created for this corner rectangle

## VBA Syntax

See [SketchManager::CreateCornerRectangle](ms-its:sldworksapivb6.chm::/Sldworks~SketchManager~CreateCornerRectangle.html).

## Examples

[Create and Edit Circular Sketch Pattern (VB.NET)](Create_and_Edit_Circular_Sketch_Pattern_Example_VBNET.htm)
[Create and Edit Circular Sketch Pattern (VBA)](Create_and_Edit_Circular_Sketch_Pattern_Example_VB.htm)
[Create and Edit Circular Sketch Pattern (C#)](Create_and_Edit_Circular_Sketch_Pattern_Example_CSharp.htm)

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)
[ISketchManager::Create3PointCenterRectangle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~Create3PointCenterRectangle.html)
[ISketchManager::Create3PointCornerRectangle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~Create3PointCornerRectangle.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0

---
title: "IGetUserPoints2 Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "IGetUserPoints2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetUserPoints2.html"
---

# IGetUserPoints2 Method (ISketch)

Gets all of the user points in this sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetUserPoints2( _
   ByVal ArraySize As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim ArraySize As System.Integer
Dim value As System.Double

value = instance.IGetUserPoints2(ArraySize)
```

### C#

```csharp
System.double IGetUserPoints2(
   System.int ArraySize
)
```

### C++/CLI

```cpp
System.double IGetUserPoints2(
   System.int ArraySize
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ArraySize`: Number of user points in the sketch

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

The return value is an array of doubles with this format:

[ Color, Line Font, Line Width, Layer ID, Layer Override, ptLoc[3] ]

where:

- Color = COLORREF returned as an integer. Return value could be 0 or -1 for default color.
- Line Font = line style. Valid line styles can be found in the [swLineStyles_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineStyles_e.html) enumeration.
- Line Width = integer value defining the line width. Valid width values can be found in the [swLineWeights_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html) enumeration.
- Layer ID = integer value indicating which layer holds this entity. The [ILayer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayer.html) object can be obtained by passing this integer value to [ILayerMgr::GetLayerById](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr~GetLayerById.html) or [ILayerMgr::IGetLayerById](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr~IGetLayerById.html).
- Layer Override = integer with bit flags set to determine which properties, if any, have been overridden with respect to the Layer default properties. If the bit value is set, then the specific property or properties have been overridden. The bit indicators are: color = 0x1, style = 0x2, and width = 0x4. Therefore, if LayerOverride was returned as 3, you know the color and style have been specifically set for this item and may not match the default values associated with this item's layer.
- ptLoc[3] = an array of doubles (x, y, z) describing the point location

This set of data repeats for each user point in the sketch. The size of the array is (NumPts * 8). To determine the number of points in the sketch, use [ISketch::GetUserPointsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~GetUserPointsCount.html).

See [ISketch::GetSketchPoints2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~GetSketchPoints2.html), [ISketch::IGetSketchPoints2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~IGetSketchPoints2.html), or [ISketch::IEnumSketchPoints](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~IEnumSketchPoints.html) for access to individual [ISketchPoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint.html) objects.

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::GetUserPoints2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetUserPoints2.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0

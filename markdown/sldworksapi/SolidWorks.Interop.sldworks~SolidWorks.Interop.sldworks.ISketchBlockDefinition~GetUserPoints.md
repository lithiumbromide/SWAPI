---
title: "GetUserPoints Method (ISketchBlockDefinition)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockDefinition"
member: "GetUserPoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetUserPoints.html"
---

# GetUserPoints Method (ISketchBlockDefinition)

Gets information about all of the user points in this block definition.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUserPoints() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockDefinition
Dim value As System.Object

value = instance.GetUserPoints()
```

### C#

```csharp
System.object GetUserPoints()
```

### C++/CLI

```cpp
System.Object^ GetUserPoints();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [SketchBlockDefinition::GetUserPoints](ms-its:sldworksapivb6.chm::/sldworks~SketchBlockDefinition~GetUserPoints.html).

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

This set of data repeats for each user point in the sketch. The size of the array is (NumPts * 8).

## See Also

[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.html)
[ISketchBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition_members.html)
[ISketchBlockDefinition::GetUserPointsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetUserPointsCount.html)
[ISketchBlockDefinition::IGetUserPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetUserPoints.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0

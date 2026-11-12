---
title: "IGetSplines2 Method (ISketchBlockDefinition)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockDefinition"
member: "IGetSplines2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetSplines2.html"
---

# IGetSplines2 Method (ISketchBlockDefinition)

Gets the spline points by tessellation instead of by interpolation as is done by [ISketchBlockDefinition::GetSplinesInterpolate](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~GetSplinesInterpolate.html) and [ISketchBlockDefinition::IGetSplinesInterpolate](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~IGetSplinesInterpolate.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSplines2( _
   ByVal ArraySize As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockDefinition
Dim ArraySize As System.Integer
Dim value As System.Double

value = instance.IGetSplines2(ArraySize)
```

### C#

```csharp
System.double IGetSplines2(
   System.int ArraySize
)
```

### C++/CLI

```cpp
System.double IGetSplines2(
   System.int ArraySize
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ArraySize`: Number of splines

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [ISketchBlockDefinition::GetSplineCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~GetSplineCount.html) before calling this method to get the value for ArraySize.

Format of return values is an array of doubles with the format:

[ [ Color, LineType, LineStyleIndex, LineWidth, LayerID, LayerOverride, NumSplinePoints, [x,y,z] ] ]

where:

- Color = COLORREF returned as an integer. Return value could be 0 or -1 for default color.
- LineType = line type. Valid returns as defined in [swLineTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html). A lineType is a combination of a lineStyle and lineWeight.
- LineStyleIndex = line style. Valid line styles as defined in [swLineStyles_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineStyles_e.html).
- LineWidth = integer value defining the line width. Valid width values as defined in [swLineWeights_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html).
- LayerID = integer value indicating which layer holds this entity. Obtain the [ILayer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayer.html) object by passing this integer value to [ILayerMgr::GetLayerById](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr~GetLayerById.html) or [ILayerMgr::IGetLayerById](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr~IGetLayerById.html).
- LayerOverride = integer with bit flags set to determine which properties, if any, have been overridden with respect to the Layer default properties.

  If the bit value is set, then the specific property or properties have been overridden. The bit indicators are: color = 0x1, style = 0x2, and width = 0x4. Therefore, if LayerOverride was returned as 3, you know the color and style have been specifically set for this item and may not match the default values associated with this item's layer.

This complete set of data repeats itself for each spline found in the sketch block definition. For each spline, the array returned contains the color, line type, number of spline points in the spline, and X,Y,Z value for each of those points. Therefore, the [x,y,z] parameter is an array of NumSplinePoints, which can vary in size from spline to spline.

The [x,y,z] points for each spline are not the same as the points used to generate the spline. This method tessellates the spline based on the display quality and place points along the spline appropriately.

## See Also

[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.html)
[ISketchBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition_members.html)
[ISketchBlockDefinition::GetSplines2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplines2.html)
[ISketchBlockDefinition::GetSplineInterpolateCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplineInterpolateCount.html)
[ISketchBlockDefinition::GetSplineParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplineParams.html)
[ISketchBlockDefinition::GetSplineParamsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplineParamsCount.html)
[ISketchBlockDefinition::IGetSplineParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetSplineParams.html)

## Availability

SOLIDWORKS 2007 SP2, Revision Number 15.2

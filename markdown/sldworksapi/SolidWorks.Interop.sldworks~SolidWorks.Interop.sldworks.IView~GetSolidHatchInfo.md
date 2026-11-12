---
title: "GetSolidHatchInfo Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetSolidHatchInfo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSolidHatchInfo.html"
---

# GetSolidHatchInfo Method (IView)

Gets the boundary data for all visible solid-fill hatches in a detail, break, or crop view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSolidHatchInfo() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetSolidHatchInfo()
```

### C#

```csharp
System.object GetSolidHatchInfo()
```

### C++/CLI

```cpp
System.Object^ GetSolidHatchInfo();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [View::GetSolidHatchInfo](ms-its:sldworksapivb6.chm::/sldworks~View~GetSolidHatchInfo.html).

## Examples

[Get Solid-fill Hatch Information (VB.NET)](Get_Solid-fill_Hatch_Information_Example_VBNET.htm)
[Get Solid-fill Hatch Information (VBA)](Get_Solid-fill_Hatch_Information_Example_VB6.htm)
[Get Solid-fill Hatch Information (C#)](Get_Solid-fill_Hatch_Information_Example_CSharp.htm)

## Remarks

The return value, which is an array of doubles, describes the geometry for each boundary loop in each visible solid-fill hatch in a detail or broken view. The first two array elements indicate:

- [0] 1 if the loop is an outer loop, which is the first loop in the boundary, or 0 if the loop is an inner loop in the boundary
- [1] Number of polylines in the loop

The remaining array elements describe the polyline data and include information about these types of boundary segments:

- arcs: Returned using a center point, radius, and start and stop location
- ellipses: Returned as equation parameters
- splines: Returned as equation parameters
- straight lines: Returned as tessellated polylines

The format of the remaining array elements ([2], [3] ...) of polyline data is as follows:

[ Type, GeomDataSize, GeomData[ ], LineColor, LineStyle, LineFont, LineWeight, LayerID, LayerOverride, NumPolyPoints, [x,y,z] ]

where:

Type = underlying geometry type, possible values are:

- 0 = Polyline type
- 1 = Arc or Circle type

GeomDataSize = number of elements in the GeomData array, for Type = 0 this will be 0.

GeomData[ ] = geometric data that can be used to represent the underlying geometry type. The data returned in this array is based on the underlying geometry type:

- Type = 0. This array is empty
- Type = 1. [ centerPtX, centerPtY, centerPtZ, startPtX, startPtY, startPtZ, endPtX, endPtY, endPtZ, normalX, normalY, normalZ ]

LineColor = polyline color. This value is determined either by the explicitly set value or by the layer that the polyline is on.

LineStyle = value combines polyline font and weight information. This value can be used as an input to GetLineFontInfo and GetLineFontName. If this value is -1, then the user has probably modified the line display manually in the drawing and you should use the LineFont and LineWeight return values to recreate the exact polyline style.

LineFont = value is used for polyline font information. This value can be used as an input to the GetLineFontInfo2 and GetLineFontName2 functions. This value will only be valid if LineStyle is -1.

LineWeight = polyline weight where Thin = 0.0, Normal = 1.0, Thick = 2.0. This value will only be valid if LineStyle is -1.

LayerID = integer value indicating which layer holds this polyline. The [ILayer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayer.html) object can be obtained by passing this integer value to [ILayerMgr::GetLayerById](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr~GetLayerById.html) and [ILayerMgr::IGetLayerById](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr~IGetLayerById.html).

LayerOverride = integer with bit flags set to determine which properties, if any, have been overridden with respect to the Layer default properties. If the bit value is set, then the specific property or properties have been overridden. The bit indicators are: color = 0x1, style = 0x2, and width = 0x4. Therefore, if LayerOverride was returned as 3, you know the color and style have been specifically set for this item and may not match the default values associated with this item's layer.

NumPolyPoints = number of XYZ points found in the [x,y,z] return value.

[x,y,z] = array of points used to describe the polyline. This array has NumPolyPoints points. This data will be returned for every polyline regardless of Type.

To get information about solid-fill hatches in drawing views, use [IView::GetFaceHatchCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFaceHatchCount.html), [IView::GetFaceHatches](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFaceHatches.html), and [IView::IGetFaceHatches](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetFaceHatches.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::IGetSolidHatchInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSolidHatchInfo.html)
[IView::GetSolidHatchCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSolidHatchCount.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

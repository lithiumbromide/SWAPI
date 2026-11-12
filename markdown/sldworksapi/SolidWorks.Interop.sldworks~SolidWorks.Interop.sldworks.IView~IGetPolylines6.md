---
title: "IGetPolylines6 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetPolylines6"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetPolylines6.html"
---

# IGetPolylines6 Method (IView)

Obsolete. Superseded by [IView::IGetPolylines7](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetPolylines7.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetPolylines6( _
   ByVal CrossHatchOption As System.Short, _
   ByVal ArraySize As System.Integer, _
   ByRef Polylines As System.Double, _
   ByVal EdgeArraySize As System.Integer _
) As Edge
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim CrossHatchOption As System.Short
Dim ArraySize As System.Integer
Dim Polylines As System.Double
Dim EdgeArraySize As System.Integer
Dim value As Edge

value = instance.IGetPolylines6(CrossHatchOption, ArraySize, Polylines, EdgeArraySize)
```

### C#

```csharp
Edge IGetPolylines6(
   System.short CrossHatchOption,
   System.int ArraySize,
   out System.double Polylines,
   System.int EdgeArraySize
)
```

### C++/CLI

```cpp
Edge^ IGetPolylines6(
   System.short CrossHatchOption,
   System.int ArraySize,
   [Out] System.double Polylines,
   System.int EdgeArraySize
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CrossHatchOption`: 0 = include crosshatch lines

  1 = exclude crosshatch lines

  2 = include only crosshatch lines
- `ArraySize`: Size of array of lines
- `Polylines`: Array of doubles representing the lines in the view (see **Remarks**)
- `EdgeArraySize`: Size of array of modeling edges

### Return Value

Array of modeling [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) corresponding to the polylines in the view

## VBA Syntax

See [View::IGetPolylines6](ms-its:sldworksapivb6.chm::/sldworks~View~IGetPolylines6.html).

## Remarks

The difference between this method and [IView::GetPolyLinesAndCurves](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetPolyLinesAndCurves.html) and [IView::IGetPolyLinesAndCurves](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetPolyLinesAndCurves.html) is that splines and ellipses returned by these methods are returned as equation parameters, which are more precise definitions.

This method returns data for all visible solid model edges in the drawing view. This includes these types of edges:

- arcs: Returned using a center point, radius, and start and stop location.
- circles: Returned using a center point, radius, and start and stop location.
- ellipses: Returned as tessellated polylines.
- splines: Returned as tessellated polylines.
- straight lines: Returned as tessellated polylines, but because the edges are straight, there is no loss of data in the approximation.

NOTE: If the view contains silhouette edges, then the polylines that render them cannot correspond to an edge because an edge does not actually exist. For example, if the third and fourth polyline in the set of polylines returned describe a silhouette edge, then array positions 4 and 5 in the edge array will be null.

This method also lets you include or exclude crosshatch lines. This method does not return data for sketch segments added by a user in the drawing view.

| To get... | Call... |
| --- | --- |
| Size of array needed to hold this data | IView::GetPolylineCount5 |
| Items that were sketched in this drawing view | IView::GetArcs4 and IView::IGetArcs4 IView::GetLines4 and IView::IGetLines4 IView::GetSplines3 and IView::IGetSplines3 IView::GetEllipses5 and IView::IGetEllipses5 |

Format of the return value is the following array of doubles:

[ Type, GeomDataSize, GeomData[ ], LineColor, LineStyle, LineFont, LineWeight, LayerID, LayerOverride, NumPolyPoints, [x,y,z] ]

where:

Type = underlying geometry type, possible values are:

GeomDataSize = number of elements in the GeomData array, for Type = 0 this will be 0.

GeomData[ ] = geometric data that can be used to represent the underlying geometry type. The data returned in this array is based on the underlying geometry type:

LineColor = polyline color. This value is determined either by the explicitly set value or by the layer that the polyline is on.

LineStyle = value combines polyline font and weight information. This value can be used as an input to GetLineFontInfo and GetLineFontName. If this value is -1, then the user has probably modified the line display manually in the drawing and you should use the LineFont and LineWeight return values to recreate the exact polyline style.

LineFont = value is used for polyline font information. This value can be used as an input to the GetLineFontInfo2 and GetLineFontName2 functions. This value will only be valid if LineStyle is -1.

LineWeight = polyline weight where Thin = 0.0, Normal = 1.0, Thick = 2.0. This value will only be valid if LineStyle is -1.

LayerID = integer value indicating which layer holds this polyline. The [ILayer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayer.html) object can be obtained by passing this integer value to [ILayerMgr::GetLayerById](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr~GetLayerById.html) and [ILayerMgr::IGetLayerById](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr~IGetLayerById.html).

LayerOverride = integer with bit flags set to determine which properties, if any, have been overridden with respect to the Layer default properties. If the bit value is set, then the specific property or properties have been overridden. The bit indicators are: color = 0x1, style = 0x2, and width = 0x4. Therefore, if LayerOverride was returned as 3, you know the color and style have been specifically set for this item and may not match the default values associated with this item's layer.

NumPolyPoints = number of XYZ points found in the [x,y,z] return value

[x,y,z] = array of points used to describe the polyline. This array has NumPolyPoints points. This data will be returned for every polyline regardless of Type.

| If... | Then... |
| --- | --- |
| Display mode of the view is: Shaded Shaded with Edges Draft Quality Fast HLR/HLV | A value is not returned. Use IView::SetDisplayMode3 to change Shaded or Shaded with Edges mode to Wireframe, Hidden Lines Removed (HLR), or Hidden Lines Visible (HLV), and then get the polylines. |
| Changes are made to the parts or assemblies shown in this drawing | Polylines are only generated that are in the visible viewing bounds when the drawing is opened. |
| Drawing is already open | All polylines in the drawing are generated. If you open a drawing that is zoomed in to a particular region, then the polylines that are outside the zoomed region do not exist if the parts or assemblies shown in this drawing have been changed. To force the generation of all possible polyline data, call IModelDoc2::ViewZoomtofit2 . |

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetDisplayMode2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayMode2.html)
[IView::GetPolylines6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetPolylines6.html)
[IView::GetPolyLinesAndCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetPolyLinesAndCurves.html)
[IView::IGetPolyLinesAndCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetPolyLinesAndCurves.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0

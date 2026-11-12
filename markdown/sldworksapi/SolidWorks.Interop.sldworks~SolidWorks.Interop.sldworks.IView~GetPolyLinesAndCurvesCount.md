---
title: "GetPolyLinesAndCurvesCount Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetPolyLinesAndCurvesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetPolyLinesAndCurvesCount.html"
---

# GetPolyLinesAndCurvesCount Method (IView)

Gets the number of lines, including arcs, ellipses, splines, and polylines, in the view with the option to include or exclude cross hatch lines.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPolyLinesAndCurvesCount( _
   ByVal CrossHatchOption As System.Short, _
   ByRef PointCount As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim CrossHatchOption As System.Short
Dim PointCount As System.Integer
Dim value As System.Integer

value = instance.GetPolyLinesAndCurvesCount(CrossHatchOption, PointCount)
```

### C#

```csharp
System.int GetPolyLinesAndCurvesCount(
   System.short CrossHatchOption,
   out System.int PointCount
)
```

### C++/CLI

```cpp
System.int GetPolyLinesAndCurvesCount(
   System.short CrossHatchOption,
   [Out] System.int PointCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CrossHatchOption`: Crosshatch option as defined in [swCrossHatchFilter_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCrossHatchFilter_e.html)
- `PointCount`: Size of array to allocate in doubles for [IView::IGetPolyLinesAndCurves](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetPolyLinesAndCurves.html)

### Return Value

Number of lines

## VBA Syntax

See [View::GetPolyLinesAndCurvesCount](ms-its:sldworksapivb6.chm::/sldworks~View~GetPolyLinesAndCurvesCount.html).

## Remarks

Call this method before calling [IView::IGetPolyLinesAndCurves](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetPolyLinesAndCurves.html).

| If... | Then... |
| --- | --- |
| Drawing view is in any of these modes: Shaded mode Shaded with edges mode Draft quality | This method returns 0. Use IView::SetDisplayMode3 to change Shaded or Shaded with edges mode to Wireframe, Hidden Lines Removed (HLR), or Hidden Lines Visible (HLV), and then get the number of polylines. |
| Changes are made to the parts or assemblies shown in this drawing | Polylines are only generated that are in the visible viewing bounds when the drawing is opened. |
| Drawing is already open | All polylines in the drawing are generated. If you open a drawing that is zoomed in to a particular region, then the polylines that are outside the zoomed region do not exist if the parts or assemblies shown in this drawing have been changed. To force the generation of all possible polyline data, call IModelDoc2::ViewZoomtofit2 . |

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetDisplayMode2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayMode2.html)
[IView::GetPolyLineCount5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetPolyLineCount5.html)
[IView::GetPolylines6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetPolylines6.html)
[IView::GetPolyLinesAndCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetPolyLinesAndCurves.html)
[IView::IGetPolylines6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetPolylines6.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0

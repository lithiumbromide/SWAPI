---
title: "GetPolyLineCount5 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetPolyLineCount5"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetPolyLineCount5.html"
---

# GetPolyLineCount5 Method (IView)

Gets the number of polylines in this view with an option to include or exclude crosshatch lines.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPolyLineCount5( _
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

value = instance.GetPolyLineCount5(CrossHatchOption, PointCount)
```

### C#

```csharp
System.int GetPolyLineCount5(
   System.short CrossHatchOption,
   out System.int PointCount
)
```

### C++/CLI

```cpp
System.int GetPolyLineCount5(
   System.short CrossHatchOption,
   [Out] System.int PointCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CrossHatchOption`: Crosshatch option as defined in [swCrossHatchFilter_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCrossHatchFilter_e.html)
- `PointCount`: Size of array needed to allocate in doubles for [IView::IGetPolylines6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetPolylines6.html)

### Return Value

Number of polylines

## VBA Syntax

See [View::GetPolyLineCount5](ms-its:sldworksapivb6.chm::/sldworks~View~GetPolyLineCount5.html).

## Examples

[Get Number of Polylines in Shaded Mode Drawing View (VBA)](Get_Number_of_Polylines_in_Shaded_Mode_Drawing_View_Example_VB.htm)

## Remarks

Call this method before calling [IView::IGetPolylines6.](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetPolylines6.html)

| If... | Then... |
| --- | --- |
| Drawing view is in any of these modes: Shaded mode Shaded with edges mode Draft quality | This method returns 0. Use IView::SetDisplayMode3 to change Shaded or Shaded with edges mode to Wireframe, Hidden Lines Removed (HLR), or Hidden Lines Visible (HLV), and then get the number of polylines. |
| Changes are made to the parts or assemblies shown in this drawing | Polylines are only generated that are in the visible viewing bounds when the drawing is opened. |
| Drawing is already open | All polylines in the drawing are generated. If you open a drawing that is zoomed in to a particular region, then the polylines that are outside the zoomed region do not exist if the parts or assemblies shown in this drawing have been changed. To force the generation of all possible polyline data, call IModelDoc2::ViewZoomtofit2 . |

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetDisplayMode2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayMode2.html)
[IView::GetPolylines6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetPolylines6.html)
[IView::GetPolyLinesAndCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetPolyLinesAndCurves.html)
[IView::GetPolyLinesAndCurvesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetPolyLinesAndCurvesCount.html)
[IView::IGetPolyLinesAndCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetPolyLinesAndCurves.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0

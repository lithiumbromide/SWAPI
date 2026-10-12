---
title: "IGetEllipses5 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetEllipses5"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetEllipses5.html"
---

# IGetEllipses5 Method (IView)

Gets all of the ellipses added by a user in this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetEllipses5() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Double

value = instance.IGetEllipses5()
```

### C#

```csharp
System.double IGetEllipses5()
```

### C++/CLI

```cpp
System.double IGetEllipses5();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (**Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

This method only returns ellipses that were sketched by a user in this drawing view. Use [IView::GetPolylines6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetPolylines6.html) or [IView::GetPolylines6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetPolylines6.html) to access the solid model's projected display data in the drawing view.

All part and assembly geometry shown in a drawing view is represented by polylines. To access the polylines, use View::GetPolylines3.

The return values are in an array of doubles:

[ Color, LineType, LineStyleIndex, LineWidth, LayerID, LayerOverride, StartPt[3], EndPt[3], CenterPt[3], MajorPt[3], MinorPt[3], Direction ... ]

where:

Color = COLORREF returned as an integer. Return value can be 0 or -1 for default color.

LineType = line type. Valid returns as defined in [swLineTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html). A lineType is a combination of a lineStyle and lineWeight.

LineStyleIndex = line style. Valid line styles as defined in [swLineStyles_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineStyles_e.html).

LineWidth = integer value defining the line width. Valid width values as defined in [swLineWeights_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html).

LayerID = integer value indicating that layer holds this entity. The [ILayer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayer.html) object can be obtained by passing this integer value to [ILayerMgr::GetLayerById](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr~GetLayerById.html) or [ILayerMgr::IGetLayerById](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr~IGetLayerById.html).

LayerOverride = integer with bit flags set to determine which properties, if any, have been overridden with respect to the Layer default properties. If the bit value is set, then the specific property or properties have been overridden. The bit indicators are: color = 0x1, style = 0x2, and width = 0x4. Therefore, if LayerOverride is returned as 3, you know the color and style have been specifically set for this item and may not match the default values associated with this item's layer.

StartPt[3] = array of 3 doubles (X,Y,Z) describing the ellipse start point.

EndPt[3] = array of 3 doubles (X,Y,Z) describing the ellipse end point. If the ellipse is closed, then this will be the same point as the StartPt.

CenterPt[3] = array of 3 doubles (X,Y,Z) describing the ellipse center point.

MajorPt[3] = array of 3 doubles (X,Y,Z) describing a point on the ellipse and on the major axis.

MinorPt[3] = array of 3 doubles (X,Y,Z) describing a point on the ellipse and on the minor axis.

Direction = -1 for clockwise, +1 for counterclockwise.

This set of data repeats for each ellipse in the view. The size of the array is (NumEllipses * 22). To determine the number of ellipses, use [IView::GetEllipseCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetEllipseCount.html).

The data returned from this method is in terms of view space. If you want the data in terms of sheet space (for example, the 0,0 origin being the lower-left corner of the sheet), then combine this data with the three return values from [IView::GetXForm](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetXform.html) or [IView::IGetXForm](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetXform.html).

The sheet must be visible. See [ISheet::SheetFormatVisible](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheet~SheetFormatVisible.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetEllipses5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetEllipses5.html)

## Availability

SOLIDWORKS 99, datecode 1999207

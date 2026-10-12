---
title: "GetArcs4 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetArcs4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetArcs4.html"
---

# GetArcs4 Method (IView)

Gets all of the information for all of the arcs added by a user in this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetArcs4() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetArcs4()
```

### C#

```csharp
System.object GetArcs4()
```

### C++/CLI

```cpp
System.Object^ GetArcs4();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of doubles (see Remarks)

## VBA Syntax

See [View::GetArcs4](ms-its:sldworksapivb6.chm::/sldworks~View~GetArcs4.html).

## Remarks

This method only returns arcs that were sketched by a user in a drawing view. Use [IView::GetPolylines6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetPolylines6.html) or [IView::IGetPolylines6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetPolylines6.html) to access the solid model's projected display data in the drawing view.

Return value is an array of doubles with the format:

[ Color, LineType, LineStyleIndex, LineWidth, LayerID, LayerOverride, StartPt[3], EndPt[3], CenterPt[3], RotDir, ... ]

where:

- Color - COLORREF returned as an integer. Return value could be 0 or -1 for default color.
- LineType - Line type. Valid returns as defined in [swLineTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html). A `LineType` is a combination of a line style and line weight.
- LineStyleIndex - Line style. Valid line styles as defined in [swLineStyles_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineStyles_e.html) enumeration.
- LineWidth - Integer value defining the line width. Valid width values as defined in [swLineWeights_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html).
- LayerID - Integer value indicating which layer holds this entity. The [ILayer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayer.html) object can be obtained by passing this integer value to [ILayerMgr::GetLayerById](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr~IGetLayerById.html) or [ILayerMgr::IGetLayerById](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr~IGetLayerById.html).
- LayerOverride - Integer with bit flags set to determine which properties, if any, have been overridden with respect to the Layer default properties. If the bit value is set, then the specific property or properties have been overridden. The bit indicators are: color = 0x1, style = 0x2, and width = 0x4. Therefore, if `LayerOverride` was returned as 3, the color and style have been specifically set for this item and may not match the default values associated with this item's layer.
- StartPt[3] - An array of 3 doubles (X,Y,Z) describing the start point.
- EndPt[3] - An array of 3 doubles (X,Y,Z) describing the end point. If the arc is closed, then EndPt[3] is the same point as the StartPt.
- CenterPt[3] - An array of 3 doubles (X,Y,Z) describing the center point.
- RotDir - Rotational direction (CW = -1, CCW = 1)

...

This set of data repeats for each arc in the view. The size of the array is (NumArcs * 16). To determine the number of arcs, use [IView::GetArcCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetArcCount.html).

The data returned from this method is in terms of view space. If you want the data in terms of sheet space (for example, the 0,0 origin being the lower-left corner of the sheet), then you should combine this data with the three return values from [IView::GetXForm](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetXform.html) or [IView::IGetXForm](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetViewXform.html).

The sheet must be visible. See [ISheet::SheetFormatVisible](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheet~SheetFormatVisible.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::IGetArcs4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetArcs4.html)

## Availability

SOLIDWORKS 99, datecode 1999207

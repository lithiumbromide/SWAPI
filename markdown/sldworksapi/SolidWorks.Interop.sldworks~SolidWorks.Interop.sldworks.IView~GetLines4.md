---
title: "GetLines4 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetLines4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetLines4.html"
---

# GetLines4 Method (IView)

Gets all of the lines in the view with an option to include or exclude crosshatch lines.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLines4( _
   ByVal CrossHatchOption As System.Short _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim CrossHatchOption As System.Short
Dim value As System.Object

value = instance.GetLines4(CrossHatchOption)
```

### C#

```csharp
System.object GetLines4(
   System.short CrossHatchOption
)
```

### C++/CLI

```cpp
System.Object^ GetLines4(
   System.short CrossHatchOption
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CrossHatchOption`: Crosshatch option as defined in [swCrossHatchFilter_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCrossHatchFilter_e.html)

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [View::GetLines4](ms-its:sldworksapivb6.chm::/sldworks~View~GetLines4.html).

## Examples

[Get Polylines Information (VBA)](Get_Polylines_Information_Example_VB.htm)

## Remarks

This method only returns lines that were sketched in this drawing view. Use [IView::GetPolylines6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetPolylines6.html) or [IView::IGetPolylines6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetPolylines6.html) to access the solid model's projected display data in this view.

The return value is the following array of doubles:

[ Color, LineType, LineStyleIndex, LineWidth, LayerID, LayerOverride, StartPt[3], EndPt[3], ... ]

where all data values are returned as doubles:

- Color = COLORREF returned as an integer. Return value could be 0 or -1 for default color.
- LineType = line type. Valid returns as defined in [swLineTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html). A lineType is a combination of a lineStyle and lineWeight.
- LineStyleIndex = line style. Valid line styles as defined in [swLineStyles_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineStyles_e.html).
- LineWidth = integer value defining the line width. Valid width values as defined in [swLineWeights_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html).
- LayerID = integer value indicating which layer holds this entity. Obtain the [ILayer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayer.html) object by passing this integer value to [ILayerMgr::GetLayerById](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr~GetLayerById.html) or [ILayerMgr::IGetLayerById](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr~IGetLayerById.html).
- LayerOverride = integer with bit flags set to determine which properties, if any, have been overridden with respect to the Layer default properties. If the bit value is set, then the specific property or properties have been overridden. The bit indicators are: color = 0x1, style = 0x2, and width = 0x4. Therefore, if LayerOverride is returned as 3, you know the color and style have been specifically set for this item and may not match the default values associated with this item's layer.
- StartPt[3] = array of 3 doubles (X,Y,Z) describing the line start point.
- EndPt[3] = array of 3 doubles (X,Y,Z) describing the line end point.

This set of data repeats for each line in the view. The number of doubles returned is (lineCount * 12). To determine the number of lines in the view, use [IView::GetLineCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetLineCount2.html).

The data returned from this method is in terms of view space. If you want the data in terms of sheet space (that is, the 0,0 origin being the lower-left corner of the sheet), then combine this data with the three return values from [IView::GetXForm](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetXform.html) or [IView::IGetXForm](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetXform.html).

The sheet must be visible. See [ISheet::SheetFormatVisible](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheet~SheetFormatVisible.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::IGetLines4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetLines4.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0

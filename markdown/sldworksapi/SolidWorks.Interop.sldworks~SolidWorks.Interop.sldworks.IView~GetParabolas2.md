---
title: "GetParabolas2 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetParabolas2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetParabolas2.html"
---

# GetParabolas2 Method (IView)

Gets all of the information about all of the parabolas in this view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetParabolas2() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetParabolas2()
```

### C#

```csharp
System.object GetParabolas2()
```

### C++/CLI

```cpp
System.Object^ GetParabolas2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [View::GetParabolas2](ms-its:sldworksapivb6.chm::/sldworks~View~GetParabolas2.html).

## Remarks

The return values are in an array of doubles:

[ Color, LineType, LineFont, LineWidth, LayerID, LayerOverride, StartPt[3], EndPt[3], FocusPt[3], ApexPt[3] ]

where:

Color = COLORREF returned as an integer. Return value could be 0 or -1 for default color.

LineType = line type. Valid returns as defined in [swLineTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html). A LineType is a combination of a LineStyle and LineWeight.

LineFont = Value is used for polyline font information.

LineWidth = integer value defining the line width. Valid width values as defined in [swLineWeights_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html).

LayerID = integer value indicating which layer holds this entity. Obtain the [ILayer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayer.html) object by passing this integer value to [ILayerMgr::GetLayerById](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr~GetLayerById.html) or [ILayerMgr::IGetLayerById](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr~IGetLayerById.html).

LayerOverride = integer with bit flags set to determine which properties, if any, have been overridden with respect to the Layer default properties. If the bit value is set, then the specific property or properties have been overridden. The bit indicators are: color = 0x1, style = 0x2, and width = 0x4. Therefore, if LayerOverride was returned as 3, you know the color and style have been specifically set for this item and may not match the default values associated with this item's layer.

StartPt[3] = array of 3 doubles (X,Y,Z) describing the parabola start point.

EndPt[3] = array of 3 doubles (X,Y,Z) describing the parabola end point.

FocusPt[3] = array of 3 doubles (X,Y,Z) describing the parabola focus point.

ApexPt[3] = array of 3 doubles (X,Y,Z) describing the parabola apex point.

This set of data repeats for each parabola in the view. The size of the array is (NumParabolas * 18). To determine the number of parabolas, use [IView::GetParabolaCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetParabolaCount.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::IGetParabolas2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetParabolas2.html)

## Availability

SOLIDWORKS 99, datecode 1999207

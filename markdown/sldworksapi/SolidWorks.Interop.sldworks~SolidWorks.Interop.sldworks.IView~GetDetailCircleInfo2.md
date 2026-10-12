---
title: "GetDetailCircleInfo2 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetDetailCircleInfo2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDetailCircleInfo2.html"
---

# GetDetailCircleInfo2 Method (IView)

Gets all of the information about each detail circle in the view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDetailCircleInfo2() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetDetailCircleInfo2()
```

### C#

```csharp
System.object GetDetailCircleInfo2()
```

### C++/CLI

```cpp
System.Object^ GetDetailCircleInfo2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [View::GetDetailCircleInfo2](ms-its:sldworksapivb6.chm::/sldworks~View~GetDetailCircleInfo2.html).

## Examples

[Get Detail Circle Information (VBA)](Get_Detail_Circle_Information_Example_VB.htm)

## Remarks

The return value is the following array of doubles:

[ numDetailCircles, [ layer, centerPt[3], startPt[3], endPt[3], lineType, textPt[3], textHeight, numArrows, [ arrowTip[3], arrowComponent[3], arrowWidth, arrowHeight, arrowStyle ] ] ]

where:

numDetailCircles = the number of detail circles in this view. See also [IView::GetDetailCircleCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetDetailCircleCount2.html).

The following set of data repeats itself for each detail circle in the view. The number of times the following information is given is numDetailCircles:

layer = integer value indicating which layer holds this entity. Obtain the [ILayer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayer.html) object by passing this integer value to [ILayerMgr::GetLayerById](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr~GetLayerById.html) or [ILayerMgr::IGetLayerById](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr~IGetLayerById.html).

centerPt[3] = X,Y,Z center point for this detail circle

startPt[3] = X,Y,Z start point for this detail circle

endPt[3] = X,Y,Z end point for this detail circle

lineType = line type for this detail circle as defined in [swLineTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html)

textPt[3] = X,Y,Z point for the text location.

textHeight = text height in meters

numArrows = number of arrows for this detail circle.

The following set of data repeats itself for each arrow in the current detail circle. The number of times the following information is given is numArrows:

arrowTip[3] = X,Y,Z start point for this arrow head

arrowComponent[3] = X,Y,Z component for this arrow head

arrowWidth = width of this arrow head

arrowHeight = height of this arrow head

arrowStyle = style of this arrow head as defined in [swArrowStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html)

To get the actual text value, see [IView::GetDetailCircleStrings](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetDetailCircleStrings.html) or [IView::IGetDetailCircleStrings](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetDetailCircleStrings.html).

The number of line segments, line segment geometry, and line type returned depend on the drawing's display standard.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetDetail Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDetail.html)
[IView::GetDetailCircles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDetailCircles.html)
[IView::IGetDetail Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDetail.html)
[IView::IGetDetailCircleInfo2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDetailCircleInfo2.html)
[IView::IGetDetailCircles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDetailCircles.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0

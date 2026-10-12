---
title: "IGetDatumPoints2 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetDatumPoints2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDatumPoints2.html"
---

# IGetDatumPoints2 Method (IView)

Gets all of the information about all the datum points in this view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetDatumPoints2() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Double

value = instance.IGetDatumPoints2()
```

### C#

```csharp
System.double IGetDatumPoints2()
```

### C++/CLI

```cpp
System.double IGetDatumPoints2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Return value is an array of doubles with the format:

[ Color, LineStyleIndex, LineWidth, LayerID, LayerOverride, ptLoc[3] ... ]

Color = COLORREF returned as an integer. Return value can be 0 or -1 for default color.

LineStyleIndex = line style. Valid line styles as defined in [swLineStyles_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html).

LineWidth = integer value defining the line width. Valid width values as defined in [swLineWeights_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html).

LayerID = integer value indicating which layer holds this entity. This integer value is the array index value into the layerList array. The layerList array can be obtained using [ILayerMgr::GetLayerList](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr~GetLayerList.html) or [ILayerMgr::IGetLayerList](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr~IGetLayerList.html). A value of 1 indicates that this item is not on a layer.

LayerOverride = integer with bit flags set to determine which properties, if any, have been overridden with respect to the [ILayer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayer.html) default properties. If the bit value is set, then the specific property or properties have been overridden. The bit indicators are: color = 0x1, style = 0x2, and width = 0x4. Therefore, if LayerOverride is returned as 3, you know the color and style have been specifically set for this item and may not match the default values associated with this item's layer.

ptLoc[3] = array of 3 doubles (X,Y,Z) describing the point location

...

This entire set of data repeats for each datum point in the view. The size of the array is (NumPts * 8). To determine the number of points,use [IView::GetDatumPointsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetDatumPointsCount.html).

The data returned from this method is in terms of view space. If you want the data in terms of sheet space (for example, the 0,0 origin being the lower-left corner of the sheet), then combine this data with the three return values from [IView::GetXForm](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetXform.html) or [IView::IGetXForm](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetXform.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetDatumPoints2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDatumPoints2.html)

## Availability

SOLIDWORKS 99, datecode 1999207

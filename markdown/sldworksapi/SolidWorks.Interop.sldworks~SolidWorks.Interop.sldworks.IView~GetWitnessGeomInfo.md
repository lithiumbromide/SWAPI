---
title: "GetWitnessGeomInfo Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetWitnessGeomInfo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetWitnessGeomInfo.html"
---

# GetWitnessGeomInfo Method (IView)

Gets the geometry data for all of the virtual sharp witness lines in this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetWitnessGeomInfo() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetWitnessGeomInfo()
```

### C#

```csharp
System.object GetWitnessGeomInfo()
```

### C++/CLI

```cpp
System.Object^ GetWitnessGeomInfo();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [View::GetWitnessGeomInfo](ms-its:sldworksapivb6.chm::/sldworks~View~GetWitnessGeomInfo.html).

## Examples

[Get Virtual Sharp Witness Line Data (C#)](Get_Virtual_Sharp_Witness_Line_Data_Example_CSharp.htm)
[Get Virtual Sharp Witness Line Data (VB.NET)](Get_Virtual_Sharp_Witness_Line_Data_Example_VBNET.htm)
[Get Virtual Sharp Witness Line Data (VBA)](Get_Virtual_Sharp_Witness_Line_Data_Example_VB.htm)

## Remarks

This method returns an array containing the following data for each virtual sharp in the view:

[`color_value`,

[swLineStyles_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineStyles_e.html) option (-1 if no line style is specified),

[swLineWeights_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html) option (-1 if no line weight is specified),

layer ID (-1 if no layer is specified),

[swLayerOverride_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLayerOverride_e.html) option,

0 (**NOTE:** 0 = witness line data),

number (m) of witness lines,

witness line 1[start_point[x,y,z], end_point[x,y,z&cd;

...

witness line m[start_point[x,y,z], end_point[x,y,z&cd;,

1 (**NOTE**: 1 = witness arc data),

number (n) of witness arcs,

witness arc 1[start_point[x,y,z], end_point[x,y,z], center_point[x,y,z], normal_point[x,y,z&cd;

...

witness arc n[start_point[x,y,z], end_point[x,y,z], center_point[x,y,z], normal_point[x,y,z&cd;]

Where:

`color_value =` MAX(MIN(`red_rgb_value`,255),0) `+` MAX(MIN(`green_rgb_value`,255),0)*16*16 `+` MAX(MIN(`blue_rgb_value`,255),0)*16*16*16*16

Call [IView::GetWitnessEntitiesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetWitnessEntitiesCount.html) to get the size of the array returned by this method.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::IGetWitnessGeomInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetWitnessGeomInfo.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0

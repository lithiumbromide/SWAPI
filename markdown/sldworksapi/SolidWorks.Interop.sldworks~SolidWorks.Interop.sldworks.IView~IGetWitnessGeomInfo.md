---
title: "IGetWitnessGeomInfo Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetWitnessGeomInfo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetWitnessGeomInfo.html"
---

# IGetWitnessGeomInfo Method (IView)

Gets the geometry data for all of the virtual sharp witness lines in this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetWitnessGeomInfo( _
   ByVal ArraySize As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim ArraySize As System.Integer
Dim value As System.Double

value = instance.IGetWitnessGeomInfo(ArraySize)
```

### C#

```csharp
System.double IGetWitnessGeomInfo(
   System.int ArraySize
)
```

### C++/CLI

```cpp
System.double IGetWitnessGeomInfo(
   System.int ArraySize
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ArraySize`: Size of the virtual sharp witness line geometry data array (see **Remarks**)

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_methods.htm) for details about this type of method.

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

1 (**NOTE:** 1 = witness arc data),

number (n) of witness arcs,

witness arc 1[start_point[x,y,z], end_point[x,y,z], center_point[x,y,z], normal_point[x,y,z&cd;

...

witness arc n[start_point[x,y,z], end_point[x,y,z], center_point[x,y,z], normal_point[x,y,z&cd;]

Where:

`color_value =` MAX(MIN(`red_rgb_value`,255),0) `+` MAX(MIN(`green_rgb_value`,255),0)*16*16 `+` MAX(MIN(`blue_rgb_value`,255),0)*16*16*16*16

Before calling this method, call [IView::GetWitnessEntitiesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetWitnessEntitiesCount.html) to get the size of the array returned by this method.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetWitnessGeomInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetWitnessGeomInfo.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0

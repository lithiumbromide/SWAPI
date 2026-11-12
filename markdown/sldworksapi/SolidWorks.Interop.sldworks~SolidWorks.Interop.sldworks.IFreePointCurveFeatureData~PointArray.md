---
title: "PointArray Property (IFreePointCurveFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFreePointCurveFeatureData"
member: "PointArray"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFreePointCurveFeatureData~PointArray.html"
---

# PointArray Property (IFreePointCurveFeatureData)

Gets or sets the list of X, Y, Z coordinates for the points for this free-point curve.

## Syntax

### Visual Basic (Declaration)

```vb
Property PointArray As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFreePointCurveFeatureData
Dim value As System.Object

instance.PointArray = value

value = instance.PointArray
```

### C#

```csharp
System.object PointArray {get; set;}
```

### C++/CLI

```cpp
property System.Object^ PointArray {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of doubles containing 3 * points (see **Remarks**)

## VBA Syntax

See [FreePointCurveFeatureData::PointArray](ms-its:sldworksapivb6.chm::/sldworks~FreePointCurveFeatureData~PointArray.html).

## Examples

[Insert Free Point Curve Feature (C#)](Insert_Free_Point_Curve_Feature_Example_CSharp.htm)
[Insert Free Point Curve Feature (VB.NET)](Insert_Free_Point_Curve_Feature_Example_VBNET.htm)
[Insert Free Point Curve Feature (VBA)](Insert_Free_Point_Curve_Feature_Example_VB.htm)

## Remarks

The ArrayDataIn argument is an array of doubles containing 3 * points:

[ x1, y1, z1, x2, y2, z2, ... ]

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IFreePointCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFreePointCurveFeatureData.html)
[IFreePointCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFreePointCurveFeatureData_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0

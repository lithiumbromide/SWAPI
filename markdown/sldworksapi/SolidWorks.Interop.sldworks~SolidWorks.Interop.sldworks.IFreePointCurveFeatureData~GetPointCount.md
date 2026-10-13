---
title: "GetPointCount Method (IFreePointCurveFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFreePointCurveFeatureData"
member: "GetPointCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFreePointCurveFeatureData~GetPointCount.html"
---

# GetPointCount Method (IFreePointCurveFeatureData)

Gets the number of doubles (3 * number of points) of this free-point curve.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPointCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFreePointCurveFeatureData
Dim value As System.Integer

value = instance.GetPointCount()
```

### C#

```csharp
System.int GetPointCount()
```

### C++/CLI

```cpp
System.int GetPointCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of doubles (3 * number of points) of this free-point curve

## VBA Syntax

See [FreePointCurveFeatureData::GetPointCount](ms-its:sldworksapivb6.chm::/sldworks~FreePointCurveFeatureData~GetPointCount.html).

## Examples

[Insert Free Point Curve Feature (C#)](Insert_Free_Point_Curve_Feature_Example_CSharp.htm)
[Insert Free Point Curve Feature (VB.NET)](Insert_Free_Point_Curve_Feature_Example_VBNET.htm)
[Insert Free Point Curve Feature (VBA)](Insert_Free_Point_Curve_Feature_Example_VB.htm)

## See Also

[IFreePointCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFreePointCurveFeatureData.html)
[IFreePointCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFreePointCurveFeatureData_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0

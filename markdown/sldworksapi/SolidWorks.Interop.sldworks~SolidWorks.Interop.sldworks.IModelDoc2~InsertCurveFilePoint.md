---
title: "InsertCurveFilePoint Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertCurveFilePoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertCurveFilePoint.html"
---

# InsertCurveFilePoint Method (IModelDoc2)

Creates a point for a curve.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertCurveFilePoint( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Boolean

value = instance.InsertCurveFilePoint(X, Y, Z)
```

### C#

```csharp
System.bool InsertCurveFilePoint(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
System.bool InsertCurveFilePoint(
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: X value for the point
- `Y`: Y value for the point
- `Z`: Z value for the point

### Return Value

True if this call is successful, false if not

## VBA Syntax

See [ModelDoc2::InsertCurveFilePoint](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertCurveFilePoint.html).

## Examples

[Insert Free Point Curve Feature (C#)](Insert_Free_Point_Curve_Feature_Example_CSharp.htm)
[Insert Free Point Curve Feature (VB.NET)](Insert_Free_Point_Curve_Feature_Example_VBNET.htm)
[Insert Free Point Curve Feature (VBA)](Insert_Free_Point_Curve_Feature_Example_VB.htm)

## Remarks

This method:

- sets a point for a curve.
- is called multiple times after [IModelDoc2::InsertCurveFileBegin](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertCurveFileBegin.html) and before [IModelDoc2::InsertCurveFileEnd](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertCurveFileEnd.html).

See the examples.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::InsertCurveFile Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertCurveFile.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

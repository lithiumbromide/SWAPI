---
title: "InsertSplinePoint Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertSplinePoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSplinePoint.html"
---

# InsertSplinePoint Method (IModelDoc2)

Inserts a spline point.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertSplinePoint( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double

instance.InsertSplinePoint(X, Y, Z)
```

### C#

```csharp
void InsertSplinePoint(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
void InsertSplinePoint(
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: X coordinate of spline point
- `Y`: Y coordinate of spline point
- `Z`: Z coordinate of spline point

## VBA Syntax

See [ModelDoc2::InsertSplinePoint](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertSplinePoint.html).

## Examples

[Insert Spline Point (VBA)](Insert_Spline_Point_Example_VB.htm)
[Insert Spline Point (VB.NET)](Insert_Spline_Point_Example_VBNET.htm)
[Insert Spline Point (C#)](Insert_Spline_Point_Example_CSharp.htm)

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::CreateSpline Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateSpline.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

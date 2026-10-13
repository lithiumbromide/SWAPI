---
title: "Insert3DSplineCurve Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "Insert3DSplineCurve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Insert3DSplineCurve.html"
---

# Insert3DSplineCurve Method (IModelDoc2)

Inserts a 3D-spline curve through the selected reference points.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Insert3DSplineCurve( _
   ByVal CurveClosed As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim CurveClosed As System.Boolean

instance.Insert3DSplineCurve(CurveClosed)
```

### C#

```csharp
void Insert3DSplineCurve(
   System.bool CurveClosed
)
```

### C++/CLI

```cpp
void Insert3DSplineCurve(
   System.bool CurveClosed
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CurveClosed`: True if you want the curve to be closed, false if not

## VBA Syntax

See [ModelDoc2::Insert3DSplineCurve](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~Insert3DSplineCurve.html).

## Examples

[Insert a 3D-Spline Curve (VBA)](Insert_3D_Spline_Curve_Example_VB.htm)
[Create Curve Through Reference Points (VBA)](Create_Curve_Through_Reference_Points_Example_VB.htm)
[Create Curve Through Reference Points (VB.NET)](Create_Curve_Through_Reference_Points_Example_VBNET.htm)
[Create Curve Through Reference Points (C#)](Create_Curve_Through_Reference_Points_Example_CSharp.htm)

## Remarks

Before calling this method, select the reference points by calling [IModelDocExtension::SelectbyID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html) with Marks of 1.

To create 2D splines on a sketch, use [IModelDoc2::SketchSpline](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SketchSpline.html) or [IModelDoc2::CreateSpline](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreateSpline.html) or [IModelDoc2::ICreateSpline](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ICreateSpline.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

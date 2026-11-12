---
title: "ShowInflectionPoints Property (ISketchSpline)"
project: "SOLIDWORKS API Help"
interface: "ISketchSpline"
member: "ShowInflectionPoints"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ShowInflectionPoints.html"
---

# ShowInflectionPoints Property (ISketchSpline)

Gets or sets whether show the inflection points of this spline.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShowInflectionPoints As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSpline
Dim value As System.Boolean

instance.ShowInflectionPoints = value

value = instance.ShowInflectionPoints
```

### C#

```csharp
System.bool ShowInflectionPoints {get; set;}
```

### C++/CLI

```cpp
property System.bool ShowInflectionPoints {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to show the inflection points, false to not

## VBA Syntax

See [SketchSpline::ShowInflectionPoints](ms-its:sldworksapivb6.chm::/sldworks~SketchSpline~ShowInflectionPoints.html).

## Examples

[Get and Set Spline Properties (VBA)](Get_and_Set_Spline_Properties_Example_VB.htm)

## Remarks

Inflection points indicate where the concavity of the spline changes.

## See Also

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.html)
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.html)
[ISketchSpline::DeletePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~DeletePoint.html)
[ISketchSpline::GetPointCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetPointCount.html)
[ISketchSpline::GetPoints2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetPoints2.html)
[ISketchSpline::IEnumPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~IEnumPoints.html)
[ISketchSpline::InsertPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~InsertPoint.html)
[ISketchHandle::SplinePointNumber Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~SplinePointNumber.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0

---
title: "ShowCurvatureCombs Property (ISketchSpline)"
project: "SOLIDWORKS API Help"
interface: "ISketchSpline"
member: "ShowCurvatureCombs"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ShowCurvatureCombs.html"
---

# ShowCurvatureCombs Property (ISketchSpline)

Gets or sets whether to show curvature combs.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShowCurvatureCombs As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSpline
Dim value As System.Boolean

instance.ShowCurvatureCombs = value

value = instance.ShowCurvatureCombs
```

### C#

```csharp
System.bool ShowCurvatureCombs {get; set;}
```

### C++/CLI

```cpp
property System.bool ShowCurvatureCombs {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to show curvature combs, false to not

## VBA Syntax

See [SketchSpline::ShowCurvatureCombs](ms-its:sldworksapivb6.chm::/sldworks~SketchSpline~ShowCurvatureCombs.html).

## Remarks

Use [ISketchManager::CurvatureScale](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~CurvatureScale.html) to adjust the size of all of the curvature combs of this spline.

## See Also

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.html)
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.html)
[ISketchManager::CurvatureDensity Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CurvatureDensity.html)
[ISketchSpline::AddCurvatureControl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~AddCurvatureControl.html)
[ISketchHandle::CurvatureControlled Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~CurvatureControlled.html)
[ISketchHandle::RadiusOfCurvature Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~RadiusOfCurvature.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0

---
title: "CurvatureScale Property (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "CurvatureScale"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CurvatureScale.html"
---

# CurvatureScale Property (ISketchManager)

Gets or sets the scaling factor by which to adjust the size of the curvature combs for this spline.

## Syntax

### Visual Basic (Declaration)

```vb
Property CurvatureScale As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim value As System.Double

instance.CurvatureScale = value

value = instance.CurvatureScale
```

### C#

```csharp
System.double CurvatureScale {get; set;}
```

### C++/CLI

```cpp
property System.double CurvatureScale {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Curvature density of the curvature combs for this spline; valid values from 0 - 100

## VBA Syntax

See [SketchManager::CurvatureScale](ms-its:sldworksapivb6.chm::/sldworks~SketchManager~CurvatureScale.html).

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)
[ISketchSpline::ShowCurvatureCombs Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ShowCurvatureCombs.html)
[ISketchManager::CurvatureDensity Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CurvatureDensity.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0

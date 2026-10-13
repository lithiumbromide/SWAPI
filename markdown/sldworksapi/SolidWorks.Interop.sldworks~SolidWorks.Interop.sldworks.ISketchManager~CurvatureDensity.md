---
title: "CurvatureDensity Property (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "CurvatureDensity"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CurvatureDensity.html"
---

# CurvatureDensity Property (ISketchManager)

Gets or sets the scaling factor by which to adjust the density of the curvature combs for this spline.

## Syntax

### Visual Basic (Declaration)

```vb
Property CurvatureDensity As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim value As System.Integer

instance.CurvatureDensity = value

value = instance.CurvatureDensity
```

### C#

```csharp
System.int CurvatureDensity {get; set;}
```

### C++/CLI

```cpp
property System.int CurvatureDensity {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Curvature density of the curvature combs for this spline; valid values from 0 - 100

## VBA Syntax

See [SketchManager::CurvatureDensity](ms-its:sldworksapivb6.chm::/sldworks~SketchManager~CurvatureDensity.html).

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)
[ISketchManager::CurvatureScale Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CurvatureScale.html)
[ISketchSpline::ShowCurvatureCombs Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ShowCurvatureCombs.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0

---
title: "SurfaceForCut Property (ISurfaceCutFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceCutFeatureData"
member: "SurfaceForCut"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData~SurfaceForCut.html"
---

# SurfaceForCut Property (ISurfaceCutFeatureData)

Gets or sets the surface to use to cut the solid bodies.

## Syntax

### Visual Basic (Declaration)

```vb
Property SurfaceForCut As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceCutFeatureData
Dim value As System.Object

instance.SurfaceForCut = value

value = instance.SurfaceForCut
```

### C#

```csharp
System.object SurfaceForCut {get; set;}
```

### C++/CLI

```cpp
property System.Object^ SurfaceForCut {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Surface feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) to use to cut the solid bodies

## VBA Syntax

See [SurfCutFeatureData::SurfaceForCut](ms-its:sldworksapivb6.chm::/sldworks~SurfCutFeatureData~SurfaceForCut.html).

## Remarks

To access this interface, you must declare it as SurfCutFeatureData or ISurfCutFeatureData.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfaceCutFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData.html)
[ISurfaceCutFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

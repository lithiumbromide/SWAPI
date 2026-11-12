---
title: "Distance Property (ISurfaceRadiateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceRadiateFeatureData"
member: "Distance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData~Distance.html"
---

# Distance Property (ISurfaceRadiateFeatureData)

Gets or sets the radiate distance for this surface radiate feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Distance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceRadiateFeatureData
Dim value As System.Double

instance.Distance = value

value = instance.Distance
```

### C#

```csharp
System.double Distance {get; set;}
```

### C++/CLI

```cpp
property System.double Distance {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Width of the surface

## VBA Syntax

See [SurfaceRadiateFeatureData::Distance](ms-its:sldworksapivb6.chm::/sldworks~SurfaceRadiateFeatureData~Distance.html).

## Examples

See the [ISurfaceRadiateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData.html) examples.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfaceRadiateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData.html)
[ISurfaceRadiateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus SP2, Revision Number 10.2

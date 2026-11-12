---
title: "Flip Property (ISurfaceRadiateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceRadiateFeatureData"
member: "Flip"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData~Flip.html"
---

# Flip Property (ISurfaceRadiateFeatureData)

Gets or sets whether to flip the direction of this surface radiate feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Flip As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceRadiateFeatureData
Dim value As System.Boolean

instance.Flip = value

value = instance.Flip
```

### C#

```csharp
System.bool Flip {get; set;}
```

### C++/CLI

```cpp
property System.bool Flip {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True flips the radiate direction, false does not

## VBA Syntax

See [SurfaceRadiateFeatureData::Flip](ms-its:sldworksapivb6.chm::/sldworks~SurfaceRadiateFeatureData~Flip.html).

## Examples

See the [ISurfaceRadiateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData.html) examples.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfaceRadiateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData.html)
[ISurfaceRadiateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData_members.html)
[ISurfaceRadiateFeatureData::DirectionReference Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData~DirectionReference.html)

## Availability

SOLIDWORKS 2001Plus SP2, Revision Number 10.2

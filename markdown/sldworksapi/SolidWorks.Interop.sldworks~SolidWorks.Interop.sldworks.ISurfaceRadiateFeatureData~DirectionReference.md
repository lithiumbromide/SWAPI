---
title: "DirectionReference Property (ISurfaceRadiateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceRadiateFeatureData"
member: "DirectionReference"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData~DirectionReference.html"
---

# DirectionReference Property (ISurfaceRadiateFeatureData)

Gets or sets the radiate direction setting for this surface radiate feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property DirectionReference As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceRadiateFeatureData
Dim value As System.Object

instance.DirectionReference = value

value = instance.DirectionReference
```

### C#

```csharp
System.object DirectionReference {get; set;}
```

### C++/CLI

```cpp
property System.Object^ DirectionReference {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Face, reference plane, or reference surface indicating radiate direction

## VBA Syntax

See [SurfaceRadiateFeatureData::DirectionReference](ms-its:sldworksapivb6.chm::/sldworks~SurfaceRadiateFeatureData~DirectionReference.html).

## Examples

See the [ISurfaceRadiateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData.html) examples.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfaceRadiateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData.html)
[ISurfaceRadiateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData_members.html)
[ISurfaceRadiateFeatureData::Flip Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData~Flip.html)

## Availability

SOLIDWORKS 2001Plus SP2, Revision Number 10.2

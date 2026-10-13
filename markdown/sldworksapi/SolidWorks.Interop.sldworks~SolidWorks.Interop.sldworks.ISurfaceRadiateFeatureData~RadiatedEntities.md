---
title: "RadiatedEntities Property (ISurfaceRadiateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceRadiateFeatureData"
member: "RadiatedEntities"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData~RadiatedEntities.html"
---

# RadiatedEntities Property (ISurfaceRadiateFeatureData)

Gets or sets the radiated entities for this surface radiate feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property RadiatedEntities As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceRadiateFeatureData
Dim value As System.Object

instance.RadiatedEntities = value

value = instance.RadiatedEntities
```

### C#

```csharp
System.object RadiatedEntities {get; set;}
```

### C++/CLI

```cpp
property System.Object^ RadiatedEntities {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of radiated entities

## VBA Syntax

See [SurfaceRadiateFeatureData::RadiatedEntities](ms-its:sldworksapivb6.chm::/sldworks~SurfaceRadiateFeatureData~RadiatedEntities.html).

## Examples

See the [ISurfaceRadiateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData.html) examples.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfaceRadiateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData.html)
[ISurfaceRadiateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData_members.html)
[ISurfaceRadiateSurfaceData::GetRadiatedEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData~GetRadiatedEntitiesCount.html)
[ISurfaceRadiateSurfaceData::IGetRadiatedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData~IGetRadiatedEntities.html)
[ISurfaceRadiateSurfaceData::ISetRadiatedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData~ISetRadiatedEntities.html)

## Availability

SOLIDWORKS 2001Plus SP2, Revision Number 10.2

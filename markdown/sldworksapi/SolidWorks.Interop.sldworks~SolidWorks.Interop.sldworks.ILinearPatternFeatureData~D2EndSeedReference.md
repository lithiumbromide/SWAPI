---
title: "D2EndSeedReference Property (ILinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILinearPatternFeatureData"
member: "D2EndSeedReference"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D2EndSeedReference.html"
---

# D2EndSeedReference Property (ILinearPatternFeatureData)

Gets or sets the seed feature geometry to offset from the up-to reference geometry in Direction 2 of this bidirectional linear pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D2EndSeedReference As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILinearPatternFeatureData
Dim value As System.Object

instance.D2EndSeedReference = value

value = instance.D2EndSeedReference
```

### C#

```csharp
System.object D2EndSeedReference {get; set;}
```

### C++/CLI

```cpp
property System.Object^ D2EndSeedReference {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Seed geometry ([vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html), [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html), [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html), or [plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html)) to offset from [ILinearPatternFeatureData::D2EndReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D2EndReference.html)

## VBA Syntax

See [LinearPatternFeatureData::D2EndSeedReference](ms-its:sldworksapivb6.chm::/sldworks~LinearPatternFeatureData~D2EndSeedReference.html).

## Remarks

This property is valid only if [ILinearPatternFeatureData::D2EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D2EndCondition.html) is set to [swPatternEndCondition_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPatternEndCondition_e.html).swPatternEndCondition_UpToReference.

## See Also

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html)
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0

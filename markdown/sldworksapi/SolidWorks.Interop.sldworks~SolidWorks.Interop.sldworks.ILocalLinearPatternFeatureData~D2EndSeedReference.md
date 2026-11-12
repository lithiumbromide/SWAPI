---
title: "D2EndSeedReference Property (ILocalLinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalLinearPatternFeatureData"
member: "D2EndSeedReference"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D2EndSeedReference.html"
---

# D2EndSeedReference Property (ILocalLinearPatternFeatureData)

Gets or sets the seed feature geometry to offset from the up-to reference geometry in Direction 2 of this bidirectional linear component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D2EndSeedReference As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalLinearPatternFeatureData
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

Seed geometry ([vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html), [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html), [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html), or [plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html)) to offset from [ILocalLinearPatternFeatureData::D2EndReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D2EndReference.html)

## VBA Syntax

See [LocalLinearPatternFeatureData::D2EndSeedReference](ms-its:sldworksapivb6.chm::/sldworks~LocalLinearPatternFeatureData~D2EndSeedReference.html).

## Remarks

This property is valid only if:

- [ILocalLinearPatternFeatureData::D2EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D2EndCondition.html) is set to [swPatternEndCondition_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPatternEndCondition_e.html).swPatternEndCondition_UpToReference,

- and -

- [ILocalLinearPatternFeatureData::D2EndUseSeedReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D2EndUseSeedReference.html) is true.

To pre-select, use selection Mark = 2048.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

For more information, see the **Linear Component Pattern PropertyManager** topic in the SOLIDWORKS Design user-interface help.

## See Also

[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.html)
[ILocalLinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData_members.html)
[ILocalLinearPatternFeatureData::D2EndSeedReferenceType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D2EndSeedReferenceType.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0

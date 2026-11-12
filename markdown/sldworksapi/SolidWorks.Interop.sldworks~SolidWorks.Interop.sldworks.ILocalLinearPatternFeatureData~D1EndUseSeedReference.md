---
title: "D1EndUseSeedReference Property (ILocalLinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalLinearPatternFeatureData"
member: "D1EndUseSeedReference"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D1EndUseSeedReference.html"
---

# D1EndUseSeedReference Property (ILocalLinearPatternFeatureData)

Gets or sets whether to offset a pattern seed reference or a centroid from the up-to reference geometry in Direction 1 of this linear component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D1EndUseSeedReference As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalLinearPatternFeatureData
Dim value As System.Boolean

instance.D1EndUseSeedReference = value

value = instance.D1EndUseSeedReference
```

### C#

```csharp
System.bool D1EndUseSeedReference {get; set;}
```

### C++/CLI

```cpp
property System.bool D1EndUseSeedReference {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to offset a pattern seed reference, false to offset a centroid

## VBA Syntax

See [LocalLinearPatternFeatureData::D1EndUseSeedReference](ms-its:sldworksapivb6.chm::/sldworks~LocalLinearPatternFeatureData~D1EndUseSeedReference.html).

## Remarks

This property is valid only if [ILocalLinearPatternFeatureData::D1EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D1EndCondition.html) is set to [swPatternEndCondition_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPatternEndCondition_e.html).swPatternEndCondition_UpToReference.

To pre-select, use selection Mark = 512.

If this property is set to true, use [ILocalLinearPatternFeatureData::D1EndSeedReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D1EndSeedReference.html) to specify the seed geometry to offset from [ILocalLinearPatternFeatureData::D1EndReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D1EndReference.html).

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

For more information, see the **Linear Component Pattern PropertyManager** topic in the SOLIDWORKS Design user-interface help.

## See Also

[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.html)
[ILocalLinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0

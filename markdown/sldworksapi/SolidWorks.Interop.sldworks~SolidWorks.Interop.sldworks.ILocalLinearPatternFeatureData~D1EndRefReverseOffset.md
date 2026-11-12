---
title: "D1EndRefReverseOffset Property (ILocalLinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalLinearPatternFeatureData"
member: "D1EndRefReverseOffset"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D1EndRefReverseOffset.html"
---

# D1EndRefReverseOffset Property (ILocalLinearPatternFeatureData)

Gets or sets whether to reverse the offset from the up-to-reference geometry in Direction 1 of this linear component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D1EndRefReverseOffset As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalLinearPatternFeatureData
Dim value As System.Boolean

instance.D1EndRefReverseOffset = value

value = instance.D1EndRefReverseOffset
```

### C#

```csharp
System.bool D1EndRefReverseOffset {get; set;}
```

### C++/CLI

```cpp
property System.bool D1EndRefReverseOffset {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to reverse [ILocalLinearPatternFeatureData::D1EndRefOffset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D1EndRefOffset.html) from [ILocalLinearPatternFeatureData::D1EndReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D1EndReference.html), false to not

## VBA Syntax

See [LocalLinearPatternFeatureData::D1EndRefReverseOffset](ms-its:sldworksapivb6.chm::/sldworks~LocalLinearPatternFeatureData~D1EndRefReverseOffset.html).

## Remarks

This property is valid only if [ILocalLinearPatternFeatureData::D1EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D1EndCondition.html) is set to [swPatternEndCondition_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPatternEndCondition_e.html).swPatternEndCondition_UpToReference.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

For more information, see the **Linear Component Pattern PropertyManager** topic in the SOLIDWORKS Design user-interface help.

## See Also

[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.html)
[ILocalLinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0

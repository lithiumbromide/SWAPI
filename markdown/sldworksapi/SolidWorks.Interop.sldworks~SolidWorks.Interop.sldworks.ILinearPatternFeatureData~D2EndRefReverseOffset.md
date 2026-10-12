---
title: "D2EndRefReverseOffset Property (ILinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILinearPatternFeatureData"
member: "D2EndRefReverseOffset"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D2EndRefReverseOffset.html"
---

# D2EndRefReverseOffset Property (ILinearPatternFeatureData)

Gets or sets whether to reverse the offset from the up-to-reference geometry in Direction 2 of this bidirectional linear pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D2EndRefReverseOffset As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILinearPatternFeatureData
Dim value As System.Boolean

instance.D2EndRefReverseOffset = value

value = instance.D2EndRefReverseOffset
```

### C#

```csharp
System.bool D2EndRefReverseOffset {get; set;}
```

### C++/CLI

```cpp
property System.bool D2EndRefReverseOffset {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to reverse [ILinearPatternFeatureData::D2EndRefOffset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D2EndRefOffset.html) from [ILinearPatternFeatureData::D2EndReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D2EndReference.html), false to not

## VBA Syntax

See [LinearPatternFeatureData::D2EndRefReverseOffset](ms-its:sldworksapivb6.chm::/sldworks~LinearPatternFeatureData~D2EndRefReverseOffset.html).

## Remarks

This property is valid only if [ILinearPatternFeatureData::D2EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D2EndCondition.html) is set to [swPatternEndCondition_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPatternEndCondition_e.html).swPatternEndCondition_UpToReference.

## See Also

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html)
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0

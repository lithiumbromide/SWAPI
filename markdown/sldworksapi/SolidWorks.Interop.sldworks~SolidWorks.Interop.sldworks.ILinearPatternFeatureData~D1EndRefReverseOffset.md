---
title: "D1EndRefReverseOffset Property (ILinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILinearPatternFeatureData"
member: "D1EndRefReverseOffset"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1EndRefReverseOffset.html"
---

# D1EndRefReverseOffset Property (ILinearPatternFeatureData)

Gets or sets whether to reverse the offset from the up-to-reference geometry in Direction 1 of this linear pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D1EndRefReverseOffset As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILinearPatternFeatureData
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

True to reverse [ILinearPatternFeatureData::D1EndRefOffset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1EndRefOffset.html) from [ILinearPatternFeatureData::D1EndReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1EndReference.html), false to not

## VBA Syntax

See [LinearPatternFeatureData::D1EndRefReverseOffset](ms-its:sldworksapivb6.chm::/sldworks~LinearPatternFeatureData~D1EndRefReverseOffset.html).

## Remarks

This property is valid only if [ILinearPatternFeatureData::D1EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1EndCondition.html) is set to [swPatternEndCondition_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPatternEndCondition_e.html).swPatternEndCondition_UpToReference.

## See Also

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html)
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0

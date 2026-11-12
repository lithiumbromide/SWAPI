---
title: "D1EndUseSpacing Property (ILinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILinearPatternFeatureData"
member: "D1EndUseSpacing"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1EndUseSpacing.html"
---

# D1EndUseSpacing Property (ILinearPatternFeatureData)

Gets or sets whether to use spacing or a number of pattern instances when offsetting up-to reference geometry in Direction 1 for this linear pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D1EndUseSpacing As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILinearPatternFeatureData
Dim value As System.Boolean

instance.D1EndUseSpacing = value

value = instance.D1EndUseSpacing
```

### C#

```csharp
System.bool D1EndUseSpacing {get; set;}
```

### C++/CLI

```cpp
property System.bool D1EndUseSpacing {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use spacing, false to use number of pattern instances in Direction 1

## VBA Syntax

See [LinearPatternFeatureData::D1EndUseSpacing](ms-its:sldworksapivb6.chm::/sldworks~LinearPatternFeatureData~D1EndUseSpacing.html).

## Remarks

This property is valid only if [ILinearPatternFeatureData::D1EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1EndCondition.html) is set to [swPatternEndCondition_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPatternEndCondition_e.html).swPatternEndCondition_UpToReference.

## See Also

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html)
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0

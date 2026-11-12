---
title: "D1EndCondition Property (ILocalLinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalLinearPatternFeatureData"
member: "D1EndCondition"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D1EndCondition.html"
---

# D1EndCondition Property (ILocalLinearPatternFeatureData)

Gets or sets how to specify the spacing of pattern instances in Direction 1 of this linear component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D1EndCondition As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalLinearPatternFeatureData
Dim value As System.Integer

instance.D1EndCondition = value

value = instance.D1EndCondition
```

### C#

```csharp
System.int D1EndCondition {get; set;}
```

### C++/CLI

```cpp
property System.int D1EndCondition {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Spacing of pattern instances in Direction 1 as defined in [swPatternEndCondition_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPatternEndCondition_e.html)

## VBA Syntax

See [LocalLinearPatternFeatureData::D1EndCondition](ms-its:sldworksapivb6.chm::/sldworks~LocalLinearPatternFeatureData~D1EndCondition.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

For more information, see the **Linear Component Pattern PropertyManager** topic in the SOLIDWORKS Design user-interface help.

## See Also

[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.html)
[ILocalLinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData_members.html)
[ILocalLinearPatternFeatureData::RotateInstances Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~RotateInstances.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0

---
title: "D2EndCondition Property (ILinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILinearPatternFeatureData"
member: "D2EndCondition"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D2EndCondition.html"
---

# D2EndCondition Property (ILinearPatternFeatureData)

Gets or sets how to specify the spacing of pattern instances in Direction 2 of this bidirectional linear pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D2EndCondition As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ILinearPatternFeatureData
Dim value As System.Integer

instance.D2EndCondition = value

value = instance.D2EndCondition
```

### C#

```csharp
System.int D2EndCondition {get; set;}
```

### C++/CLI

```cpp
property System.int D2EndCondition {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Spacing of pattern instances in Direction 2 as defined in [swPatternEndCondition_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPatternEndCondition_e.html)

## VBA Syntax

See [LinearPatternFeatureData::D2EndCondition](ms-its:sldworksapivb6.chm::/sldworks~LinearPatternFeatureData~D2EndCondition.html).

## Examples

See the [ILinearPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html) example.

## Remarks

For more information, see the **Linear Patterns and the Linear Pattern PropertyManager** topic in the SOLIDWORKS Design user-interface help.

## See Also

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html)
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0

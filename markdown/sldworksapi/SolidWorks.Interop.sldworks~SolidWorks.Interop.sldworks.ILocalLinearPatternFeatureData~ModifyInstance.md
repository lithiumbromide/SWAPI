---
title: "ModifyInstance Method (ILocalLinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalLinearPatternFeatureData"
member: "ModifyInstance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~ModifyInstance.html"
---

# ModifyInstance Method (ILocalLinearPatternFeatureData)

Modifies the specified pattern instance with the specified distances in Directions 1 and 2 in this linear component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function ModifyInstance( _
   ByVal Instance As System.Integer, _
   ByVal D1Distance As System.Double, _
   ByVal IsD1OffsetFromNominal As System.Boolean, _
   ByVal D2Distance As System.Double, _
   ByVal IsD2OffsetFromNominal As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalLinearPatternFeatureData
Dim Instance As System.Integer
Dim D1Distance As System.Double
Dim IsD1OffsetFromNominal As System.Boolean
Dim D2Distance As System.Double
Dim IsD2OffsetFromNominal As System.Boolean
Dim value As System.Boolean

value = instance.ModifyInstance(Instance, D1Distance, IsD1OffsetFromNominal, D2Distance, IsD2OffsetFromNominal)
```

### C#

```csharp
System.bool ModifyInstance(
   System.int Instance,
   System.double D1Distance,
   System.bool IsD1OffsetFromNominal,
   System.double D2Distance,
   System.bool IsD2OffsetFromNominal
)
```

### C++/CLI

```cpp
System.bool ModifyInstance(
   System.int Instance,
   System.double D1Distance,
   System.bool IsD1OffsetFromNominal,
   System.double D2Distance,
   System.bool IsD2OffsetFromNominal
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Instance`: Pattern instance number (see **Remarks**)
- `D1Distance`: Distance from the pattern seed in Direction 1
- `IsD1OffsetFromNominal`: True if D1Distance is the offset from the nominal position of Instance, false if not
- `D2Distance`: Distance from the pattern seed in Direction 2
- `IsD2OffsetFromNominal`: True if D2Distance is the offset from the nominal position of Instance, false if not

### Return Value

True if the pattern instance is modified successfully, false if not

## VBA Syntax

See [LocalLinearPatternFeatureData::ModifyInstance](ms-its:sldworksapivb6.chm::/sldworks~LocalLinearPatternFeatureData~ModifyInstance.html).

## Remarks

To calculate Instance:

1. Ensure that [ILocalLinearPatternFeatureData::D2PatternSeedOnly](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D2PatternSeedOnly.html) is set to false.
2. Calculate:

For a bi-directional pattern:

`I` = `n2` * (`i` - 1) + (`j` - 1)

For a uni-directional pattern:

`I` = `i` - 1

where:

- `I` = pattern instance number
- `n2` = number of instances in Direction 2
- `i` = index for Direction 1
- `j` = index for Direction 2

In the pattern's PropertyManager, find `n2` in the **Direction 2** **> Spacing and Instances > Number of instances** field and find [`i,j`] in the **Modified Instances** section.

## See Also

[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.html)
[ILocalLinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29

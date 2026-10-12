---
title: "ModifyInstance Method (ILocalCircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalCircularPatternFeatureData"
member: "ModifyInstance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~ModifyInstance.html"
---

# ModifyInstance Method (ILocalCircularPatternFeatureData)

Modifies the specified pattern instance with the specified angle in this circular component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function ModifyInstance( _
   ByVal Instance As System.Integer, _
   ByVal AngleFromSeed As System.Double, _
   ByVal IsOffsetFromNominal As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalCircularPatternFeatureData
Dim Instance As System.Integer
Dim AngleFromSeed As System.Double
Dim IsOffsetFromNominal As System.Boolean
Dim value As System.Boolean

value = instance.ModifyInstance(Instance, AngleFromSeed, IsOffsetFromNominal)
```

### C#

```csharp
System.bool ModifyInstance(
   System.int Instance,
   System.double AngleFromSeed,
   System.bool IsOffsetFromNominal
)
```

### C++/CLI

```cpp
System.bool ModifyInstance(
   System.int Instance,
   System.double AngleFromSeed,
   System.bool IsOffsetFromNominal
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Instance`: Pattern instance number (see **Remarks**)
- `AngleFromSeed`: Angle from the pattern seed
- `IsOffsetFromNominal`: True if AngleFromSeed is the offset from the nominal position of Instance, false if not

### Return Value

True if the pattern instance is modified successfully, false if not

## VBA Syntax

See [LocalCircularPatternFeatureData::ModifyInstance](ms-its:sldworksapivb6.chm::/sldworks~LocalCircularPatternFeatureData~ModifyInstance.html).

## Remarks

To calculate Instance:

Calculate:

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

[ILocalCircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData.html)
[ILocalCircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29

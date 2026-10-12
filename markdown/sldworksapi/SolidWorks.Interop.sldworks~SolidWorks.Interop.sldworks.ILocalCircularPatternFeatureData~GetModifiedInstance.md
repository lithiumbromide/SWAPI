---
title: "GetModifiedInstance Method (ILocalCircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalCircularPatternFeatureData"
member: "GetModifiedInstance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~GetModifiedInstance.html"
---

# GetModifiedInstance Method (ILocalCircularPatternFeatureData)

Gets the modified values for the specified pattern instance in this circular component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetModifiedInstance( _
   ByVal Instance As System.Integer, _
   ByRef AngleFromSeed As System.Double, _
   ByRef OffsetFromNominal As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalCircularPatternFeatureData
Dim Instance As System.Integer
Dim AngleFromSeed As System.Double
Dim OffsetFromNominal As System.Double

instance.GetModifiedInstance(Instance, AngleFromSeed, OffsetFromNominal)
```

### C#

```csharp
void GetModifiedInstance(
   System.int Instance,
   out System.double AngleFromSeed,
   out System.double OffsetFromNominal
)
```

### C++/CLI

```cpp
void GetModifiedInstance(
   System.int Instance,
   [Out] System.double AngleFromSeed,
   [Out] System.double OffsetFromNominal
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Instance`: Pattern instance number (see **Remarks**)
- `AngleFromSeed`: Angle from the pattern seed
- `OffsetFromNominal`: Degree offset from the nominal position of Instance

## VBA Syntax

See [LocalCircularPatternFeatureData::GetModifiedInstance](ms-its:sldworksapivb6.chm::/sldworks~LocalCircularPatternFeatureData~GetModifiedInstance.html).

## Remarks

To specify Instance, you can use [ILocalCircularPatternFeatureData::GetModifiedInstances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~GetModifiedInstances.html) to learn which pattern instances are modified.

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

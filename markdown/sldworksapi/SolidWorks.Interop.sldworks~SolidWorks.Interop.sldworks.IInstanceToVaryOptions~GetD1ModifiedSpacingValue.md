---
title: "GetD1ModifiedSpacingValue Method (IInstanceToVaryOptions)"
project: "SOLIDWORKS API Help"
interface: "IInstanceToVaryOptions"
member: "GetD1ModifiedSpacingValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions~GetD1ModifiedSpacingValue.html"
---

# GetD1ModifiedSpacingValue Method (IInstanceToVaryOptions)

Gets the spacing in Direction 1 of the specified modified pattern instance.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetD1ModifiedSpacingValue( _
   ByVal Instance As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IInstanceToVaryOptions
Dim Instance As System.Integer
Dim value As System.Double

value = instance.GetD1ModifiedSpacingValue(Instance)
```

### C#

```csharp
System.double GetD1ModifiedSpacingValue(
   System.int Instance
)
```

### C++/CLI

```cpp
System.double GetD1ModifiedSpacingValue(
   System.int Instance
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Instance`: Pattern instance number (see **Remarks**)

### Return Value

Spacing value in Direction 1

## VBA Syntax

See [InstanceToVaryOptions::GetD1ModifiedSpacingValue](ms-its:sldworksapivb6.chm::/sldworks~InstanceToVaryOptions~GetD1ModifiedSpacingValue.html).

## Examples

See the [IInstanceToVaryOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions.html) examples.

## Remarks

To specify Instance, you can use [IInstanceToVaryOptions::GetModifiedInstances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions~GetModifiedInstances.html) to learn which pattern instances are modified.

To calculate Instance:

1. Ensure that the D2PatternSeedOnly property in the pattern feature data object is set to false.
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

[IInstanceToVaryOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions.html)
[IInstanceToVaryOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29

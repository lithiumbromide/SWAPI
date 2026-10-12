---
title: "ModifyD1SpacingValue Method (IInstanceToVaryOptions)"
project: "SOLIDWORKS API Help"
interface: "IInstanceToVaryOptions"
member: "ModifyD1SpacingValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions~ModifyD1SpacingValue.html"
---

# ModifyD1SpacingValue Method (IInstanceToVaryOptions)

Modifies the spacing in Direction 1 of the specified pattern instance.

## Syntax

### Visual Basic (Declaration)

```vb
Function ModifyD1SpacingValue( _
   ByVal Instance As System.Integer, _
   ByVal Value As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IInstanceToVaryOptions
Dim Instance As System.Integer
Dim Value As System.Double
Dim value As System.Boolean

value = instance.ModifyD1SpacingValue(Instance, Value)
```

### C#

```csharp
System.bool ModifyD1SpacingValue(
   System.int Instance,
   System.double Value
)
```

### C++/CLI

```cpp
System.bool ModifyD1SpacingValue(
   System.int Instance,
   System.double Value
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Instance`: Pattern instance number (see **Remarks**)
- `Value`: Spacing value in Direction 1

### Return Value

True if the spacing is modified successfully, false if not

## VBA Syntax

See [InstanceToVaryOptions::ModifyD1SpacingValue](ms-its:sldworksapivb6.chm::/sldworks~InstanceToVaryOptions~ModifyD1SpacingValue.html).

## Examples

See the [IInstanceToVaryOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions.html) examples.

## Remarks

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

---
title: "ModifyDimensions Method (IInstanceToVaryOptions)"
project: "SOLIDWORKS API Help"
interface: "IInstanceToVaryOptions"
member: "ModifyDimensions"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions~ModifyDimensions.html"
---

# ModifyDimensions Method (IInstanceToVaryOptions)

Modifies the specified dimensions of the specified pattern instance.

## Syntax

### Visual Basic (Declaration)

```vb
Function ModifyDimensions( _
   ByVal Instance As System.Integer, _
   ByVal Dimensions As System.Object, _
   ByVal Values As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IInstanceToVaryOptions
Dim Instance As System.Integer
Dim Dimensions As System.Object
Dim Values As System.Object
Dim value As System.Boolean

value = instance.ModifyDimensions(Instance, Dimensions, Values)
```

### C#

```csharp
System.bool ModifyDimensions(
   System.int Instance,
   System.object Dimensions,
   System.object Values
)
```

### C++/CLI

```cpp
System.bool ModifyDimensions(
   System.int Instance,
   System.Object^ Dimensions,
   System.Object^ Values
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Instance`: Pattern instance number (see **Remarks**)
- `Dimensions`: Array of dimensions
- `Values`: Array of values

### Return Value

True if dimensions modified successfully, false if not

## VBA Syntax

See [InstanceToVaryOptions::ModifyDimensions](ms-its:sldworksapivb6.chm::/sldworks~InstanceToVaryOptions~ModifyDimensions.html).

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

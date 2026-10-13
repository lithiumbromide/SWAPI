---
title: "GetModifiedDimensions Method (IInstanceToVaryOptions)"
project: "SOLIDWORKS API Help"
interface: "IInstanceToVaryOptions"
member: "GetModifiedDimensions"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions~GetModifiedDimensions.html"
---

# GetModifiedDimensions Method (IInstanceToVaryOptions)

Gets the modified dimensions of the specified pattern instance.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetModifiedDimensions( _
   ByVal Instance As System.Integer, _
   ByRef Dimensions As System.Object, _
   ByRef Values As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IInstanceToVaryOptions
Dim Instance As System.Integer
Dim Dimensions As System.Object
Dim Values As System.Object

instance.GetModifiedDimensions(Instance, Dimensions, Values)
```

### C#

```csharp
void GetModifiedDimensions(
   System.int Instance,
   out System.object Dimensions,
   out System.object Values
)
```

### C++/CLI

```cpp
void GetModifiedDimensions(
   System.int Instance,
   [Out] System.Object^ Dimensions,
   [Out] System.Object^ Values
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Instance`: Pattern instance number (see **Remarks**)
- `Dimensions`: Array of modified dimensions
- `Values`: Array of dimension values

## VBA Syntax

See [InstanceToVaryOptions::GetModifiedDimensions](ms-its:sldworksapivb6.chm::/sldworks~InstanceToVaryOptions~GetModifiedDimensions.html).

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

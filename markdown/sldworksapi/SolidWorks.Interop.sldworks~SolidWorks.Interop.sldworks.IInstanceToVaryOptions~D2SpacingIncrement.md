---
title: "D2SpacingIncrement Property (IInstanceToVaryOptions)"
project: "SOLIDWORKS API Help"
interface: "IInstanceToVaryOptions"
member: "D2SpacingIncrement"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions~D2SpacingIncrement.html"
---

# D2SpacingIncrement Property (IInstanceToVaryOptions)

Gets or sets the spacing increment of all pattern instances in Direction 2.

## Syntax

### Visual Basic (Declaration)

```vb
Property D2SpacingIncrement As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IInstanceToVaryOptions
Dim value As System.Double

instance.D2SpacingIncrement = value

value = instance.D2SpacingIncrement
```

### C#

```csharp
System.double D2SpacingIncrement {get; set;}
```

### C++/CLI

```cpp
property System.double D2SpacingIncrement {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Spacing increment in Direction 2

## VBA Syntax

See [InstanceToVaryOptions::D2SpacingIncrement](ms-its:sldworksapivb6.chm::/sldworks~InstanceToVaryOptions~D2SpacingIncrement.html).

## Examples

See the [IInstanceToVaryOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions.html) examples.

## See Also

[IInstanceToVaryOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions.html)
[IInstanceToVaryOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29

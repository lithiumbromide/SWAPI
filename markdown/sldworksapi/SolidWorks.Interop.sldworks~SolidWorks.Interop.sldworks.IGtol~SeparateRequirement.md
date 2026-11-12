---
title: "SeparateRequirement Property (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "SeparateRequirement"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SeparateRequirement.html"
---

# SeparateRequirement Property (IGtol)

Gets or sets whether a SEP REQT label is present with the Gtol symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Property SeparateRequirement As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim value As System.Boolean

instance.SeparateRequirement = value

value = instance.SeparateRequirement
```

### C#

```csharp
System.bool SeparateRequirement {get; set;}
```

### C++/CLI

```cpp
property System.bool SeparateRequirement {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if a SEP REQT label is present, false if not

## VBA Syntax

See [Gtol::SeparateRequirement](ms-its:sldworksapivb6.chm::/sldworks~Gtol~SeparateRequirement.html).

## Examples

See the [IGtolFrame](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame.html) examples.

## Remarks

The Separate Requirement label is present below the Gtol frame.

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31

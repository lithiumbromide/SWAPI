---
title: "IncludeMass Property (ICWLinkageRod)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLinkageRod"
member: "IncludeMass"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod~IncludeMass.html"
---

# IncludeMass Property (ICWLinkageRod)

Sets whether to add mass to the force calculations of this linkage rod connector.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property IncludeMass As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLinkageRod

instance.IncludeMass = value
```

### C#

```csharp
System.bool IncludeMass {set;}
```

### C++/CLI

```cpp
property System.bool IncludeMass {
   void set (    System.bool value);
}
```

### Property Value

True to include mass in calculations, false to not

## VBA Syntax

See [CWLinkageRod::IncludeMass](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLinkageRod~IncludeMass.html).

## Examples

See the [ICWLinkageRod](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod.html) examples

## Remarks

If this property sets true, then use [ICWLinkageRod::Mass](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod~Mass.html) to specify the density.

## See Also

[ICWLinkageRod Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod.html)
[ICWLinkageRod Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod_members.html)

## Availability

SOLIDWORKS Simulation API 2022 SP0

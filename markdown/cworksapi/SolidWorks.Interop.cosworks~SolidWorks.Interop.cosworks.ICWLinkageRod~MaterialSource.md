---
title: "MaterialSource Property (ICWLinkageRod)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLinkageRod"
member: "MaterialSource"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod~MaterialSource.html"
---

# MaterialSource Property (ICWLinkageRod)

Sets the source of the material for this linkage rod connector.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property MaterialSource As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLinkageRod

instance.MaterialSource = value
```

### C#

```csharp
System.int MaterialSource {set;}
```

### C++/CLI

```cpp
property System.int MaterialSource {
   void set (    System.int value);
}
```

### Property Value

Source of material as defined by [swsMaterialSourceType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMaterialSourceType_e.html)

## VBA Syntax

See [CWLinkageRod::MaterialSource](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLinkageRod~MaterialSource.html).

## Examples

See the [ICWLinkageRod](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod.html) examples

## See Also

[ICWLinkageRod Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod.html)
[ICWLinkageRod Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod_members.html)

## Availability

SOLIDWORKS Simulation API 2022 SP0

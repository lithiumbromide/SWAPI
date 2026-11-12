---
title: "Staggered Property (ICosmeticWeldBeadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICosmeticWeldBeadFeatureData"
member: "Staggered"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~Staggered.html"
---

# Staggered Property (ICosmeticWeldBeadFeatureData)

Gets or sets whether to alternate the positioning of the weld beads on both sides of the weld body.

## Syntax

### Visual Basic (Declaration)

```vb
Property Staggered As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmeticWeldBeadFeatureData
Dim value As System.Boolean

instance.Staggered = value

value = instance.Staggered
```

### C#

```csharp
System.bool Staggered {get; set;}
```

### C++/CLI

```cpp
property System.bool Staggered {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to alternate positioning of the weld beads, false to not (see **Remarks**)

## VBA Syntax

See [CosmeticWeldBeadFeatureData::Staggered](ms-its:sldworksapivb6.chm::/sldworks~CosmeticWeldBeadFeatureData~Staggered.html).

## Examples

See [ICosmeticWeldBeadFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticWeldBeadFeatureData.html) examples.

## Remarks

This property is valid only if [ICosmeticWeldBeadFeatureData::Side](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticWeldBeadFeatureData~Side.html) = [swCosmeticWeldBeadSide_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCosmeticWeldBeadSide_e.html).swCosmeticWeldBeadSide_BothSides and [ICosmeticWeldBeadFeatureData::IntermittentWeld](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticWeldBeadFeatureData~IntermittentWeld.html) is true.

## See Also

[ICosmeticWeldBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.html)
[ICosmeticWeldBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0

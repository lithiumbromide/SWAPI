---
title: "Side Property (ICosmeticWeldBeadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICosmeticWeldBeadFeatureData"
member: "Side"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~Side.html"
---

# Side Property (ICosmeticWeldBeadFeatureData)

Gets or sets how the weld bead is applied to selected faces or edges.

## Syntax

### Visual Basic (Declaration)

```vb
Property Side As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmeticWeldBeadFeatureData
Dim value As System.Integer

instance.Side = value

value = instance.Side
```

### C#

```csharp
System.int Side {get; set;}
```

### C++/CLI

```cpp
property System.int Side {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Weld bead configuration as defined in [swCosmeticWeldBeadSide_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCosmeticWeldBeadSide_e.html)

## VBA Syntax

See [CosmeticWeldBeadFeatureData::Side](ms-its:sldworksapivb6.chm::/sldworks~CosmeticWeldBeadFeatureData~Side.html).

## Examples

See [ICosmeticWeldBeadFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticWeldBeadFeatureData.html) examples.

## Remarks

This property is valid only if [ICosmeticWeldBeadFeatureData::TangentPropagation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticWeldBeadFeatureData~TangentPropagation.html) is false.

## See Also

[ICosmeticWeldBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.html)
[ICosmeticWeldBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0

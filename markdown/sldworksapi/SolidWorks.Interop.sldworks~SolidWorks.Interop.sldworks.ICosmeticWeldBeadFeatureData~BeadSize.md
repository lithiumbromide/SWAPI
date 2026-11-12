---
title: "BeadSize Property (ICosmeticWeldBeadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICosmeticWeldBeadFeatureData"
member: "BeadSize"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~BeadSize.html"
---

# BeadSize Property (ICosmeticWeldBeadFeatureData)

Gets or sets the thickness of a weld bead.

## Syntax

### Visual Basic (Declaration)

```vb
Property BeadSize As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmeticWeldBeadFeatureData
Dim value As System.Double

instance.BeadSize = value

value = instance.BeadSize
```

### C#

```csharp
System.double BeadSize {get; set;}
```

### C++/CLI

```cpp
property System.double BeadSize {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Weld bead thickness

## VBA Syntax

See [CosmeticWeldBeadFeatureData::BeadSize](ms-its:sldworksapivb6.chm::/sldworks~CosmeticWeldBeadFeatureData~BeadSize.html).

## Examples

See [ICosmeticWeldBeadFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticWeldBeadFeatureData.html) examples.

## See Also

[ICosmeticWeldBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.html)
[ICosmeticWeldBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0

---
title: "DimXpertScheme Property (IMirrorComponentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorComponentFeatureData"
member: "DimXpertScheme"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~DimXpertScheme.html"
---

# DimXpertScheme Property (IMirrorComponentFeatureData)

Gets or sets whether to copy the DimXpert scheme of the original components to the opposite-hand versions.

## Syntax

### Visual Basic (Declaration)

```vb
Property DimXpertScheme As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorComponentFeatureData
Dim value As System.Boolean

instance.DimXpertScheme = value

value = instance.DimXpertScheme
```

### C#

```csharp
System.bool DimXpertScheme {get; set;}
```

### C++/CLI

```cpp
property System.bool DimXpertScheme {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to copy the DimXpert scheme, false (default) to not

## VBA Syntax

See [MirrorComponentFeatureData::DimXpertScheme](ms-its:sldworksapivb6.chm::/sldworks~MirrorComponentFeatureData~DimXpertScheme.html).

## Examples

See the [IMirrorComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html) example.

## Remarks

This property is valid only if:

- [IMirrorComponentFeatureData::CreateDerivedConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~CreateDerivedConfigurations.html) is false,

- and -

- [IMirrorComponentFeatureData::BreakLinksToOriginalPart](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~BreakLinksToOriginalPart.html) is false.

## See Also

[IMirrorComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html)
[IMirrorComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0

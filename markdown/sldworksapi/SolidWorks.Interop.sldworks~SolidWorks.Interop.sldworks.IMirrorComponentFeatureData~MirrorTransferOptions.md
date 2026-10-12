---
title: "MirrorTransferOptions Property (IMirrorComponentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorComponentFeatureData"
member: "MirrorTransferOptions"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~MirrorTransferOptions.html"
---

# MirrorTransferOptions Property (IMirrorComponentFeatureData)

Gets or sets the items to transfer to the opposite-hand versions.

## Syntax

### Visual Basic (Declaration)

```vb
Property MirrorTransferOptions As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorComponentFeatureData
Dim value As System.Integer

instance.MirrorTransferOptions = value

value = instance.MirrorTransferOptions
```

### C#

```csharp
System.int MirrorTransferOptions {get; set;}
```

### C++/CLI

```cpp
property System.int MirrorTransferOptions {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Items to transfer as defined in [swMirrorPartOptions_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMirrorPartOptions_e.html)

## VBA Syntax

See [MirrorComponentFeatureData::MirrorTransferOptions](ms-its:sldworksapivb6.chm::/sldworks~MirrorComponentFeatureData~MirrorTransferOptions.html).

## Examples

See the [IMirrorComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html) example.

## Remarks

This property is valid only if:

- [IMirrorComponentFeatureData::CreateDerivedConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~CreateDerivedConfigurations.html) is false,

- and -

- [IMirrorComponentFeatureData::BreakLinksToOriginalPart](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~BreakLinksToOriginalPart.html) is false.

If not set, this property defaults to swMirrorPartOptions_e.swMirrorPartoptions_ImportSolids.

## See Also

[IMirrorComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html)
[IMirrorComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0

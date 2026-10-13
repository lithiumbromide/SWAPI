---
title: "BreakLinksToOriginalPart Property (IMirrorComponentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorComponentFeatureData"
member: "BreakLinksToOriginalPart"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~BreakLinksToOriginalPart.html"
---

# BreakLinksToOriginalPart Property (IMirrorComponentFeatureData)

Gets or sets whether to break links between opposite-hand components and original components.

## Syntax

### Visual Basic (Declaration)

```vb
Property BreakLinksToOriginalPart As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorComponentFeatureData
Dim value As System.Boolean

instance.BreakLinksToOriginalPart = value

value = instance.BreakLinksToOriginalPart
```

### C#

```csharp
System.bool BreakLinksToOriginalPart {get; set;}
```

### C++/CLI

```cpp
property System.bool BreakLinksToOriginalPart {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to break links, false (default) to not

## VBA Syntax

See [MirrorComponentFeatureData::BreakLinksToOriginalPart](ms-its:sldworksapivb6.chm::/sldworks~MirrorComponentFeatureData~BreakLinksToOriginalPart.html).

## Examples

See the [IMirrorComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html) example.

## Remarks

This property is valid only if [IMirrorComponentFeatureData::CreateDerivedConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~CreateDerivedConfigurations.html) is false.

If you set this property to true, then changes made to the original component do not propagate to the opposite-hand version.

## See Also

[IMirrorComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html)
[IMirrorComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0

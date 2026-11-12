---
title: "MateAlignment Property (IProfileCenterMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IProfileCenterMateFeatureData"
member: "MateAlignment"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileCenterMateFeatureData~MateAlignment.html"
---

# MateAlignment Property (IProfileCenterMateFeatureData)

Gets or sets the alignment of this profile center mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property MateAlignment As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IProfileCenterMateFeatureData
Dim value As System.Integer

instance.MateAlignment = value

value = instance.MateAlignment
```

### C#

```csharp
System.int MateAlignment {get; set;}
```

### C++/CLI

```cpp
property System.int MateAlignment {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Mate alignment as defined in [swMateAlign_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMateAlign_e.html)

## VBA Syntax

See [ProfileCenterMateFeatureData::MateAlignment](ms-its:sldworksapivb6.chm::/sldworks~ProfileCenterMateFeatureData~MateAlignment.html).

## Examples

See the [IProfileCenterMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileCenterMateFeatureData.html) examples.

## Remarks

If this property is set to swMateAlign_e:

- swMateAlignALIGNED, then vectors normal to the selected entities point in the same direction.
- swMateAlignANTI_ALIGNED, then vectors normal to the selected entities point in opposite directions.

## See Also

[IProfileCenterMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileCenterMateFeatureData.html)
[IProfileCenterMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileCenterMateFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0

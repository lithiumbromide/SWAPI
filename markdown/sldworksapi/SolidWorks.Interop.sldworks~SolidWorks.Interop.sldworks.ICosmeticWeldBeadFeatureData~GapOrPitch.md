---
title: "GapOrPitch Property (ICosmeticWeldBeadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICosmeticWeldBeadFeatureData"
member: "GapOrPitch"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~GapOrPitch.html"
---

# GapOrPitch Property (ICosmeticWeldBeadFeatureData)

Gets or sets whether to use gap or pitch spacing for intermittent weld beads.

## Syntax

### Visual Basic (Declaration)

```vb
Property GapOrPitch As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmeticWeldBeadFeatureData
Dim value As System.Boolean

instance.GapOrPitch = value

value = instance.GapOrPitch
```

### C#

```csharp
System.bool GapOrPitch {get; set;}
```

### C++/CLI

```cpp
property System.bool GapOrPitch {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use gap spacing, false to use pitch spacing (see **Remarks**)

## VBA Syntax

See [CosmeticWeldBeadFeatureData::GapOrPitch](ms-its:sldworksapivb6.chm::/sldworks~CosmeticWeldBeadFeatureData~GapOrPitch.html).

## Examples

See [ICosmeticWeldBeadFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticWeldBeadFeatureData.html) examples.

## Remarks

This property is valid only if [ICosmeticWeldBeadFeatureData::IntermittentWeld](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticWeldBeadFeatureData~IntermittentWeld.html) is true.

| If this property is... | Then to get and set the gap between the weld beads, call... |
| --- | --- |
| True | ICosmeticWeldBeadFeatureData::Gap |
| False | ICosmeticWeldBeadFeatureData::Pitch |

## See Also

[ICosmeticWeldBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.html)
[ICosmeticWeldBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData_members.html)
[ICosmeticWeldBeadFeatureData::IntermittentWeldLength Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~IntermittentWeldLength.html)
[ICosmeticWeldBeadFeatureData::Staggered Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~Staggered.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0

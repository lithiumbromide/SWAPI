---
title: "Gap Property (ICosmeticWeldBeadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICosmeticWeldBeadFeatureData"
member: "Gap"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~Gap.html"
---

# Gap Property (ICosmeticWeldBeadFeatureData)

Gets or sets the gap between intermittent weld beads.

## Syntax

### Visual Basic (Declaration)

```vb
Property Gap As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmeticWeldBeadFeatureData
Dim value As System.Double

instance.Gap = value

value = instance.Gap
```

### C#

```csharp
System.double Gap {get; set;}
```

### C++/CLI

```cpp
property System.double Gap {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Gap between intermittent weld beads (see **Remarks**)

## VBA Syntax

See [CosmeticWeldBeadFeatureData::Gap](ms-its:sldworksapivb6.chm::/sldworks~CosmeticWeldBeadFeatureData~Gap.html).

## Examples

See [ICosmeticWeldBeadFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticWeldBeadFeatureData.html) examples.

## Remarks

This property is valid only if [ICosmeticWeldBeadFeatureData::GapOrPitch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticWeldBeadFeatureData~GapOrPitch.html) is true and [ICosmeticWeldBeadFeatureData::IntermittentWeld](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticWeldBeadFeatureData~IntermittentWeld.html) is true.

## See Also

[ICosmeticWeldBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.html)
[ICosmeticWeldBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0

---
title: "Pitch Property (ICosmeticWeldBeadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICosmeticWeldBeadFeatureData"
member: "Pitch"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~Pitch.html"
---

# Pitch Property (ICosmeticWeldBeadFeatureData)

Gets or sets the pitch of intermittent weld beads.

## Syntax

### Visual Basic (Declaration)

```vb
Property Pitch As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmeticWeldBeadFeatureData
Dim value As System.Double

instance.Pitch = value

value = instance.Pitch
```

### C#

```csharp
System.double Pitch {get; set;}
```

### C++/CLI

```cpp
property System.double Pitch {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pitch of intermittent weld beads (see **Remarks**)

## VBA Syntax

See [CosmeticWeldBeadFeatureData::Pitch](ms-its:sldworksapivb6.chm::/sldworks~CosmeticWeldBeadFeatureData~Pitch.html).

## Examples

See [ICosmeticWeldBeadFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticWeldBeadFeatureData.html) examples.

## Remarks

This property is valid only if [ICosmeticWeldBeadFeatureData::GapOrPitch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticWeldBeadFeatureData~GapOrPitch.html) is false and [ICosmeticWeldBeadFeatureData::IntermittentWeld](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticWeldBeadFeatureData~IntermittentWeld.html) is true.

Pitch is the length from the center of one weld bead to the center of the next weld bead.

## See Also

[ICosmeticWeldBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.html)
[ICosmeticWeldBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0

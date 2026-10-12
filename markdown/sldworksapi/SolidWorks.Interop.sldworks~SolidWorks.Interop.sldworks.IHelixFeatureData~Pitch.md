---
title: "Pitch Property (IHelixFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHelixFeatureData"
member: "Pitch"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~Pitch.html"
---

# Pitch Property (IHelixFeatureData)

Gets or sets the pitch of this helix feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Pitch As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IHelixFeatureData
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

Pitch (see **Remarks**)

## VBA Syntax

See [HelixFeatureData::Pitch](ms-its:sldworksapivb6.chm::/sldworks~HelixFeatureData~Pitch.html).

## Examples

[Change Pitch of Helix (C#)](Change_Pitch_of_Helix_Example_CSharp.htm)
[Change Pitch of Helix (VB.NET)](Change_Pitch_of_Helix_Example_VBNET.htm)
[Change Pitch of Helix (VBA)](Change_Pitch_of_Helix_Example_VB.htm)

## Remarks

| For... | This property sets... |
| --- | --- |
| Helixes | Distance between turns |
| Spirals | Radial distance between revolutions of the curve |

**NOTES**:

- If the [helix is defined](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHelixFeatureData~DefinedBy.html) as swHelixDefinedBy_e.swHelixDefinedByHeightAndRevolution, then you cannot change the pitch of the helix.
- If setting a value for pitch for the first region only, then you cannot change diameter, height, or revolution.

## See Also

[IHelixFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData.html)
[IHelixFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0

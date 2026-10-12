---
title: "IntermittentWeld Property (ICosmeticWeldBeadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICosmeticWeldBeadFeatureData"
member: "IntermittentWeld"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~IntermittentWeld.html"
---

# IntermittentWeld Property (ICosmeticWeldBeadFeatureData)

Gets or sets whether to enable intermittent weld properties.

## Syntax

### Visual Basic (Declaration)

```vb
Property IntermittentWeld As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmeticWeldBeadFeatureData
Dim value As System.Boolean

instance.IntermittentWeld = value

value = instance.IntermittentWeld
```

### C#

```csharp
System.bool IntermittentWeld {get; set;}
```

### C++/CLI

```cpp
property System.bool IntermittentWeld {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to enable intermittent weld properties, false to not (see **Remarks**)

## VBA Syntax

See [CosmeticWeldBeadFeatureData::IntermittentWeld](ms-its:sldworksapivb6.chm::/sldworks~CosmeticWeldBeadFeatureData~IntermittentWeld.html).

## Examples

See [ICosmeticWeldBeadFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticWeldBeadFeatureData.html) examples.

## Remarks

If this property is true, you can use the following properties:

- [ICosmeticWeldBeadFeatureData::Gap](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticWeldBeadFeatureData~Gap.html)
- [ICosmeticWeldBeadFeatureData::GapOrPitch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticWeldBeadFeatureData~GapOrPitch.html)
- [ICosmeticWeldBeadFeatureData::Pitch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticWeldBeadFeatureData~Pitch.html)
- [ICosmeticWeldBeadFeatureData::IntermittentWeldLength](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticWeldBeadFeatureData~IntermittentWeldLength.html)
- [ICosmeticWeldBeadFeatureData::Staggered](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticWeldBeadFeatureData~Staggered.html)

## See Also

[ICosmeticWeldBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.html)
[ICosmeticWeldBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0

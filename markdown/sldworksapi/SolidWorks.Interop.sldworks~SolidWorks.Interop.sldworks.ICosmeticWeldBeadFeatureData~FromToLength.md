---
title: "FromToLength Property (ICosmeticWeldBeadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICosmeticWeldBeadFeatureData"
member: "FromToLength"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~FromToLength.html"
---

# FromToLength Property (ICosmeticWeldBeadFeatureData)

Gets or sets whether to enable the from/to length properties.

## Syntax

### Visual Basic (Declaration)

```vb
Property FromToLength As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmeticWeldBeadFeatureData
Dim value As System.Boolean

instance.FromToLength = value

value = instance.FromToLength
```

### C#

```csharp
System.bool FromToLength {get; set;}
```

### C++/CLI

```cpp
property System.bool FromToLength {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to enable the from/to length properties, false to not (see **Remarks**)

## VBA Syntax

See [CosmeticWeldBeadFeatureData::FromToLength](ms-its:sldworksapivb6.chm::/sldworks~CosmeticWeldBeadFeatureData~FromToLength.html).

## Examples

See [ICosmeticWeldBeadFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticWeldBeadFeatureData.html) examples.

## Remarks

This property is valid only if:

- [ICosmeticWeldBeadFeatureData::TangentPropagation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticWeldBeadFeatureData~TangentPropagation.html) is true

- or -

- [ICosmeticWeldBeadFeatureData::Side](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticWeldBeadFeatureData~Side.html) is either [swCosmeticWeldBeadSide_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCosmeticWeldBeadSide_e.html).swCosmeticWeldBeadSide_Selection or swCosmeticWeldBeadSide_e.swCosmeticWeldBeadSide_BothSides.

If this property is true, you can use the following properties:

- [ICosmeticWeldBeadFeatureData::FromToStartPoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticWeldBeadFeatureData~FromToStartPoint.html)
- [ICosmeticWeldBeadFeatureData::FromToReverse](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticWeldBeadFeatureData~FromToReverse.html)
- [ICosmeticWeldBeadFeatureData::FromToWeldLength](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticWeldBeadFeatureData~FromToWeldLength.html)

## See Also

[ICosmeticWeldBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.html)
[ICosmeticWeldBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0

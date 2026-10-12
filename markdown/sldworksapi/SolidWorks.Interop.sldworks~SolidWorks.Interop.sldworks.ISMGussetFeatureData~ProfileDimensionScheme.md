---
title: "ProfileDimensionScheme Property (ISMGussetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISMGussetFeatureData"
member: "ProfileDimensionScheme"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ProfileDimensionScheme.html"
---

# ProfileDimensionScheme Property (ISMGussetFeatureData)

Gets or sets the type of profile dimensioning scheme for this gusset.

## Syntax

### Visual Basic (Declaration)

```vb
Property ProfileDimensionScheme As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISMGussetFeatureData
Dim value As System.Integer

instance.ProfileDimensionScheme = value

value = instance.ProfileDimensionScheme
```

### C#

```csharp
System.int ProfileDimensionScheme {get; set;}
```

### C++/CLI

```cpp
property System.int ProfileDimensionScheme {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of gusset profile dimensioning scheme as defined in [swSheetMetalGussetProfileDimType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalGussetProfileDimType_e.html)

## VBA Syntax

See [SMGussetFeatureData::ProfileDimensionScheme](ms-its:sldworksapivb6.chm::/sldworks~SMGussetFeatureData~ProfileDimensionScheme.html).

## Examples

See the examples for [ISMGussetFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData.html).

## Remarks

See the [ISMGussetFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.html) Remarks.

## See Also

[ISMGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.html)
[ISMGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData_members.html)
[ISMGussetFeatureData::ProfileAngleDim Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ProfileAngleDim.html)
[ISMGussetFeatureData::ProfileHeightDim Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ProfileHeightDim.html)
[ISMGussetFeatureData::ProfileLengthDim Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ProfileLengthDim.html)
[ISMGussetFeatureData::FlipDimSides Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~FlipDimSides.html)
[ISMGussetFeatureData::UseAngleDimForProfile Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~UseAngleDimForProfile.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0

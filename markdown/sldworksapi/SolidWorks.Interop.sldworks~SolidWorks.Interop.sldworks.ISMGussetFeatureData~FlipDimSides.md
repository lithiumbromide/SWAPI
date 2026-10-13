---
title: "FlipDimSides Property (ISMGussetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISMGussetFeatureData"
member: "FlipDimSides"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~FlipDimSides.html"
---

# FlipDimSides Property (ISMGussetFeatureData)

Gets or sets whether to swap the gusset legs in the dimensioning scheme.

## Syntax

### Visual Basic (Declaration)

```vb
Property FlipDimSides As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISMGussetFeatureData
Dim value As System.Boolean

instance.FlipDimSides = value

value = instance.FlipDimSides
```

### C#

```csharp
System.bool FlipDimSides {get; set;}
```

### C++/CLI

```cpp
property System.bool FlipDimSides {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to swap the gusset legs in the dimensioning scheme, false to not

## VBA Syntax

See [SMGussetFeatureData::FlipDimSides](ms-its:sldworksapivb6.chm::/sldworks~SMGussetFeatureData~FlipDimSides.html).

## Examples

See the examples for [ISMGussetFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData.html).

## Remarks

[ISMGussetFeatureData::ProfileHeightDim](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData~ProfileHeightDim.html) corresponds to the d2 leg and [ISMGussetFeatureData::ProfileLengthDim](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData~ProfileLengthDim.html) corresponds to the d1 leg in the dimensioning scheme. This property allows you to swap the d2 and d1 legs in order to change the gusset dimension profile.

See the [ISMGussetFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.html) Remarks.

## See Also

[ISMGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.html)
[ISMGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData_members.html)
[ISMGussetFeatureData::ProfileAngleDim Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ProfileAngleDim.html)
[ISMGussetFeatureData::ProfileDimensionScheme Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ProfileDimensionScheme.html)
[ISMGussetFeatureData::UseAngleDimForProfile Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~UseAngleDimForProfile.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0

---
title: "ProfileAngleDim Property (ISMGussetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISMGussetFeatureData"
member: "ProfileAngleDim"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ProfileAngleDim.html"
---

# ProfileAngleDim Property (ISMGussetFeatureData)

Gets or sets the angle formed by the intersection of this gusset with one face adjacent to the bend of the sheet metal part.

## Syntax

### Visual Basic (Declaration)

```vb
Property ProfileAngleDim As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISMGussetFeatureData
Dim value As System.Double

instance.ProfileAngleDim = value

value = instance.ProfileAngleDim
```

### C#

```csharp
System.double ProfileAngleDim {get; set;}
```

### C++/CLI

```cpp
property System.double ProfileAngleDim {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Angle formed where gusset intersects the sheet metal part

## VBA Syntax

See [SMGussetFeatureData::ProfileAngleDim](ms-its:sldworksapivb6.chm::/sldworks~SMGussetFeatureData~ProfileAngleDim.html).

## Examples

See the examples for [ISMGussetFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData.html).

## Remarks

This property is valid only if [ISMGussetFeatureData::UseAngleDimForProfile](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData~UseAngleDimForProfile.html) is true and [ISMGussetFeatureData::ProfileDimensionScheme](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData~ProfileDimensionScheme.html) is set to 1.

See the [ISMGussetFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.html) Remarks.

## See Also

[ISMGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.html)
[ISMGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData_members.html)
[ISMGussetFeatureData::ProfileHeightDim Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ProfileHeightDim.html)
[ISMGussetFeatureData::ProfileLengthDim Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ProfileLengthDim.html)
[ISMGussetFeatureData::FlipDimSides Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~FlipDimSides.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0

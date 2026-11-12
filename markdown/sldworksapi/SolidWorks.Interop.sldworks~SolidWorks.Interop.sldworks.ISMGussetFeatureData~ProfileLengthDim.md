---
title: "ProfileLengthDim Property (ISMGussetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISMGussetFeatureData"
member: "ProfileLengthDim"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ProfileLengthDim.html"
---

# ProfileLengthDim Property (ISMGussetFeatureData)

Gets or sets the length of the d1 leg of this gusset.

## Syntax

### Visual Basic (Declaration)

```vb
Property ProfileLengthDim As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISMGussetFeatureData
Dim value As System.Double

instance.ProfileLengthDim = value

value = instance.ProfileLengthDim
```

### C#

```csharp
System.double ProfileLengthDim {get; set;}
```

### C++/CLI

```cpp
property System.double ProfileLengthDim {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Length of d1 leg

## VBA Syntax

See [SMGussetFeatureData::ProfileLengthDim](ms-its:sldworksapivb6.chm::/sldworks~SMGussetFeatureData~ProfileLengthDim.html).

## Examples

See the examples for [ISMGussetFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData.html).

## Remarks

This property is valid only if [ISMGussetFeatureData::ProfileDimensionScheme](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData~ProfileDimensionScheme.html) is set to 1.

See the [ISMGussetFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.html) Remarks.

## See Also

[ISMGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.html)
[ISMGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData_members.html)
[ISMGussetFeatureData::FlipDimSides Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~FlipDimSides.html)
[ISMGussetFeatureData::ProfileAngleDim Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ProfileAngleDim.html)
[ISMGussetFeatureData::ProfileHeightDim Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ProfileHeightDim.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0

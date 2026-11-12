---
title: "ProfileHeightDim Property (ISMGussetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISMGussetFeatureData"
member: "ProfileHeightDim"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ProfileHeightDim.html"
---

# ProfileHeightDim Property (ISMGussetFeatureData)

Gets or sets the length of the d2 leg of this gusset.

## Syntax

### Visual Basic (Declaration)

```vb
Property ProfileHeightDim As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISMGussetFeatureData
Dim value As System.Double

instance.ProfileHeightDim = value

value = instance.ProfileHeightDim
```

### C#

```csharp
System.double ProfileHeightDim {get; set;}
```

### C++/CLI

```cpp
property System.double ProfileHeightDim {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Length of d2 leg

## VBA Syntax

See [SMGussetFeatureData::ProfileHeightDim](ms-its:sldworksapivb6.chm::/sldworks~SMGussetFeatureData~ProfileHeightDim.html).

## Examples

See the examples for [ISMGussetFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData.html).

## Remarks

This property is valid only if [ISMGussetFeatureData::ProfileDimensionScheme](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData~ProfileDimensionScheme.html) is set to 1.

See the [ISMGussetFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.html) Remarks.

## See Also

[ISMGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.html)
[ISMGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData_members.html)
[ISMGussetFeatureData::ProfileAngleDim Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ProfileAngleDim.html)
[ISMGussetFeatureData::ProfileLengthDim Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ProfileLengthDim.html)
[ISMGussetFeatureData::FlipDimSides Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~FlipDimSides.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0

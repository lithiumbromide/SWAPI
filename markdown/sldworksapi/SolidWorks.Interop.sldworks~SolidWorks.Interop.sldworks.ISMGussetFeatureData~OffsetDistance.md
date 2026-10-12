---
title: "OffsetDistance Property (ISMGussetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISMGussetFeatureData"
member: "OffsetDistance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~OffsetDistance.html"
---

# OffsetDistance Property (ISMGussetFeatureData)

Gets or sets the offset of the gusset's section plane from a specified [reference point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData~ReferencePoint.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property OffsetDistance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISMGussetFeatureData
Dim value As System.Double

instance.OffsetDistance = value

value = instance.OffsetDistance
```

### C#

```csharp
System.double OffsetDistance {get; set;}
```

### C++/CLI

```cpp
property System.double OffsetDistance {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Gusset section plane offset

## VBA Syntax

See [SMGussetFeatureData::OffsetDistance](ms-its:sldworksapivb6.chm::/sldworks~SMGussetFeatureData~OffsetDistance.html).

## Examples

See the examples for [ISMGussetFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData.html).

## Remarks

This property is valid only if [ISMGussetFeatureData::UseOffset](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData~UseOffset.html) is true.

## See Also

[ISMGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.html)
[ISMGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData_members.html)
[ISMGussetFeatureData::FlipOffset Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~FlipOffset.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0

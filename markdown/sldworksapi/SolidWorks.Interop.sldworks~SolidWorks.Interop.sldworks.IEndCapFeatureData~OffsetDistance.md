---
title: "OffsetDistance Property (IEndCapFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IEndCapFeatureData"
member: "OffsetDistance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData~OffsetDistance.html"
---

# OffsetDistance Property (IEndCapFeatureData)

Gets or sets the offset distance for this end-cap feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property OffsetDistance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IEndCapFeatureData
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

Offset distance

## VBA Syntax

See [EndCapFeatureData::OffsetDistance](ms-its:sldworksapivb6.chm::/sldworks~EndCapFeatureData~OffsetDistance.html).

## Examples

See the [IEndCapFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEndCapFeatureData.html) examples.

## Remarks

[IEndCapFeatureData::UseThicknessRatioForOffset](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEndCapFeatureData~UseThicknessRatioForOffset.html) must be set to false for this property to have an effect.

## See Also

[IEndCapFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData.html)
[IEndCapFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0

---
title: "BendRadius Property (IMiterFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMiterFlangeFeatureData"
member: "BendRadius"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~BendRadius.html"
---

# BendRadius Property (IMiterFlangeFeatureData)

Gets or sets the bend radius for this miter flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property BendRadius As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMiterFlangeFeatureData
Dim value As System.Double

instance.BendRadius = value

value = instance.BendRadius
```

### C#

```csharp
System.double BendRadius {get; set;}
```

### C++/CLI

```cpp
property System.double BendRadius {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Bend radius in meters

## VBA Syntax

See [MiterFlangeFeatureData::BendRadius](ms-its:sldworksapivb6.chm::/sldworks~MiterFlangeFeatureData~BendRadius.html).

## Examples

See [IMiterFlangeFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMiterFlangeFeatureData.html) examples.

## Remarks

This property is only used when [IMiterFlangeFeatureData::UseDefaultBendRadius](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMiterFlangeFeatureData~UseDefaultBendRadius.html) is True.

## See Also

[IMiterFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData.html)
[IMiterFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData_members.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2

---
title: "InnerCornerFilletRadius Property (ISMGussetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISMGussetFeatureData"
member: "InnerCornerFilletRadius"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~InnerCornerFilletRadius.html"
---

# InnerCornerFilletRadius Property (ISMGussetFeatureData)

Gets or sets the fillet radius for the inner corners of this gusset.

## Syntax

### Visual Basic (Declaration)

```vb
Property InnerCornerFilletRadius As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISMGussetFeatureData
Dim value As System.Double

instance.InnerCornerFilletRadius = value

value = instance.InnerCornerFilletRadius
```

### C#

```csharp
System.double InnerCornerFilletRadius {get; set;}
```

### C++/CLI

```cpp
property System.double InnerCornerFilletRadius {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Inner corner fillet radius

## VBA Syntax

See [SMGussetFeatureData::InnerCornerFilletRadius](ms-its:sldworksapivb6.chm::/sldworks~SMGussetFeatureData~InnerCornerFilletRadius.html).

## Examples

See the examples for [ISMGussetFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData.html).

## Remarks

This property is valid only if [ISMGussetFeatureData::FilletInnerCorners](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData~FilletInnerCorners.html) is true.

## See Also

[ISMGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.html)
[ISMGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData_members.html)
[ISMGussetFeatureData::OuterCornerFilletRadius Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~OuterCornerFilletRadius.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0

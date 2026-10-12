---
title: "OuterCornerFilletRadius Property (ISMGussetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISMGussetFeatureData"
member: "OuterCornerFilletRadius"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~OuterCornerFilletRadius.html"
---

# OuterCornerFilletRadius Property (ISMGussetFeatureData)

Gets or sets the fillet radius for the outer corners of this gusset.

## Syntax

### Visual Basic (Declaration)

```vb
Property OuterCornerFilletRadius As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISMGussetFeatureData
Dim value As System.Double

instance.OuterCornerFilletRadius = value

value = instance.OuterCornerFilletRadius
```

### C#

```csharp
System.double OuterCornerFilletRadius {get; set;}
```

### C++/CLI

```cpp
property System.double OuterCornerFilletRadius {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Outer corner fillet radius

## VBA Syntax

See [SMGussetFeatureData::OuterCornerFilletRadius](ms-its:sldworksapivb6.chm::/sldworks~SMGussetFeatureData~OuterCornerFilletRadius.html).

## Examples

See the examples for [ISMGussetFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData.html).

## Remarks

This property is valid only if [ISMGussetFeatureData::FilletOuterCorners](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData~FilletOuterCorners.html) is true.

## See Also

[ISMGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.html)
[ISMGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData_members.html)
[ISMGussetFeatureData::InnerCornerFilletRadius Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~InnerCornerFilletRadius.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0

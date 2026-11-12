---
title: "FlipOffset Property (ISMGussetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISMGussetFeatureData"
member: "FlipOffset"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~FlipOffset.html"
---

# FlipOffset Property (ISMGussetFeatureData)

Gets or sets whether to offset the gusset section plane on the opposite side of the specified [reference point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData~ReferencePoint.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property FlipOffset As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISMGussetFeatureData
Dim value As System.Boolean

instance.FlipOffset = value

value = instance.FlipOffset
```

### C#

```csharp
System.bool FlipOffset {get; set;}
```

### C++/CLI

```cpp
property System.bool FlipOffset {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to offset the gusset section plane on the opposite side of the reference point, false to not

## VBA Syntax

See [SMGussetFeatureData::FlipOffset](ms-its:sldworksapivb6.chm::/sldworks~SMGussetFeatureData~FlipOffset.html).

## Examples

See the examples for [ISMGussetFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData.html).

## Remarks

This property is valid only if [ISMGussetFeatureData::UseOffset](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData~UseOffset.html) is true.

## See Also

[ISMGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.html)
[ISMGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData_members.html)
[ISMGussetFeatureData::OffsetDistance Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~OffsetDistance.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0

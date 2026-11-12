---
title: "BeltThickness Property (IBeltChainFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBeltChainFeatureData"
member: "BeltThickness"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~BeltThickness.html"
---

# BeltThickness Property (IBeltChainFeatureData)

Gets and sets the belt thickness.

## Syntax

### Visual Basic (Declaration)

```vb
Property BeltThickness As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IBeltChainFeatureData
Dim value As System.Double

instance.BeltThickness = value

value = instance.BeltThickness
```

### C#

```csharp
System.double BeltThickness {get; set;}
```

### C++/CLI

```cpp
property System.double BeltThickness {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Belt thickness

## VBA Syntax

See [BeltChainFeatureData::BeltThickness](ms-its:sldworksapivb6.chm::/sldworks~BeltChainFeatureData~BeltThickness.html).

## Examples

See the [IBeltChainFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.html) examples.

## Remarks

This property is valid only if [IBeltChainFeatureData::UseBeltThickness](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~UseBeltThickness.html) is true. The belt curve is offset from the cylindrical faces of the pulleys by one half the specified belt thickness.

## See Also

[IBeltChainFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.html)
[IBeltChainFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30

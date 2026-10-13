---
title: "BeltLength Property (IBeltChainFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBeltChainFeatureData"
member: "BeltLength"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~BeltLength.html"
---

# BeltLength Property (IBeltChainFeatureData)

Gets and sets the belt length.

## Syntax

### Visual Basic (Declaration)

```vb
Property BeltLength As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IBeltChainFeatureData
Dim value As System.Double

instance.BeltLength = value

value = instance.BeltLength
```

### C#

```csharp
System.double BeltLength {get; set;}
```

### C++/CLI

```cpp
property System.double BeltLength {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Belt length

## VBA Syntax

See [BeltChainFeatureData::BeltLength](ms-its:sldworksapivb6.chm::/sldworks~BeltChainFeatureData~BeltLength.html).

## Examples

See the [IBeltChainFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.html) examples.

## Remarks

This property can only be set if [IBeltChainFeatureData::DrivingLength](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~DrivingLength.html) is set to true.

## See Also

[IBeltChainFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.html)
[IBeltChainFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30

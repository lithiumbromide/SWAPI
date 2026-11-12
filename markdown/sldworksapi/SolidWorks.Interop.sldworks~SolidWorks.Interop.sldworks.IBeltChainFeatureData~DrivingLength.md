---
title: "DrivingLength Property (IBeltChainFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBeltChainFeatureData"
member: "DrivingLength"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~DrivingLength.html"
---

# DrivingLength Property (IBeltChainFeatureData)

Gets and sets whether belt length can be changed.

## Syntax

### Visual Basic (Declaration)

```vb
Property DrivingLength As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBeltChainFeatureData
Dim value As System.Boolean

instance.DrivingLength = value

value = instance.DrivingLength
```

### C#

```csharp
System.bool DrivingLength {get; set;}
```

### C++/CLI

```cpp
property System.bool DrivingLength {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to allow belt length changes, false to not

## VBA Syntax

See [BeltChainFeatureData::DrivingLength](ms-its:sldworksapivb6.chm::/sldworks~BeltChainFeatureData~DrivingLength.html).

## Examples

See the [IBeltChainFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.html) examples.

## Remarks

If this property is true, then use [IBeltChainFeatureData::BeltLength](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~BeltLength.html) to set the belt length. Pulley positions adjust if at least one pulley has an appropriate degree of freedom.

## See Also

[IBeltChainFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.html)
[IBeltChainFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30

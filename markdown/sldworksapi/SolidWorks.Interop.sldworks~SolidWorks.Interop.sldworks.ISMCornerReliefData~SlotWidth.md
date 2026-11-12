---
title: "SlotWidth Property (ISMCornerReliefData)"
project: "SOLIDWORKS API Help"
interface: "ISMCornerReliefData"
member: "SlotWidth"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData~SlotWidth.html"
---

# SlotWidth Property (ISMCornerReliefData)

Gets and sets the width of this corner relief slot.

## Syntax

### Visual Basic (Declaration)

```vb
Property SlotWidth As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISMCornerReliefData
Dim value As System.Double

instance.SlotWidth = value

value = instance.SlotWidth
```

### C#

```csharp
System.double SlotWidth {get; set;}
```

### C++/CLI

```cpp
property System.double SlotWidth {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Corner relief slot width (see **Remarks**)

## VBA Syntax

See [SMCornerReliefData::SlotWidth](ms-its:sldworksapivb6.chm::/sldworks~SMCornerReliefData~SlotWidth.html).

## Examples

See the [ICornerReliefFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.html) examples.

## Remarks

This property is valid only if [ISMCornerReliefData::ReliefType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData~ReliefType.html) is set to one of the following [swCornerReliefType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerReliefType_e.html) members. If...:

- swCornerCircularRelief, then this property returns a radial slot width value.
- swCornerObroundRelief, then this property returns a linear slot width value.

## See Also

[ISMCornerReliefData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData.html)
[ISMCornerReliefData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30

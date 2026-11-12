---
title: "CornerFilletDiameter Property (ISMCornerReliefData)"
project: "SOLIDWORKS API Help"
interface: "ISMCornerReliefData"
member: "CornerFilletDiameter"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData~CornerFilletDiameter.html"
---

# CornerFilletDiameter Property (ISMCornerReliefData)

Gets and sets the diameter of the filleted corner.

## Syntax

### Visual Basic (Declaration)

```vb
Property CornerFilletDiameter As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISMCornerReliefData
Dim value As System.Double

instance.CornerFilletDiameter = value

value = instance.CornerFilletDiameter
```

### C#

```csharp
System.double CornerFilletDiameter {get; set;}
```

### C++/CLI

```cpp
property System.double CornerFilletDiameter {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Diameter

## VBA Syntax

See [SMCornerReliefData::CornerFilletDiameter](ms-its:sldworksapivb6.chm::/sldworks~SMCornerReliefData~CornerFilletDiameter.html).

## Examples

See the [ICornerReliefFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.html) examples.

## Remarks

This property is valid only if:

- [ISMCornerReliefData::AddFilletedCorners](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData~AddFilletedCorners.html) is true,

- And -

- [ISMCornerReliefData::ReliefType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData~ReliefType.html) is set to [swCornerReliefType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerReliefType_e.html).swCornerRectangularRelief.

## See Also

[ISMCornerReliefData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData.html)
[ISMCornerReliefData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30

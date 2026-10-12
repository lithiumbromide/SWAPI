---
title: "AddFilletedCorners Property (ISMCornerReliefData)"
project: "SOLIDWORKS API Help"
interface: "ISMCornerReliefData"
member: "AddFilletedCorners"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData~AddFilletedCorners.html"
---

# AddFilletedCorners Property (ISMCornerReliefData)

Gets and sets whether to fillet the corner relief corners.

## Syntax

### Visual Basic (Declaration)

```vb
Property AddFilletedCorners As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISMCornerReliefData
Dim value As System.Boolean

instance.AddFilletedCorners = value

value = instance.AddFilletedCorners
```

### C#

```csharp
System.bool AddFilletedCorners {get; set;}
```

### C++/CLI

```cpp
property System.bool AddFilletedCorners {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to fillet the corner relief corners, false to not

## VBA Syntax

See [SMCornerReliefData::AddFilletedCorners](ms-its:sldworksapivb6.chm::/sldworks~SMCornerReliefData~AddFilletedCorners.html).

## Examples

See the [ICornerReliefFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.html) examples.

## Remarks

This property is valid only if [ISMCornerReliefData::ReliefType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData~ReliefType.html) is set to [swCornerReliefType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerReliefType_e.html).swCornerRectangularRelief.

## See Also

[ISMCornerReliefData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData.html)
[ISMCornerReliefData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData_members.html)
[ISMCornerReliefData::CornerFilletDiameter Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData~CornerFilletDiameter.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30

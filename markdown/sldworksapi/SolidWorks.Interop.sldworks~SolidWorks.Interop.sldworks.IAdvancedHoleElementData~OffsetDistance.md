---
title: "OffsetDistance Property (IAdvancedHoleElementData)"
project: "SOLIDWORKS API Help"
interface: "IAdvancedHoleElementData"
member: "OffsetDistance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~OffsetDistance.html"
---

# OffsetDistance Property (IAdvancedHoleElementData)

Gets or sets the offset distance for this Advanced Hole element.

## Syntax

### Visual Basic (Declaration)

```vb
Property OffsetDistance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IAdvancedHoleElementData
Dim value As System.Double

instance.OffsetDistance = value

value = instance.OffsetDistance
```

### C#

```csharp
System.double OffsetDistance {get; set;}
```

### C++/CLI

```cpp
property System.double OffsetDistance {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Offset distance (see **Remarks**)

## VBA Syntax

See [AdvancedHoleElementData::OffsetDistance](ms-its:sldworksapivb6.chm::/sldworks~AdvancedHoleElementData~OffsetDistance.html).

## Remarks

This property is valid only when [IAdvancedHoleElementData::EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~EndCondition.html) is set to [swEndConditions_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swEndConditions_e.html).swEndCondOffsetFromSurface.

You can set this property only if this hole element's corresponding property is set to false:

- [ICounterboreElementData::UseStandardDepth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICounterboreElementData~UseStandardDepth.html)
- [ICountersinkElementData::UseStandardDepth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICountersinkElementData~UseStandardDepth.html)
- [ITaperedTapElementData::UseStandardDepth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaperedTapElementData~UseStandardDepth.html)

## See Also

[IAdvancedHoleElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData.html)
[IAdvancedHoleElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData_members.html)
[IAdvancedHoleElementData::OffsetReverseDirection Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~OffsetReverseDirection.html)
[IStraightTapElementData::Equation Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData~Equation.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0

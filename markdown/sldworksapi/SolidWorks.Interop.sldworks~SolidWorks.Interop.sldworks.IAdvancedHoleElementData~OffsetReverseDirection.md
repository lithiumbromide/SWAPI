---
title: "OffsetReverseDirection Property (IAdvancedHoleElementData)"
project: "SOLIDWORKS API Help"
interface: "IAdvancedHoleElementData"
member: "OffsetReverseDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~OffsetReverseDirection.html"
---

# OffsetReverseDirection Property (IAdvancedHoleElementData)

Gets or sets whether to reverse the offset direction for this Advanced Hole element.

## Syntax

### Visual Basic (Declaration)

```vb
Property OffsetReverseDirection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAdvancedHoleElementData
Dim value As System.Boolean

instance.OffsetReverseDirection = value

value = instance.OffsetReverseDirection
```

### C#

```csharp
System.bool OffsetReverseDirection {get; set;}
```

### C++/CLI

```cpp
property System.bool OffsetReverseDirection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to reverse the offset direction, false to not

## VBA Syntax

See [AdvancedHoleElementData::OffsetReverseDirection](ms-its:sldworksapivb6.chm::/sldworks~AdvancedHoleElementData~OffsetReverseDirection.html).

## Remarks

This property is valid only when [IAdvancedHoleElementData::EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~EndCondition.html) is set to [swEndConditions_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swEndConditions_e.html).swEndCondOffsetFromSurface.

## See Also

[IAdvancedHoleElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData.html)
[IAdvancedHoleElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData_members.html)
[IAdvancedHoleElementData::OffsetDistance Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~OffsetDistance.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0

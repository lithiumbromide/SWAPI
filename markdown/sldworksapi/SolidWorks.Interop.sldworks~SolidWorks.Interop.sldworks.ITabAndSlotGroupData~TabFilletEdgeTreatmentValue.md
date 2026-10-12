---
title: "TabFilletEdgeTreatmentValue Property (ITabAndSlotGroupData)"
project: "SOLIDWORKS API Help"
interface: "ITabAndSlotGroupData"
member: "TabFilletEdgeTreatmentValue"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~TabFilletEdgeTreatmentValue.html"
---

# TabFilletEdgeTreatmentValue Property (ITabAndSlotGroupData)

Gets or sets the fillet radius for tab edges.

## Syntax

### Visual Basic (Declaration)

```vb
Property TabFilletEdgeTreatmentValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITabAndSlotGroupData
Dim value As System.Double

instance.TabFilletEdgeTreatmentValue = value

value = instance.TabFilletEdgeTreatmentValue
```

### C#

```csharp
System.double TabFilletEdgeTreatmentValue {get; set;}
```

### C++/CLI

```cpp
property System.double TabFilletEdgeTreatmentValue {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Fillet radius

## VBA Syntax

See [TabAndSlotGroupData::TabFilletEdgeTreatmentValue](ms-its:sldworksapivb6.chm::/sldworks~TabAndSlotGroupData~TabFilletEdgeTreatmentValue.html).

## Remarks

This property is valid only if [ITabAndSlotGroupData::TabEdgesType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~TabEdgesType.html) is set to [swTabEdgesType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTabEdgesType_e.html).FilletEdge.

## See Also

[ITabAndSlotGroupData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData.html)
[ITabAndSlotGroupData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0

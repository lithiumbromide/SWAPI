---
title: "TabOffsetValue Property (ITabAndSlotGroupData)"
project: "SOLIDWORKS API Help"
interface: "ITabAndSlotGroupData"
member: "TabOffsetValue"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~TabOffsetValue.html"
---

# TabOffsetValue Property (ITabAndSlotGroupData)

Gets or sets the tab offset value.

## Syntax

### Visual Basic (Declaration)

```vb
Property TabOffsetValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITabAndSlotGroupData
Dim value As System.Double

instance.TabOffsetValue = value

value = instance.TabOffsetValue
```

### C#

```csharp
System.double TabOffsetValue {get; set;}
```

### C++/CLI

```cpp
property System.double TabOffsetValue {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Tab offset value

## VBA Syntax

See [TabAndSlotGroupData::TabOffsetValue](ms-its:sldworksapivb6.chm::/sldworks~TabAndSlotGroupData~TabOffsetValue.html).

## Remarks

This property is:

- measured from [ITabAndSlotGroupData::SelectionSlotFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~SelectionSlotFace.html)

-and-

- valid only if [ITabAndSlotGroupData::TabHeightType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~TabHeightType.html) is set to [swTabSlotFeatureHeightType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTabSlotFeatureHeightType_e.html).OffsetFromSurface.

## See Also

[ITabAndSlotGroupData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData.html)
[ITabAndSlotGroupData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0

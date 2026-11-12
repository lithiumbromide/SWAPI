---
title: "TabReverseDirection Property (ITabAndSlotGroupData)"
project: "SOLIDWORKS API Help"
interface: "ITabAndSlotGroupData"
member: "TabReverseDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~TabReverseDirection.html"
---

# TabReverseDirection Property (ITabAndSlotGroupData)

Gets or sets whether to reverse the tab offset from surface value.

## Syntax

### Visual Basic (Declaration)

```vb
Property TabReverseDirection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITabAndSlotGroupData
Dim value As System.Boolean

instance.TabReverseDirection = value

value = instance.TabReverseDirection
```

### C#

```csharp
System.bool TabReverseDirection {get; set;}
```

### C++/CLI

```cpp
property System.bool TabReverseDirection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to reverse the tab offset from surface value, false to not

## VBA Syntax

See [TabAndSlotGroupData::TabReverseDirection](ms-its:sldworksapivb6.chm::/sldworks~TabAndSlotGroupData~TabReverseDirection.html).

## Remarks

This property is valid only if valid only if [ITabAndSlotGroupData::TabHeightType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~TabHeightType.html) is set to [swTabSlotFeatureHeightType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTabSlotFeatureHeightType_e.html).OffsetFromSurface.

## See Also

[ITabAndSlotGroupData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData.html)
[ITabAndSlotGroupData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0

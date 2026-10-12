---
title: "TabHeightType Property (ITabAndSlotGroupData)"
project: "SOLIDWORKS API Help"
interface: "ITabAndSlotGroupData"
member: "TabHeightType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~TabHeightType.html"
---

# TabHeightType Property (ITabAndSlotGroupData)

Gets or sets the type of tab height.

## Syntax

### Visual Basic (Declaration)

```vb
Property TabHeightType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITabAndSlotGroupData
Dim value As System.Integer

instance.TabHeightType = value

value = instance.TabHeightType
```

### C#

```csharp
System.int TabHeightType {get; set;}
```

### C++/CLI

```cpp
property System.int TabHeightType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Tab height type as defined in [swTabSlotFeatureHeightType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTabSlotFeatureHeightType_e.html)

## VBA Syntax

See [TabAndSlotGroupData::TabHeightType](ms-its:sldworksapivb6.chm::/sldworks~TabAndSlotGroupData~TabHeightType.html).

## Remarks

If you set this property to swTabSlotFeatureHeightType_e:

- Blind, then use [ITabAndSlotGroupData::TabHeightValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~TabHeightValue.html) to set the tab height.
- OffsetFromSurface, then use [ITabAndSlotGroupData::TabOffsetValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~TabOffsetValue.html) to set the tab offset value as measured from the slot face. Also set [ITabAndSlotGroupData::TabReverseDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~TabReverseDirection.html).
- UpToSurface, then the tab height is automatically set to the distance up to the slot face.

## See Also

[ITabAndSlotGroupData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData.html)
[ITabAndSlotGroupData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0

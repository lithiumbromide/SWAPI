---
title: "TabHeightValue Property (ITabAndSlotGroupData)"
project: "SOLIDWORKS API Help"
interface: "ITabAndSlotGroupData"
member: "TabHeightValue"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~TabHeightValue.html"
---

# TabHeightValue Property (ITabAndSlotGroupData)

Gets or sets the tab height.

## Syntax

### Visual Basic (Declaration)

```vb
Property TabHeightValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITabAndSlotGroupData
Dim value As System.Double

instance.TabHeightValue = value

value = instance.TabHeightValue
```

### C#

```csharp
System.double TabHeightValue {get; set;}
```

### C++/CLI

```cpp
property System.double TabHeightValue {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Tab height

## VBA Syntax

See [TabAndSlotGroupData::TabHeightValue](ms-its:sldworksapivb6.chm::/sldworks~TabAndSlotGroupData~TabHeightValue.html).

## Remarks

This property is valid only if [ITabAndSlotGroupData::TabHeightType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~TabHeightType.html) is set to [swTabSlotFeatureHeightType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTabSlotFeatureHeightType_e.html).Blind.

See the Remarks for ITabAndSlotGroupData::TabHeightType.

## See Also

[ITabAndSlotGroupData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData.html)
[ITabAndSlotGroupData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0

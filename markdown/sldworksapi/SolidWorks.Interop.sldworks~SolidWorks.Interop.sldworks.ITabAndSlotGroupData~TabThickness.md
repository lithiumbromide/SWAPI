---
title: "TabThickness Property (ITabAndSlotGroupData)"
project: "SOLIDWORKS API Help"
interface: "ITabAndSlotGroupData"
member: "TabThickness"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~TabThickness.html"
---

# TabThickness Property (ITabAndSlotGroupData)

Gets or sets the tab thickness.

## Syntax

### Visual Basic (Declaration)

```vb
Property TabThickness As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITabAndSlotGroupData
Dim value As System.Double

instance.TabThickness = value

value = instance.TabThickness
```

### C#

```csharp
System.double TabThickness {get; set;}
```

### C++/CLI

```cpp
property System.double TabThickness {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Tab thickness

## VBA Syntax

See [TabAndSlotGroupData::TabThickness](ms-its:sldworksapivb6.chm::/sldworks~TabAndSlotGroupData~TabThickness.html).

## Remarks

This property defines the thickness of [ITabAndSlotGroupData::TabFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~TabFace.html), which is a planar face shared with [ITabAndSlotGroupData::SelectionTabEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~SelectionTabEdge.html).

## See Also

[ITabAndSlotGroupData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData.html)
[ITabAndSlotGroupData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0

---
title: "TabFace Property (ITabAndSlotGroupData)"
project: "SOLIDWORKS API Help"
interface: "ITabAndSlotGroupData"
member: "TabFace"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~TabFace.html"
---

# TabFace Property (ITabAndSlotGroupData)

Gets or sets the tab face that defines the tab thickness.

## Syntax

### Visual Basic (Declaration)

```vb
Property TabFace As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ITabAndSlotGroupData
Dim value As System.Object

instance.TabFace = value

value = instance.TabFace
```

### C#

```csharp
System.object TabFace {get; set;}
```

### C++/CLI

```cpp
property System.Object^ TabFace {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)

## VBA Syntax

See [TabAndSlotGroupData::TabFace](ms-its:sldworksapivb6.chm::/sldworks~TabAndSlotGroupData~TabFace.html).

## Remarks

The value of this property is a planar face that is shared with [ITabAndSlotGroupData::SelectionTabEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~SelectionTabEdge.html) of thickness, [ITabAndSlotGroupData::TabThickness](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~TabThickness.html).

## See Also

[ITabAndSlotGroupData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData.html)
[ITabAndSlotGroupData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0

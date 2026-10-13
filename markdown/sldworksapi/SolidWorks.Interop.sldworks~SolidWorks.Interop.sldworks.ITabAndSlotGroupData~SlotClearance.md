---
title: "SlotClearance Property (ITabAndSlotGroupData)"
project: "SOLIDWORKS API Help"
interface: "ITabAndSlotGroupData"
member: "SlotClearance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~SlotClearance.html"
---

# SlotClearance Property (ITabAndSlotGroupData)

Gets or sets the offset of the slots relative to the tabs.

## Syntax

### Visual Basic (Declaration)

```vb
Property SlotClearance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITabAndSlotGroupData
Dim value As System.Double

instance.SlotClearance = value

value = instance.SlotClearance
```

### C#

```csharp
System.double SlotClearance {get; set;}
```

### C++/CLI

```cpp
property System.double SlotClearance {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Slot clearance

## VBA Syntax

See [TabAndSlotGroupData::SlotClearance](ms-its:sldworksapivb6.chm::/sldworks~TabAndSlotGroupData~SlotClearance.html).

## Remarks

This property allows you to make the slots larger than the tabs.

## See Also

[ITabAndSlotGroupData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData.html)
[ITabAndSlotGroupData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0

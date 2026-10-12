---
title: "D1OffsetFromStart Property (ITabAndSlotGroupData)"
project: "SOLIDWORKS API Help"
interface: "ITabAndSlotGroupData"
member: "D1OffsetFromStart"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~D1OffsetFromStart.html"
---

# D1OffsetFromStart Property (ITabAndSlotGroupData)

Gets or sets the starting offset of the tabs/slots in this group.

## Syntax

### Visual Basic (Declaration)

```vb
Property D1OffsetFromStart As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITabAndSlotGroupData
Dim value As System.Double

instance.D1OffsetFromStart = value

value = instance.D1OffsetFromStart
```

### C#

```csharp
System.double D1OffsetFromStart {get; set;}
```

### C++/CLI

```cpp
property System.double D1OffsetFromStart {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Distance from the edge where to start the tabs and slots

## VBA Syntax

See [TabAndSlotGroupData::D1OffsetFromStart](ms-its:sldworksapivb6.chm::/sldworks~TabAndSlotGroupData~D1OffsetFromStart.html).

## Remarks

This method is valid only if [ITabAndSlotGroupData::Offset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~Offset.html) is set to true.

If you want the tabs/slots to span the entire edge of the model, set both this property and [ITabAndSlotGroupData::D2OffsetFromEnd](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~D2OffsetFromEnd.html) to zero.

## See Also

[ITabAndSlotGroupData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData.html)
[ITabAndSlotGroupData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0

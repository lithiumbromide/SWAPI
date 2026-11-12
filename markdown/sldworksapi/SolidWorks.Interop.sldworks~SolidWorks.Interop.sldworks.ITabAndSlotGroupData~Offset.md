---
title: "Offset Property (ITabAndSlotGroupData)"
project: "SOLIDWORKS API Help"
interface: "ITabAndSlotGroupData"
member: "Offset"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~Offset.html"
---

# Offset Property (ITabAndSlotGroupData)

Gets or sets whether to offset the tabs/slots from the edge of the model.

## Syntax

### Visual Basic (Declaration)

```vb
Property Offset As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITabAndSlotGroupData
Dim value As System.Boolean

instance.Offset = value

value = instance.Offset
```

### C#

```csharp
System.bool Offset {get; set;}
```

### C++/CLI

```cpp
property System.bool Offset {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to offset the tabs/slots, false to not

## VBA Syntax

See [TabAndSlotGroupData::Offset](ms-its:sldworksapivb6.chm::/sldworks~TabAndSlotGroupData~Offset.html).

## Examples

See the [ITabAndSlotFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotFeatureData.html) example.

## Remarks

If you set this property to true, also set:

- [ITabAndSlotGroupData::D1OffsetFromStart](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~D1OffsetFromStart.html)
- [ITabAndSlotGroupData::D2OffsetFromEnd](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~D2OffsetFromEnd.html)

## See Also

[ITabAndSlotGroupData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData.html)
[ITabAndSlotGroupData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0

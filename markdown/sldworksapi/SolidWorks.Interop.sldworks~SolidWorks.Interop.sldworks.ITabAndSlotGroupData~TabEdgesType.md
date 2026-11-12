---
title: "TabEdgesType Property (ITabAndSlotGroupData)"
project: "SOLIDWORKS API Help"
interface: "ITabAndSlotGroupData"
member: "TabEdgesType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~TabEdgesType.html"
---

# TabEdgesType Property (ITabAndSlotGroupData)

Gets or sets the tab edge treatment.

## Syntax

### Visual Basic (Declaration)

```vb
Property TabEdgesType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITabAndSlotGroupData
Dim value As System.Integer

instance.TabEdgesType = value

value = instance.TabEdgesType
```

### C#

```csharp
System.int TabEdgesType {get; set;}
```

### C++/CLI

```cpp
property System.int TabEdgesType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Tab edge treatment as defined in [swTabEdgesType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTabEdgesType_e.html)

## VBA Syntax

See [TabAndSlotGroupData::TabEdgesType](ms-its:sldworksapivb6.chm::/sldworks~TabAndSlotGroupData~TabEdgesType.html).

## See Also

[ITabAndSlotGroupData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData.html)
[ITabAndSlotGroupData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0

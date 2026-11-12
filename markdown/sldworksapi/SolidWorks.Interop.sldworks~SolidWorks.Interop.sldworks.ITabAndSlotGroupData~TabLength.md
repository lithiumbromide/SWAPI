---
title: "TabLength Property (ITabAndSlotGroupData)"
project: "SOLIDWORKS API Help"
interface: "ITabAndSlotGroupData"
member: "TabLength"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~TabLength.html"
---

# TabLength Property (ITabAndSlotGroupData)

Gets or sets the tab length.

## Syntax

### Visual Basic (Declaration)

```vb
Property TabLength As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITabAndSlotGroupData
Dim value As System.Double

instance.TabLength = value

value = instance.TabLength
```

### C#

```csharp
System.double TabLength {get; set;}
```

### C++/CLI

```cpp
property System.double TabLength {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Tab length

## VBA Syntax

See [TabAndSlotGroupData::TabLength](ms-its:sldworksapivb6.chm::/sldworks~TabAndSlotGroupData~TabLength.html).

## See Also

[ITabAndSlotGroupData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData.html)
[ITabAndSlotGroupData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0

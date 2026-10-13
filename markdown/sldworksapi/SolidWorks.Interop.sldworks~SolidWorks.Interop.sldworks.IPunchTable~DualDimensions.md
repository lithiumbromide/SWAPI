---
title: "DualDimensions Property (IPunchTable)"
project: "SOLIDWORKS API Help"
interface: "IPunchTable"
member: "DualDimensions"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable~DualDimensions.html"
---

# DualDimensions Property (IPunchTable)

Gets or sets whether to display dual dimensions in this punch table.

## Syntax

### Visual Basic (Declaration)

```vb
Property DualDimensions As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPunchTable
Dim value As System.Boolean

instance.DualDimensions = value

value = instance.DualDimensions
```

### C#

```csharp
System.bool DualDimensions {get; set;}
```

### C++/CLI

```cpp
property System.bool DualDimensions {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to display dual dimensions, false to not

## VBA Syntax

See [PunchTable::DualDimensions](ms-its:sldworksapivb6.chm::/sldworks~PunchTable~DualDimensions.html).

## Examples

[Insert Punch Table (C#)](Insert_Punch_Table_Example_CSharp.htm)
[Insert Punch Table (VB.NET)](Insert_Punch_Table_Example_VBNET.htm)
[Insert Punch Table (VBA)](Insert_Punch_Table_Example_VB.htm)

## See Also

[IPunchTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable.html)
[IPunchTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable_members.html)
[IPunchTable::ShowUnits Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable~ShowUnits.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0

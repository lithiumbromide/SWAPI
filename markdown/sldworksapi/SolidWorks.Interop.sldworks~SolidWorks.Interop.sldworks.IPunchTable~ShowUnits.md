---
title: "ShowUnits Property (IPunchTable)"
project: "SOLIDWORKS API Help"
interface: "IPunchTable"
member: "ShowUnits"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable~ShowUnits.html"
---

# ShowUnits Property (IPunchTable)

Gets or sets whether to show dual dimension units in this punch table.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShowUnits As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPunchTable
Dim value As System.Boolean

instance.ShowUnits = value

value = instance.ShowUnits
```

### C#

```csharp
System.bool ShowUnits {get; set;}
```

### C++/CLI

```cpp
property System.bool ShowUnits {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to display dual dimension units in the punch table, false to not; valid only if [IPunchTable::DualDimensions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPunchTable~DualDimensions.html) is true

## VBA Syntax

See [PunchTable::ShowUnits](ms-its:sldworksapivb6.chm::/sldworks~PunchTable~ShowUnits.html).

## Examples

[Insert Punch Table (VBA)](Insert_Punch_Table_Example_VB.htm)
[Insert Punch Table (VB.NET)](Insert_Punch_Table_Example_VBNET.htm)
[Insert Punch Table (C#)](Insert_Punch_Table_Example_CSharp.htm)

## See Also

[IPunchTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable.html)
[IPunchTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0

---
title: "StartingValue Property (IPunchTable)"
project: "SOLIDWORKS API Help"
interface: "IPunchTable"
member: "StartingValue"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable~StartingValue.html"
---

# StartingValue Property (IPunchTable)

Gets or sets the starting value for the datum tags of this punch table.

## Syntax

### Visual Basic (Declaration)

```vb
Property StartingValue As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPunchTable
Dim value As System.String

instance.StartingValue = value

value = instance.StartingValue
```

### C#

```csharp
System.string StartingValue {get; set;}
```

### C++/CLI

```cpp
property System.String^ StartingValue {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Letter from A to Z, if the template of this punch table uses letter tags; a positive integer, if it uses number tags (see **Remarks**)

## VBA Syntax

See [PunchTable::StartingValue](ms-its:sldworksapivb6.chm::/sldworks~PunchTable~StartingValue.html).

## Examples

[Insert Punch Table (C#)](Insert_Punch_Table_Example_CSharp.htm)
[Insert Punch Table (VB.NET)](Insert_Punch_Table_Example_VBNET.htm)
[Insert Punch Table (VBA)](Insert_Punch_Table_Example_VB.htm)

## Remarks

See [IView::InsertPunchTable](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~InsertPunchTable.html) for more information about punch table templates.

## See Also

[IPunchTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable.html)
[IPunchTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0

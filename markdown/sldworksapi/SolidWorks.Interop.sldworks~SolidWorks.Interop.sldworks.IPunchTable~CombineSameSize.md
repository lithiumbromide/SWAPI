---
title: "CombineSameSize Property (IPunchTable)"
project: "SOLIDWORKS API Help"
interface: "IPunchTable"
member: "CombineSameSize"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable~CombineSameSize.html"
---

# CombineSameSize Property (IPunchTable)

Gets or sets whether to merge Punch ID column cells that have the same contents.

## Syntax

### Visual Basic (Declaration)

```vb
Property CombineSameSize As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPunchTable
Dim value As System.Boolean

instance.CombineSameSize = value

value = instance.CombineSameSize
```

### C#

```csharp
System.bool CombineSameSize {get; set;}
```

### C++/CLI

```cpp
property System.bool CombineSameSize {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to merge Punch ID column cells that have the same contents, false to not; only valid if [IPunchTable::CombineTags](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPunchTable~CombineTags.html) is false (see **Remarks**)

## VBA Syntax

See [PunchTable::CombineSameSize](ms-its:sldworksapivb6.chm::/sldworks~PunchTable~CombineSameSize.html).

## Examples

[Insert Punch Table (C#)](Insert_Punch_Table_Example_CSharp.htm)
[Insert Punch Table (VB.NET)](Insert_Punch_Table_Example_VBNET.htm)
[Insert Punch Table (VBA)](Insert_Punch_Table_Example_VB.htm)

## Remarks

Set this property to true to create a punch table with a PUNCH ID column that contains column cells that have been merged because they contain the same value within each tag group (e.g., A1, A2, A3).

If this property is set to false, the punch table looks like this:

| TAG | PUNCH ID | X LOCATION | Y LOCATION | ANGLE | QUANTITY |
| --- | --- | --- | --- | --- | --- |
| A1 | 135 | 107 | 300 | 90 | 1 |
| A2 | 135 | 200 | 150 | 90 | 1 |
| A3 | 135 | 300 | 200 | 90 | 1 |

If this property is set to true, the punch table looks like this:

| TAG | PUNCH ID | X LOCATION | Y LOCATION | ANGLE | QUANTITY |
| --- | --- | --- | --- | --- | --- |
| A1 | 135 | 107 | 300 | 90 | 1 |
| A2 | 200 | 150 | 90 | 1 |  |
| A3 | 300 | 200 | 90 | 1 |  |

## See Also

[IPunchTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable.html)
[IPunchTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0

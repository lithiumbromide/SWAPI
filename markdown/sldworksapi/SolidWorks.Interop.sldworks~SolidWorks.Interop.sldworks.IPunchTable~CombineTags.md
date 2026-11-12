---
title: "CombineTags Property (IPunchTable)"
project: "SOLIDWORKS API Help"
interface: "IPunchTable"
member: "CombineTags"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable~CombineTags.html"
---

# CombineTags Property (IPunchTable)

Gets or sets whether to combine tags for punches having the same Punch ID.

## Syntax

### Visual Basic (Declaration)

```vb
Property CombineTags As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPunchTable
Dim value As System.Boolean

instance.CombineTags = value

value = instance.CombineTags
```

### C#

```csharp
System.bool CombineTags {get; set;}
```

### C++/CLI

```cpp
property System.bool CombineTags {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to combine tags, false to not (see **Remarks**)

## VBA Syntax

See [PunchTable::CombineTags](ms-its:sldworksapivb6.chm::/sldworks~PunchTable~CombineTags.html).

## Examples

If this property is set to false, the punch table looks like this:

| TAG | PUNCH ID | X LOCATION | Y LOCATION | ANGLE | QUANTITY |
| --- | --- | --- | --- | --- | --- |
| A1 | 135 | 107 | 300 | 90 | 1 |
| A2 | 135 | 200 | 150 | 90 | 1 |
| A3 | 135 | 300 | 200 | 90 | 1 |

If this property is set to true, the punch table looks like this:

| TAG | PUNCH ID | QUANTITY |
| --- | --- | --- |
| A | 135 | 3 |

## Examples

[Insert Punch Table (VBA)](Insert_Punch_Table_Example_VB.htm)
[Insert Punch Table (VB.NET)](Insert_Punch_Table_Example_VBNET.htm)
[Insert Punch Table (C#)](Insert_Punch_Table_Example_CSharp.htm)

## See Also

[IPunchTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable.html)
[IPunchTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable_members.html)
[IPunch::TagStyle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable~TagStyle.html)
[IPunchTable::CombineSameSize Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable~CombineSameSize.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0

---
title: "TagStyle Property (IPunchTable)"
project: "SOLIDWORKS API Help"
interface: "IPunchTable"
member: "TagStyle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable~TagStyle.html"
---

# TagStyle Property (IPunchTable)

Gets or sets the tag style for this punch table.

## Syntax

### Visual Basic (Declaration)

```vb
Property TagStyle As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPunchTable
Dim value As System.Integer

instance.TagStyle = value

value = instance.TagStyle
```

### C#

```csharp
System.int TagStyle {get; set;}
```

### C++/CLI

```cpp
property System.int TagStyle {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Tag style as defined by [swPunchTableTagStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPunchTableTagStyle_e.html)

## VBA Syntax

See [PunchTable::TagStyle](ms-its:sldworksapivb6.chm::/sldworks~PunchTable~TagStyle.html).

## Examples

[Insert Punch Table (VBA)](Insert_Punch_Table_Example_VB.htm)
[Insert Punch Table (VB.NET)](Insert_Punch_Table_Example_VBNET.htm)
[Insert Punch Table (C#)](Insert_Punch_Table_Example_CSharp.htm)

## See Also

[IPunchTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable.html)
[IPunchTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable_members.html)
[IPunch::CombineTags Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable~CombineTags.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0

---
title: "TagStyle Property (IBendTable)"
project: "SOLIDWORKS API Help"
interface: "IBendTable"
member: "TagStyle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable~TagStyle.html"
---

# TagStyle Property (IBendTable)

Gets and sets the tag style for this bend table.

## Syntax

### Visual Basic (Declaration)

```vb
Property TagStyle As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBendTable
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

Tag style as defined in [swBendTableTagStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBendTableTagStyle_e.html)

## VBA Syntax

See [BendTable::TagStyle](ms-its:sldworksapivb6.chm::/sldworks~BendTable~TagStyle.html).

## Examples

[Insert Bend Table (VBA)](Insert_Bend_Table_Example_VB.htm)
[Insert Bend Table (VB.NET)](Insert_Bend_Table_Example_VBNET.htm)
[Insert Bend Table (C#)](Insert_Bend_Table_Example_CSharp.htm)

## See Also

[IBendTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable.html)
[IBendTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable_members.html)
[IBendTable::StartingValue Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable~StartingValue.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0

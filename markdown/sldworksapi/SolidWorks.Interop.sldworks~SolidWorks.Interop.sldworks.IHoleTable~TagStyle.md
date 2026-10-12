---
title: "TagStyle Property (IHoleTable)"
project: "SOLIDWORKS API Help"
interface: "IHoleTable"
member: "TagStyle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~TagStyle.html"
---

# TagStyle Property (IHoleTable)

Gets or sets the tag style for this hole table.

## Syntax

### Visual Basic (Declaration)

```vb
Property TagStyle As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleTable
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

Tag style as defined by [swHoleTableTagStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swHoleTableTagStyle_e.html)

## VBA Syntax

See [HoleTable::TagStyle](ms-its:sldworksapivb6.chm::/sldworks~HoleTable~TagStyle.html).

## See Also

[IHoleTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable.html)
[IHoleTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable_members.html)
[IHoleTable::CombineTags Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~CombineTags.html)
[IHoleTable::HoleTag Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~HoleTag.html)
[IHoleTable::HoleTagsVisible Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~HoleTagsVisible.html)
[IHoleTable::EnableUpdate Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~EnableUpdate.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0

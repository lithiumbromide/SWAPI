---
title: "HoleTag Property (IHoleTable)"
project: "SOLIDWORKS API Help"
interface: "IHoleTable"
member: "HoleTag"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~HoleTag.html"
---

# HoleTag Property (IHoleTable)

Gets or sets the name of the specified tag in a hole table.

## Syntax

### Visual Basic (Declaration)

```vb
Property HoleTag( _
   ByVal Row As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleTable
Dim Row As System.Integer
Dim value As System.String

instance.HoleTag(Row) = value

value = instance.HoleTag(Row)
```

### C#

```csharp
System.string HoleTag(
   System.int Row
) {get; set;}
```

### C++/CLI

```cpp
property System.String^ HoleTag {
   System.String^ get(System.int Row);
   void set (System.int Row, System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Row`: 0-based index of the row in which you want to change the name of the tag

### Property Value

Tag name

## VBA Syntax

See [HoleTable::HoleTag](ms-its:sldworksapivb6.chm::/sldworks~HoleTable~HoleTag.html).

## Examples

[Change Tags in Hole Table (VB.NET)](Change_Tags_in_Hole_Table_Example_VBNET.htm)
[Change Tags in Hole Table (VBA)](Change_Tags_in_Hole_Table_Example_VB.htm)
[Change Tags in Hole Table (C#)](Change_Tags_in_Hole_Table_Example_CSharp.htm)

## Remarks

[IHoleTable::CombineTags](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleTable~CombineTags.html) must be false for IHoleTable::HoleTag to work.

If you plan on changing many hole tags, then consider setting [IHoleTable::EnableUpdate](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleTable~EnableUpdate.html) to false to avoid a possible degradation in performance. After changing all of the hole tags, set IHoleTable::EnableUpdate to true to update the hole table and model view.

## See Also

[IHoleTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable.html)
[IHoleTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable_members.html)
[IHoleTable::HoleTagsVisible Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~HoleTagsVisible.html)
[IHoleTable::TagStyle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~TagStyle.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

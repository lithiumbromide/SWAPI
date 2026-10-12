---
title: "TableAnchor Property (ISheet)"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: "TableAnchor"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~TableAnchor.html"
---

# TableAnchor Property (ISheet)

Gets the specified table anchor.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property TableAnchor( _
   ByVal TableType As System.Integer _
) As TableAnchor
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
Dim TableType As System.Integer
Dim value As TableAnchor

value = instance.TableAnchor(TableType)
```

### C#

```csharp
TableAnchor TableAnchor(
   System.int TableType
) {get;}
```

### C++/CLI

```cpp
property TableAnchor^ TableAnchor {
   TableAnchor^ get(System.int TableType);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TableType`: Table type as defined in [swTableAnnotationType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTableAnnotationType_e.html)

### Property Value

[Table anchor](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITableAnchor.html)

## VBA Syntax

See [Sheet::TableAnchor](ms-its:sldworksapivb6.chm::/sldworks~Sheet~TableAnchor.html).

## Examples

[Get and Set Table Anchor of Hole Table (C#)](Get_and_Set_Table_Anchor_of_Hole_Table_Example_CSharp.htm)
[Get and Set Table Anchor of Hole Table (VB.NET)](Get_and_Set_Table_Anchor_of_Hole_Table_Example_VBNET.htm)
[Get and Set Table Anchor of Hole Table (VBA)](Get_and_Set_Table_Anchor_of_Hole_Table_Example_VB.htm)

## See Also

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)
[ISheet::SetAsTableAnchor Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetAsTableAnchor.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0

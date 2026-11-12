---
title: "SetColumnType2 Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "SetColumnType2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnType2.html"
---

# SetColumnType2 Method (ITableAnnotation)

Obsolete. Superseded by [ITableAnnotation::SetColumnType3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnType3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetColumnType2( _
   ByVal Index As System.Integer, _
   ByVal Type As System.Integer, _
   ByVal IncludeHidden As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim Index As System.Integer
Dim Type As System.Integer
Dim IncludeHidden As System.Boolean
Dim value As System.Boolean

value = instance.SetColumnType2(Index, Type, IncludeHidden)
```

### C#

```csharp
System.bool SetColumnType2(
   System.int Index,
   System.int Type,
   System.bool IncludeHidden
)
```

### C++/CLI

```cpp
System.bool SetColumnType2(
   System.int Index,
   System.int Type,
   System.bool IncludeHidden
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the column whose type to set
- `Type`: Column type as defined by [swTableColumnTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTableColumnTypes_e.html)
- `IncludeHidden`: True to set the hidden column type, false to not

### Return Value

True if column type is set, false if not

## VBA Syntax

See [TableAnnotation::SetColumnType2](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~SetColumnType2.html).

## Examples

[Insert Column in BOM Table (VBA)](Insert_Column_in_BOM_Table_Example_VB.htm)
[Insert Column in BOM Table (VB.NET)](Insert_Column_in_BOM_Table_Example_VBNET.htm)
[Insert Column in BOM Table (C#)](Insert_Column_in_BOM_Table_Example_CSharp.htm)

## Remarks

The index for both rows and columns is 0-based.

When you set a column type, the title is automatically changed to match that column type. If you change the column type to be a custom property column, then the column title is empty and you must set the column title using [ITableAnnotation::SetColumnTitle2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnTitle2.html).

A BOM table column cannot be changed to a Quantity type column in the SOLIDWORKS Design user interface. This method is consistent with the user interface.

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::GetColumnType2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnType2.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0

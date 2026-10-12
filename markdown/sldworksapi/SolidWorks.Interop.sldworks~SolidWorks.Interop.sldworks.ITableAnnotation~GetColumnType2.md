---
title: "GetColumnType2 Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "GetColumnType2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnType2.html"
---

# GetColumnType2 Method (ITableAnnotation)

Obsolete. Superseded by [ITableAnnotation::GetColumnType3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnType3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetColumnType2( _
   ByVal Index As System.Integer, _
   ByVal IncludeHidden As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim Index As System.Integer
Dim IncludeHidden As System.Boolean
Dim value As System.Integer

value = instance.GetColumnType2(Index, IncludeHidden)
```

### C#

```csharp
System.int GetColumnType2(
   System.int Index,
   System.bool IncludeHidden
)
```

### C++/CLI

```cpp
System.int GetColumnType2(
   System.int Index,
   System.bool IncludeHidden
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: 0-based index indicating the column whose type to get
- `IncludeHidden`: True to get the type of the hidden column, false to not

### Return Value

Type of column as defined by [swTableColumnTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTableColumnTypes_e.html)

## VBA Syntax

See [TableAnnotation::GetColumnType2](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~GetColumnType2.html).

## Examples

[Insert Column in BOM Table (VBA)](Insert_Column_in_BOM_Table_Example_VB.htm)
[Insert Column in BOM Table (VB.NET)](Insert_Column_in_BOM_Table_Example_VBNET.htm)
[Insert Column in BOM Table (C#)](Insert_Column_in_BOM_Table_Example_CSharp.htm)

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::SetColumnType2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnType2.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0

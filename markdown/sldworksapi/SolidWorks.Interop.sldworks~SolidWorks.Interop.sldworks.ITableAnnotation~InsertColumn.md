---
title: "InsertColumn Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "InsertColumn"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~InsertColumn.html"
---

# InsertColumn Method (ITableAnnotation)

Obsolete. Superseded by [ITableAnnnotation::InsertColumn2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITableAnnotation~InsertColumn2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertColumn( _
   ByVal Where As System.Integer, _
   ByVal Index As System.Integer, _
   ByVal Name As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim Where As System.Integer
Dim Index As System.Integer
Dim Name As System.String
Dim value As System.Boolean

value = instance.InsertColumn(Where, Index, Name)
```

### C#

```csharp
System.bool InsertColumn(
   System.int Where,
   System.int Index,
   System.string Name
)
```

### C++/CLI

```cpp
System.bool InsertColumn(
   System.int Where,
   System.int Index,
   System.String^ Name
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Where`: Where to insert the column as specified in [swTableItemInsertPosition_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTableItemInsertPosition_e.html)
- `Index`: Index of the column where to insert the new column
- `Name`: Column name

### Return Value

True if column is inserted successfully, false if not

## VBA Syntax

See [TableAnnotation::InsertColumn](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~InsertColumn.html).

## Examples

[Insert Part Number Column in BOM Table (C#)](Insert_Part_Number_Column_in_BOM_Table_Example_CSharp.htm)
[Insert Part Number Column in BOM Table (VB.NET)](Insert_Part_Number_Column_in_BOM_Table_Example_VBNET.htm)
[Insert Part Number Column in BOM Table (VBA)](Insert_Part_Number_Column_in_BOM_Table_Example_VB.htm)

## Remarks

The index for both rows and columns is 0-based.

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0

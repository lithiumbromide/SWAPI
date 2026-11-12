---
title: "SetColumnType3 Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "SetColumnType3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnType3.html"
---

# SetColumnType3 Method (ITableAnnotation)

Sets the type and property data for the specified BOM table column.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetColumnType3( _
   ByVal Index As System.Integer, _
   ByVal ColumnType As System.Integer, _
   ByVal IncludeHidden As System.Boolean, _
   ByVal PropertyData As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim Index As System.Integer
Dim ColumnType As System.Integer
Dim IncludeHidden As System.Boolean
Dim PropertyData As System.Object
Dim value As System.Integer

value = instance.SetColumnType3(Index, ColumnType, IncludeHidden, PropertyData)
```

### C#

```csharp
System.int SetColumnType3(
   System.int Index,
   System.int ColumnType,
   System.bool IncludeHidden,
   System.object PropertyData
)
```

### C++/CLI

```cpp
System.int SetColumnType3(
   System.int Index,
   System.int ColumnType,
   System.bool IncludeHidden,
   System.Object^ PropertyData
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: 0-based index of the column whose type to set
- `ColumnType`: Type of column as defined in [swTableColumnTypes_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTableColumnTypes_e.html) (see **Remarks**)
- `IncludeHidden`: True to include hidden columns in Index, false to not
- `PropertyData`: Property data specific to ColumnType (see **Remarks**)

### Return Value

Return code as defined in [swColumnTypeStatus_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swColumnTypeStatus_e.html)

## VBA Syntax

See [TableAnnotation::SetColumnType3](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~SetColumnType3.html).

## Examples

[Get and Set BOM Column Types and Cell Equations (VBA)](Get_and_Set_Column_Types_and_Cell_Equations_Example_VB.htm)

## Remarks

PropertyData specifies the column title and contents.

| If ColumnType is set to swTableColumnTypes_e.... | Then Set PropertyData with... |
| --- | --- |
| swBomTableColumnType_CustomProperty | Valid property name* |
| swBomTableColumnType_UnitOfMeasure | Valid property name* |
| swBomTableColumnType_Equation | Equation string |
| swBomTableColumnType_ComponentReference | Null or Nothing |
| swBomTableColumnType_ToolboxProperty | Property as defined in swToolBoxPropertyName_e |
| swBomTableColumnType_CutListProperties (valid only for sheetmetal parts) | Valid cutlist property name* |
| swBomTableColumnType_ItemNumber | Array of four values { Start_Item_Int , Increment_Int , Order_balloons_and_BOM_to_follow_assembly_order_Bool , Do_not_change_BOM_item_number_Bool } |
| swBomTableColumnType_PartNumber | True to use title summary, false to not |

* Note: To get the valid property names for a given column type, open a part in SOLIDWORKS and add a BOM table to it. Right-click a column and select **Insert > Column Right**. In the popup, select the column type of interest in the first dropdown. Inspect the contents of the second dropdown to see the valid property names for the column type.

When you set a column type, the title is automatically changed to match that column type. If you change the column type to custom property, you must set the column title using [ITableAnnotation::SetColumnTitle2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnTitle2.html).

This method is consistent with the SOLIDWORKS Design user interface where you cannot add, delete, or replace the Quantity type column in a BOM table.

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::GetColumnType3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnType3.html)
[ITableAnnotation::SetCellEquation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetCellEquation.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0

---
title: "GetColumnType3 Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "GetColumnType3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnType3.html"
---

# GetColumnType3 Method (ITableAnnotation)

Gets the type and property data for the specified BOM table column.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetColumnType3( _
   ByVal Index As System.Integer, _
   ByVal IncludeHidden As System.Boolean, _
   ByRef PropertyData As System.Object, _
   ByRef Status As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim Index As System.Integer
Dim IncludeHidden As System.Boolean
Dim PropertyData As System.Object
Dim Status As System.Integer
Dim value As System.Integer

value = instance.GetColumnType3(Index, IncludeHidden, PropertyData, Status)
```

### C#

```csharp
System.int GetColumnType3(
   System.int Index,
   System.bool IncludeHidden,
   out System.object PropertyData,
   out System.int Status
)
```

### C++/CLI

```cpp
System.int GetColumnType3(
   System.int Index,
   System.bool IncludeHidden,
   [Out] System.Object^ PropertyData,
   [Out] System.int Status
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: 0-based index of the column whose type to get
- `IncludeHidden`: True to include hidden columns in Index, false to not
- `PropertyData`: Property data specific to the type of column (see **Remarks**)
- `Status`: Return code as defined in [swColumnTypeStatus_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swColumnTypeStatus_e.html)

### Return Value

Type of column as defined in [swTableColumnTypes_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTableColumnTypes_e.html)

## VBA Syntax

See [TableAnnotation::GetColumnType3](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~GetColumnType3.html).

## Examples

[Get and Set BOM Column Types and Cell Equations (VBA)](Get_and_Set_Column_Types_and_Cell_Equations_Example_VB.htm)

## Remarks

PropertyData varies by the type of column. See the Remarks in [ITableAnnotation::SetColumnType3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnType3.html).

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::GetCellEquation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellEquation.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0

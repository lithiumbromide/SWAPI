---
title: "InsertFamilyTable Method (ISheet)"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: "InsertFamilyTable"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~InsertFamilyTable.html"
---

# InsertFamilyTable Method (ISheet)

Inserts a family table in this drawing sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertFamilyTable( _
   ByVal AttachToAnchorPoint As System.Boolean, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal ModelName As System.String, _
   ByVal TableTemplateName As System.String, _
   ByVal DimColumnType As System.Integer, _
   ByVal UseAllConfigs As System.Boolean, _
   ByVal ConfigArray As System.Object, _
   ByVal ItemNumberStart As System.Integer, _
   ByVal ItemNumberIncrement As System.Integer, _
   ByVal FollowConfigTreeOrder As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
Dim AttachToAnchorPoint As System.Boolean
Dim X As System.Double
Dim Y As System.Double
Dim ModelName As System.String
Dim TableTemplateName As System.String
Dim DimColumnType As System.Integer
Dim UseAllConfigs As System.Boolean
Dim ConfigArray As System.Object
Dim ItemNumberStart As System.Integer
Dim ItemNumberIncrement As System.Integer
Dim FollowConfigTreeOrder As System.Boolean
Dim value As System.Object

value = instance.InsertFamilyTable(AttachToAnchorPoint, X, Y, ModelName, TableTemplateName, DimColumnType, UseAllConfigs, ConfigArray, ItemNumberStart, ItemNumberIncrement, FollowConfigTreeOrder)
```

### C#

```csharp
System.object InsertFamilyTable(
   System.bool AttachToAnchorPoint,
   System.double X,
   System.double Y,
   System.string ModelName,
   System.string TableTemplateName,
   System.int DimColumnType,
   System.bool UseAllConfigs,
   System.object ConfigArray,
   System.int ItemNumberStart,
   System.int ItemNumberIncrement,
   System.bool FollowConfigTreeOrder
)
```

### C++/CLI

```cpp
System.Object^ InsertFamilyTable(
   System.bool AttachToAnchorPoint,
   System.double X,
   System.double Y,
   System.String^ ModelName,
   System.String^ TableTemplateName,
   System.int DimColumnType,
   System.bool UseAllConfigs,
   System.Object^ ConfigArray,
   System.int ItemNumberStart,
   System.int ItemNumberIncrement,
   System.bool FollowConfigTreeOrder
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AttachToAnchorPoint`: True to insert the family table at the existing family table anchor point, false to anchor the table at the point specified by X and Y
- `X`: X coordinate for the placement of the family table annotation
- `Y`: Y coordinate for the placement of the family table annotation
- `ModelName`: Name of part or assembly on whose drawing sheet to insert the family table
- `TableTemplateName`: Path and filename of the template that corresponds to this type of table (see **Remarks**)
- `DimColumnType`: Dimension column type as defined by [swFamilyTableDimColumnType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFamilyTableDimColumnType_e.html)
- `UseAllConfigs`: True to use all configurations, false to only use ConfigArray configurations
- `ConfigArray`: Array of configurations to use; valid only if UseAllConfigs is false
- `ItemNumberStart`: Starting item number
- `ItemNumberIncrement`: Item number increment
- `FollowConfigTreeOrder`: True to follow the configuration tree order, false to not

### Return Value

[IFamilyTableAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableAnnotation.html)

## VBA Syntax

See [Sheet::InsertFamilyTable](ms-its:sldworksapivb6.chm::/sldworks~Sheet~InsertFamilyTable.html).

## Remarks

Family tables display the variations in part and assembly configurations or custom properties in table format.

By default, the family table templates are in install_dir\lang\language and have a filename extension of .sldfamtbt. The template and table must be of the same type. For example, you must specify TableTemplate with `install_dir`\lang\English\family-standard.sldfamtbt if you want to insert the English version of a family table.

For more information about family tables, see the **SOLIDWORKS Design user-interface Help > Detailing and Drawings > Tables > Family Tables** topics.

## See Also

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34

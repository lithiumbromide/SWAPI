---
title: "ITableAnnotation Interface"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html"
---

# ITableAnnotation Interface

Provides access to table annotations.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ITableAnnotation
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
```

### C#

```csharp
public interface ITableAnnotation
```

### C++/CLI

```cpp
public interface class ITableAnnotation
```

## VBA Syntax

See [TableAnnotation](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation.html).

## Examples

[Hide or Show First Column in Hole Table (VB.NET)](Hide_or_Show_First_Column_in_Hole_Table_Example_VBNET.htm)
[Hide or Show First Column in Hole Table (VBA)](Hide_or_Show_First_Column_in_Hole_Table_Example_VB.htm)
[Hide or Show First Column in Hole Table (C#)](Hide_or_Show_First_Column_in_Hole_Table_Example_CSharp.htm)
[Select Table Cells (C#)](Select_Table_Cells_Example_CSharp.htm)
[Select Table Cells (VB.NET)](Select_Table_Cells_Example_VBNET.htm)
[Select Table Cells (VBA)](Select_Table_Cells_Example_VB.htm)
[Get General Table Feature (C#)](Get_General_Table_Feature_Example_CSharp.htm)
[Get General Table Feature (VB.NET)](Get_General_Table_Feature_Example_VBNET.htm)
[Get General Table Feature (VBA)](Get_General_Table_Feature_Example_VB.htm)
[Get Components in Each BOM Table Row (C#)](Get_Components_in_Each_BOM_Table_Row_Example_CSharp.htm)
[Get Components in Each BOM Table Row (VB.NET)](Get_Components_in_Each_BOM_Table_Row_Example_VBNET.htm)
[Get Components in Each BOM Table Row (VBA)](Get_Components_in_Each_BOM_Table_Row_VB.htm)

## Remarks

See [swTableAnnotationType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTableAnnotationType_e.html) for the types of tables derived from ITableAnnotation.

## Accessors

[IDrawingDoc::InsertTableAnnotation2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~InsertTableAnnotation2.html)

[IGeneralTableFeature::GetTableAnnotations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGeneralTableFeature~GetTableAnnotations.html) and [IGeneralTableFeature::IGetTableAnnotations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGeneralTableFeature~IGetTableAnnotations.html)

[IModelDocExtension::GetGeneralTableAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetGeneralTableAnnotation.html)

[IModelDocExtension::InsertGeneralTableAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~InsertGeneralTableAnnotation.html)

[IModelDocExtension::InsertTitleBlockTable](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~InsertTitleBlockTable.html)

[ITableAnnotation::GetNext](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITableAnnotation~GetNext.html)

[ITableAnnotation::HorizontalAutoSplit](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITableAnnotation~HorizontalAutoSplit.html)

[ITableAnnotation::Split](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITableAnnotation~Split.html)

[IView::GetFirstTableAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFirstTableAnnotation.html)

[IView::GetTableAnnotations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetTableAnnotations.html) and [IView::IGetTableAnnotations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetTableAnnotations.html)

## Access Diagram

[TableAnnotation](SWObjectModel.pdf#TableAnnotation)

## See Also

[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)

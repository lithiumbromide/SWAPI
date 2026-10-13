---
title: "ITableAnchor Interface"
project: "SOLIDWORKS API Help"
interface: "ITableAnchor"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnchor.html"
---

# ITableAnchor Interface

Allows access to the data that defines a table anchor feature.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ITableAnchor
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnchor
```

### C#

```csharp
public interface ITableAnchor
```

### C++/CLI

```cpp
public interface class ITableAnchor
```

## VBA Syntax

See [TableAnchor](ms-its:sldworksapivb6.chm::/sldworks~TableAnchor.html).

## Examples

[Get Table Anchor (VBA)](Get_Table_Anchor_Example_VB.htm)
[Get and Set Table Anchor of Hole Table (VBA)](Get_and_Set_Table_Anchor_of_Hole_Table_Example_VB.htm)
[Get and Set Table Anchor of Hole Table (VB.NET)](Get_and_Set_Table_Anchor_of_Hole_Table_Example_VBNET.htm)
[Get and Set Table Anchor of Hole Table (C#)](Get_and_Set_Table_Anchor_of_Hole_Table_Example_CSharp.htm)

## Remarks

If a table anchor is selected, then it can be retrieved with [ISelectionMgr::GetSelectedObject6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectedObject6.html). If the selected object type is swSelBOMTEMPS, then getting the selected object is a [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object. Use [IFeature::GetSpecifiedFeature2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetSpecificFeature2.html) to return a TableAnchor object.

If you traverse the features and subfeatures of a drawing, then the table anchors display as subfeatures of the sheet format. When [IFeature::GetTypeName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetTypeName.html) returns GeneralTableAnchor, HoleTableAnchor, WeldmentCutListAnchor, RevisionTableAnchor, or BomTemplate, use IFeature::GetSpecificFeature2 to return a ITableAnchor object.

NOTE: Weld table anchors are not currently supported.

You can also retrieve a ITableAnchor object from the [ISheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheet.html) object using [ISheet::TableAnchor](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheet~TableAnchor.html). There is only one anchor of each type on a sheet format.

## Accessors

[IFeature::GetDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetDefinition.html) and [IFeature::IGetDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetDefinition.html)

[ISheet::SetAsTableAnchor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetAsTableAnchor.html)

[ISheet::TableAnchor](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheet~TableAnchor.html)

## Access Diagram

[TableAnchor](SWObjectModel.pdf#TableAnchor)

## See Also

[ITableAnchor Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnchor_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)

---
title: "SelectAll Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "SelectAll"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectAll.html"
---

# SelectAll Method (IModelDocExtension)

Selects all edges in a part, all components in an assembly, or all entities (by default, sketch entities, dimensions, and annotations) in a drawing.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SelectAll()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension

instance.SelectAll()
```

### C#

```csharp
void SelectAll()
```

### C++/CLI

```cpp
void SelectAll();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDocExtension::SelectAll](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~SelectAll.html).

## Examples

[Select All in Part, Assembly, or Drawing (C#)](Select_All_in_Part_Assembly_or_Drawing_Example_CSharp.htm)
[Select All in Part, Assembly, or Drawing (VB.NET)](Select_All_in_Part_Assembly_or_Drawing_Example_vbnet.htm)
[Select All in Part, Assembly, or Drawing (VBA)](Select_All_in_Part_Assembly_or_Drawing_Example_vb.htm)

## Remarks

This method behaves the same as box selecting everything in the graphics area of a part or assembly document or in a sheet of a drawing document.

To select entities different from the defaults, use selection filters. The **See Also** section contains links to methods related to selection filters.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::MultiSelect Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~MultiSelect.html)
[IModelDocExtension::IMultiSelect Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IMultiSelect.html)
[IModelDocExtension::SelectByID2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html)
[IComponent2::Select4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Select4.html)
[IBody2::GetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetEdges.html)
[IBody2::IGetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetEdges.html)
[IView::ISelectEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ISelectEntity.html)
[IView::SelectEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SelectEntity.html)
[ISldWorks::GetSelectionFilter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetSelectionFilter.html)
[ISldWorks::GetSelectionFilters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetSelectionFilters.html)
[ISldWorks::IGetSelectionFilters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetSelectionFilters.html)
[ISldWorks::IGetSelectionFiltersCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetSelectionFiltersCount.html)
[ISldWorks::ISetSelectionFilters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ISetSelectionFilters.html)
[ISldWorks::SetSelectionFilter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetSelectionFilter.html)
[ISldWorks::SetSelectionFilters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetSelectionFilters.html)
[ISldWorks::GetApplySelectionFilter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetApplySelectionFilter.html)
[ISldWorks::SetApplySelectionFilter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetApplySelectionFilter.html)
[ISelectData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.html)
[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html)
[IAssemblyDoc::SelectComponentsBySize Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SelectComponentsBySize.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0

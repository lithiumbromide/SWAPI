---
title: "GetVisibleEntityCount2 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetVisibleEntityCount2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleEntityCount2.html"
---

# GetVisibleEntityCount2 Method (IView)

Gets the number of visible entities of the specified type for the specified component in this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetVisibleEntityCount2( _
   ByVal LpViewComponent As Component2, _
   ByVal EntityType As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim LpViewComponent As Component2
Dim EntityType As System.Integer
Dim value As System.Integer

value = instance.GetVisibleEntityCount2(LpViewComponent, EntityType)
```

### C#

```csharp
System.int GetVisibleEntityCount2(
   Component2 LpViewComponent,
   System.int EntityType
)
```

### C++/CLI

```cpp
System.int GetVisibleEntityCount2(
   Component2^ LpViewComponent,
   System.int EntityType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `LpViewComponent`: [Component](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) from which to get the visible EntityType
- `EntityType`: Type of entity as defined in [swViewEntityType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewEntityType_e.html)

### Return Value

Number of visible entities of EntityType in LpViewComponent

## VBA Syntax

See [View::GetVisibleEntityCount2](ms-its:sldworksapivb6.chm::/sldworks~View~GetVisibleEntityCount2.html).

## Examples

[Hide and Show All Edges in Drawing View (C#)](Hide_and_Show_All_Ediges_in_Drawing_View_Example_CSharp.htm)
[Hide and Show All Edges in Drawing View (VB.NET)](Hide_and_Show_All_Ediges_in_Drawing_View_Example_VBNET.htm)
[Hide and Show All Edges in Drawing View (VBA)](Hide_and_Show_All_Edges_in_Drawing_View_Example_VB.htm)

## Remarks

Visible entities are entities that are not completely obscured by other entities in the view.

Call this method to get the size of the array returned by [IView::IGetVisibleEntities2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetVisibleEntities2.html).

The difference between this method and the now obsolete IView::GetVisibleEntityCount method is that this method gets the correct number of silhouette edges (EntityType = swViewEntityType_e.swViewEntityType_SilhouetteEdge).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetVisibleEntities2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleEntities2.html)
[IView::GetVisibleComponentCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleComponentCount.html)
[IView::GetVisibleComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleComponents.html)
[IView::IGetVisibleComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetVisibleComponents.html)
[IView::GetHiddenComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetHiddenComponents.html)
[IView::EnumHiddenComponents2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~EnumHiddenComponents2.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0

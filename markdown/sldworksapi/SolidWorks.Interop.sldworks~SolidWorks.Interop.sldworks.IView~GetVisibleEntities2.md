---
title: "GetVisibleEntities2 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetVisibleEntities2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleEntities2.html"
---

# GetVisibleEntities2 Method (IView)

Gets the visible entities of the specified type for the specified component in this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetVisibleEntities2( _
   ByVal LpViewComponent As Component2, _
   ByVal EntityType As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim LpViewComponent As Component2
Dim EntityType As System.Integer
Dim value As System.Object

value = instance.GetVisibleEntities2(LpViewComponent, EntityType)
```

### C#

```csharp
System.object GetVisibleEntities2(
   Component2 LpViewComponent,
   System.int EntityType
)
```

### C++/CLI

```cpp
System.Object^ GetVisibleEntities2(
   Component2^ LpViewComponent,
   System.int EntityType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `LpViewComponent`: [Component](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) from which to get EntityType
- `EntityType`: Type of entity as defined in [swViewEntityType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewEntityType_e.html)

### Return Value

Array of the visible entities of EntityType in LpViewComponent

## VBA Syntax

See [View::GetVisibleEntities2](ms-its:sldworksapivb6.chm::/sldworks~View~GetVisibleEntities2.html).

## Examples

[Get Visible Components and Entities in Drawing View (VBA)](Get_Visible_Components_and_Entities_in_Drawing_View_Example_VB.htm)
[Get Visible Components and Entities in Drawing View (VB.NET)](Get_Visible_Components_and_Entites_in_a_Drawing_View_Example_VBNET.htm)
[Get Visible Components and Entities in Drawing View (C#)](Get_Visible_Components_and_Entites_in_a_Drawing_View_Example_CSharp.htm)

## Remarks

Visible entities are entities that are not completely obscured by other entities in the view.

The difference between this method and the now obsolete IView::GetVisibleEntities method is that this method supports silhouette edges (EntityType = swViewEntityType_e.swViewEntityType_SilhouetteEdge).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::IGetVisibleEntities2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetVisibleEntities2.html)
[IView::GetVisibleEntityCount2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleEntityCount2.html)
[IView::GetVisibleComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleComponents.html)
[IView::GetVisibleComponentCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleComponentCount.html)
[IView::IGetVisibleComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetVisibleComponents.html)
[IView::GetHiddenComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetHiddenComponents.html)
[IView::EnumHiddenComponents2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~EnumHiddenComponents2.html)
[IView::GetVisibleDrawingComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleDrawingComponents.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0

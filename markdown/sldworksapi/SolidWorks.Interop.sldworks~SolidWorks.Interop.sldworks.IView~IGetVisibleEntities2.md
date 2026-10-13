---
title: "IGetVisibleEntities2 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetVisibleEntities2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetVisibleEntities2.html"
---

# IGetVisibleEntities2 Method (IView)

Gets the visible entities of the specified type for the specified component in this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetVisibleEntities2( _
   ByVal LpViewComponent As Component2, _
   ByVal EntityType As System.Integer, _
   ByVal ViewEntityCount As System.Integer _
) As Entity
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim LpViewComponent As Component2
Dim EntityType As System.Integer
Dim ViewEntityCount As System.Integer
Dim value As Entity

value = instance.IGetVisibleEntities2(LpViewComponent, EntityType, ViewEntityCount)
```

### C#

```csharp
Entity IGetVisibleEntities2(
   Component2 LpViewComponent,
   System.int EntityType,
   System.int ViewEntityCount
)
```

### C++/CLI

```cpp
Entity^ IGetVisibleEntities2(
   Component2^ LpViewComponent,
   System.int EntityType,
   System.int ViewEntityCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `LpViewComponent`: [Component](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) from which to get EntityType
- `EntityType`: Type of entity as defined in [swViewEntityType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewEntityType_e.html)
- `ViewEntityCount`: Number of visible entities of EntityType in LpViewComponent

### Return Value

- In-process, unmanaged C++: Pointer to an array of visible entities

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Visible entities are entities that are not completely obscured by other entities in the view.

Call [IView::GetVisibleEntityCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetVisibleEntityCount2.html) before calling this method to get the value of ViewEntityCount.

The difference between this method and the now obsolete IView::IGetVisibleEntities method is that this method supports silhouette edges (EntityType = swViewEntityType_e.swViewEntityType_SilhouetteEdge).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetVisibleEntities2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleEntities2.html)
[IView::GetVisibleComponentCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleComponentCount.html)
[IView::GetVisibleComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleComponents.html)
[IView::GetHiddenComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetHiddenComponents.html)
[IView::EnumHiddenComponents2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~EnumHiddenComponents2.html)
[IView::IGetVisibleComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetVisibleComponents.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0

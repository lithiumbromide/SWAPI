---
title: "IGetVisibleEntities Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetVisibleEntities"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetVisibleEntities.html"
---

# IGetVisibleEntities Method (IView)

Obsolete. Superseded by [IView::IGetVisibleEntities2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetVisibleEntities2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetVisibleEntities( _
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

value = instance.IGetVisibleEntities(LpViewComponent, EntityType, ViewEntityCount)
```

### C#

```csharp
Entity IGetVisibleEntities(
   Component2 LpViewComponent,
   System.int EntityType,
   System.int ViewEntityCount
)
```

### C++/CLI

```cpp
Entity^ IGetVisibleEntities(
   Component2^ LpViewComponent,
   System.int EntityType,
   System.int ViewEntityCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `LpViewComponent`: [Component](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) from which to get EntityType
- `EntityType`: Type of entity as defined in [swViewEntityType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewEntityType_e.html)
- `ViewEntityCount`: Number of specified visible entities

### Return Value

Array of the specified visible entities

## Remarks

Visible entities are only those entities not completely obscured by other entities in the view.

Call [IView::GetVisibleEntityCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetVisibleEntityCount.html) before calling this method to get the value of ViewEntityCount.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetVisibleEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleEntities.html)
[IView::GetVisibleComponentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleComponentCount.html)
[IView::GetVisibleComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleComponents.html)
[IView::EnumHiddenComponents2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~EnumHiddenComponents2.html)
[IView::GetHiddenComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetHiddenComponents.html)
[IView::IGetVisibleComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetVisibleComponents.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0

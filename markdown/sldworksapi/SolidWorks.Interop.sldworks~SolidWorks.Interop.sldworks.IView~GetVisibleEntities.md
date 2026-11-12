---
title: "GetVisibleEntities Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetVisibleEntities"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleEntities.html"
---

# GetVisibleEntities Method (IView)

Obsolete. Superseded by [IView::GetVisibleEntities2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetVisibleEntities2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetVisibleEntities( _
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

value = instance.GetVisibleEntities(LpViewComponent, EntityType)
```

### C#

```csharp
System.object GetVisibleEntities(
   Component2 LpViewComponent,
   System.int EntityType
)
```

### C++/CLI

```cpp
System.Object^ GetVisibleEntities(
   Component2^ LpViewComponent,
   System.int EntityType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `LpViewComponent`: [Component](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) from which to get EntityType
- `EntityType`: Type of entity as defined in [swViewEntityType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewEntityType_e.html)

### Return Value

Array of the specified visible entities

## VBA Syntax

See [View::GetVisibleEntities](ms-its:sldworksapivb6.chm::/sldworks~View~GetVisibleEntities.html).

## Remarks

Visible entities are only those entities not completely obscured by other entities in the view.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetVisibleEntityCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleEntityCount.html)
[IView::IGetVisibleEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetVisibleEntities.html)
[IView::IGetVisibleComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetVisibleComponents.html)
[IView::GetVisibleComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleComponents.html)
[IView::GetVisibleComponentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleComponentCount.html)
[IView::GetHiddenComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetHiddenComponents.html)
[IView::EnumHiddenComponents2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~EnumHiddenComponents2.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0

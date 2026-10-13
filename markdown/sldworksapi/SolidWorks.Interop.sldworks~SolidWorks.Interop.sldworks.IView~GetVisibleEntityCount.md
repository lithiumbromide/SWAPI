---
title: "GetVisibleEntityCount Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetVisibleEntityCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleEntityCount.html"
---

# GetVisibleEntityCount Method (IView)

Obsolete. Superseded by [IView::GetVisibleEntityCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetVisibleEntityCount2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetVisibleEntityCount( _
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

value = instance.GetVisibleEntityCount(LpViewComponent, EntityType)
```

### C#

```csharp
System.int GetVisibleEntityCount(
   Component2 LpViewComponent,
   System.int EntityType
)
```

### C++/CLI

```cpp
System.int GetVisibleEntityCount(
   Component2^ LpViewComponent,
   System.int EntityType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `LpViewComponent`: [Component](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) from which to get the visible EntityType
- `EntityType`: Type of entity as defined in [swViewEntityType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewEntityType_e.html)

### Return Value

Number of specified entities in LpViewComponent

## VBA Syntax

See [View::GetVisibleEntityCount](ms-its:sldworksapivb6.chm::/sldworks~View~GetVisibleEntityCount.html).

## Remarks

Visible entities are only those entities not completely obscured by other entities in the view.

Call this method before calling [IView::IGetVisibleEntities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetVisibleEntities.html) to get the size of the array for that method.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetVisibleEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleEntities.html)
[IView::GetVisibleComponentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleComponentCount.html)
[IView::GetVisibleComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleComponents.html)
[IView::IGetVisibleComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetVisibleComponents.html)
[IView::GetHiddenComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetHiddenComponents.html)
[IView::EnumHiddenComponents2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~EnumHiddenComponents2.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0

---
title: "GetSelectedObjectsComponent3 Method (ISelectionMgr)"
project: "SOLIDWORKS API Help"
interface: "ISelectionMgr"
member: "GetSelectedObjectsComponent3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsComponent3.html"
---

# GetSelectedObjectsComponent3 Method (ISelectionMgr)

Obsolete. Superseded by [ISelectionMgr::GetSelectedObjectsComponent4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectedObjectsComponent4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSelectedObjectsComponent3( _
   ByVal Index As System.Integer, _
   ByVal Mark As System.Integer _
) As Component2
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectionMgr
Dim Index As System.Integer
Dim Mark As System.Integer
Dim value As Component2

value = instance.GetSelectedObjectsComponent3(Index, Mark)
```

### C#

```csharp
Component2 GetSelectedObjectsComponent3(
   System.int Index,
   System.int Mark
)
```

### C++/CLI

```cpp
Component2^ GetSelectedObjectsComponent3(
   System.int Index,
   System.int Mark
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index position within the current list of selected items, where the index ranges from 1 to [ISelectionMgr::GetSelectedObjectCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectedObjectCount2.html) (see **Remarks**)
- `Mark`: - -1 = All selections regardless of marks

  0 = Only the selections without marks

  Any other value = Value that was used to mark and select an object

### Return Value

[Component](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)

## VBA Syntax

See [SelectionMgr::GetSelectedObjectsComponent3](ms-its:sldworksapivb6.chm::/sldworks~SelectionMgr~GetSelectedObjectsComponent3.html).

## Examples

[Access Selections (VBA)](Access_Selections_Example_VB.htm)
[Add Comment to Assembly Component (VBA)](Add_Comment_to_Assembly_Component_Example_VB.htm)
[Align Assembly Component to Assembly Origin and Planes (VBA)](Align_Assembly_Component_to_Assembly_Origin_and_Planes_Example_VB.htm)
[Display Temporary Body (C#)](Display_Temporary_Body_Example_CSharp.htm)
[Display Temporary Body (VB.NET)](Display_Temporary_Body_Example_VBNET.htm)
[Display Temporary Body (VBA)](Display_Temporary_Body_Example_VB.htm)

## Remarks

The index starts at 1, even when using C++. However, if you specify -1 for the Index argument, then the Mark argument is ignored and the dynamically highlighted component is selected if dynamic highlighting is turned on. See also IAssemblyDoc event [DynamicHighlightNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DAssemblyDocEvents_DynamicHighlightNotifyEventHandler.html).

The difference between this obsolete method and [ISelectionMgr::GetSelectedObjectsComponent4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectedObjectsComponent4.html) is that ISelectionMgr::GetSelectedObjectsComponent4 can return an [IDrawingComponent](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingComponent.html) and ISelectionMgr::GetSelectedObjectsComponent3 cannot.

## See Also

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html)
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.html)
[ISelectionMgr::DeSelect2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~DeSelect2.html)
[ISelectionMgr::GetSelectedObject6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.html)
[ISelectionMgr::GetSelectedObjectLoop2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectLoop2.html)
[ISelectionMgr::GetSelectedObjectMark Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectMark.html)
[ISelectionMgr::GetSelectedObjectsDrawingView2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsDrawingView2.html)
[ISelectionMgr::GetSelectedObjectType3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectType3.html)
[ISelectionMgr::GetSelectionPoint2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionPoint2.html)
[ISelectionMgr::GetSelectionPointInSketchSpace2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionPointInSketchSpace2.html)
[ISelectionMgr::IDeSelect2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IDeSelect2.html)
[ISelectionMgr::ISelectionMgr::IGetSelectionPointInSketchSpace2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IGetSelectionPointInSketchSpace2.html)
[IComponent2::Select3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Select3.html)
[ISelectionMgr::IGetSelectionPoint2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IGetSelectionPoint2.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0

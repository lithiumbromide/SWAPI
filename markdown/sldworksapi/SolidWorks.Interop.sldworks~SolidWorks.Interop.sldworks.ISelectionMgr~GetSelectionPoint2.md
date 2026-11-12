---
title: "GetSelectionPoint2 Method (ISelectionMgr)"
project: "SOLIDWORKS API Help"
interface: "ISelectionMgr"
member: "GetSelectionPoint2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionPoint2.html"
---

# GetSelectionPoint2 Method (ISelectionMgr)

Gets the selected point in model space coordinates from the currently selected object.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSelectionPoint2( _
   ByVal Index As System.Integer, _
   ByVal Mark As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectionMgr
Dim Index As System.Integer
Dim Mark As System.Integer
Dim value As System.Object

value = instance.GetSelectionPoint2(Index, Mark)
```

### C#

```csharp
System.object GetSelectionPoint2(
   System.int Index,
   System.int Mark
)
```

### C++/CLI

```cpp
System.Object^ GetSelectionPoint2(
   System.int Index,
   System.int Mark
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index position with in the current list of selected items, where AtIndex ranges from 1 to [ISelectionMgr::GetSelectedObjectCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectedObjectCount2.html) (see **Remarks**)
- `Mark`: - -1 = All selections regardless of marks

  0 = only the selections without marks

  Any other value = Value that was used to mark and select an object

### Return Value

Array of 3 doubles (x,y,z)

## VBA Syntax

See [SelectionMgr::GetSelectionPoint2](ms-its:sldworksapivb6.chm::/sldworks~SelectionMgr~GetSelectionPoint2.html).

## Examples

[Create Multi-row Callouts (VBA)](Create_Multi-row_Callouts_Example_VB.htm)
[Create Drag Arrow Manipulator (C#)](Create_Drag_Arrow_Manipulator_Example_CSharp.htm)
[Create Drag Arrow Manipulator (VB.NET)](Create_Drag_Arrow_Manipulator_Example_VBNET.htm)
[Create Drag Arrow Manipulator (VBA)](Create_Drag_Arrow_Manipulator_Example_VB.htm)

## Remarks

The index starts at 1, even when using C++. However, if you specify -1 for the Index argument, then the Mark argument is ignored and the dynamically highlighted view is selected if dynamic highlighting is turned on. See also IAssemblyDoc event [DynamicHighlightNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DAssemblyDocEvents_DynamicHighlightNotifyEventHandler.html), IDrawingDoc event [DynamicHighlightNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_DynamicHighlightNotifyEventHandler.html), and IPartDoc event [DynamicHighlightNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_DynamicHighlightNotifyEventHandler.html).

The point returned from ISelectionMgr::GetSelectionPoint2 or [ISelectionMgr::IGetSelectionPoint2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectionPoint2.html) cannot lie on the object that was selected. For example, the user can select an edge when the edge is within the pick radius of their mouse cursor. However, to get a point on a face, edge, or vertex, use that object's GetClosestPointOn method.

To do this, get the [IFace2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html), [IEdge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html), or [IVertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html) object using the [ISelectionMgr::GetSelectedObject6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectedObject6.html) method, and then use that object to call GetClosestPointOn. Pass the X,Y,Z values returned from ISelectionMgr::GetSelectionPoint2 or ISelectionMgr::IGetSelectionPoint2, and the GetClosestPointOn method will return the closest X,Y,Z point that is on the face, edge, or vertex.

If the selected object is sketch geometry, then the coordinates returned are in sketch space. The coordinates are 2D and related to the origin of the sketch that owns the selected geometry.

## See Also

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html)
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.html)
[ISelectionMgr::GetSelectionPointInSketchSpace2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionPointInSketchSpace2.html)
[ISelectionMgr::GetSelectedObjectLoop2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectLoop2.html)
[ISelectionMgr::GetSelectedObjectMark Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectMark.html)
[ISelectionMgr::GetSelectedObjectsComponent3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsComponent3.html)
[ISelectionMgr::GetSelectedObjectsDrawingView2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsDrawingView2.html)
[ISelectionMgr::GetSelectedObjectType3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectType3.html)
[ISelectionMgr::IGetSelectionPointInSketchSpace2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IGetSelectionPointInSketchSpace2.html)
[ISelectionMgr::IDeSelect2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IDeSelect2.html)
[ISelectionMgr::DeSelect2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~DeSelect2.html)
[ISelectionMgr::SetSelectionPoint2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~SetSelectionPoint2.html)
[ISelectionMgr::GetSelectByIdSpecification Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectByIdSpecification.html)
[ISelectionMgr::GetSelectionSpecification Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionSpecification.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0

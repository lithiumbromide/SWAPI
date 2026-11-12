---
title: "IGetSelectionPointInSketchSpace2 Method (ISelectionMgr)"
project: "SOLIDWORKS API Help"
interface: "ISelectionMgr"
member: "IGetSelectionPointInSketchSpace2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IGetSelectionPointInSketchSpace2.html"
---

# IGetSelectionPointInSketchSpace2 Method (ISelectionMgr)

Gets the selection point projected on to the active sketch and returned in sketch space.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSelectionPointInSketchSpace2( _
   ByVal Index As System.Integer, _
   ByVal Mark As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectionMgr
Dim Index As System.Integer
Dim Mark As System.Integer
Dim value As System.Double

value = instance.IGetSelectionPointInSketchSpace2(Index, Mark)
```

### C#

```csharp
System.double IGetSelectionPointInSketchSpace2(
   System.int Index,
   System.int Mark
)
```

### C++/CLI

```cpp
System.double IGetSelectionPointInSketchSpace2(
   System.int Index,
   System.int Mark
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index position with in the current list of selected items, where AtIndex ranges from 1 to [ISelectionMgr::GetSelectedObjectCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectedObjectCount2.html) (see **Remarks**)
- `Mark`: - -1 = All selections regardless of marks
  - 0 = only the selections without marks
  - Any other value that was used to mark and select an object

### Return Value

- in-process, unmanaged C++: Pointer to an array of 3 doubles (see **Remarks**)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## VBA Syntax

See [SelectionMgr::IGetSelectionPointInSketchSpace2](ms-its:sldworksapivb6.chm::/sldworks~SelectionMgr~IGetSelectionPointInSketchSpace2.html).

## Remarks

The selection point is projected on to the currently active sketch, resulting in a z value of 0.00.

If a sketch is not currently active, then the return value is the same as that returned by [ISelectionMgr::GetSelectionPoint2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectionPoint2.html) or [ISelectionMgr::IGetSelectionPoint2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~IGetSelectionPoint2.html). You can determine if a sketch is active by checking for a null return value from [IModelDoc2::GetActiveSketch2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetActiveSketch2.html) or [IModelDoc2::IGetActiveSketch2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IGetActiveSketch2.html).

The index starts at 1. However, if you specify -1 for the Index argument, then the Mark argument is ignored and the dynamically highlighted view is selected if dynamic highlighting is turned on. See also IAssemblyDoc event [DynamicHighlightNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DAssemblyDocEvents_DynamicHighlightNotifyEventHandler.html), IDrawingDoc event [DynamicHighlightNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_DynamicHighlightNotifyEventHandler.html), and IPartDoc event [DynamicHighlightNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_DynamicHighlightNotifyEventHandler.html).

## See Also

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html)
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.html)
[ISelectionMgr::GetSelectionPointInSketchSpace2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionPointInSketchSpace2.html)
[ISelectionMgr::DeSelect2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~DeSelect2.html)
[ISelectionMgr::GetSelectedObject6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.html)
[ISelectionMgr::GetSelectedObjectLoop2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectLoop2.html)
[ISelectionMgr::GetSelectedObjectMark Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectMark.html)
[ISelectionMgr::GetSelectedObjectsComponent3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsComponent3.html)
[ISelectionMgr::GetSelectedObjectsDrawingView2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsDrawingView2.html)
[ISelectionMgr::GetSelectedObjectType3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectType3.html)
[ISelectionMgr::IDeSelect2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IDeSelect2.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0

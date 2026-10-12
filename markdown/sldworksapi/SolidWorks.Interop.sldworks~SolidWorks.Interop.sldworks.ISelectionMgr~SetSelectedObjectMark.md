---
title: "SetSelectedObjectMark Method (ISelectionMgr)"
project: "SOLIDWORKS API Help"
interface: "ISelectionMgr"
member: "SetSelectedObjectMark"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~SetSelectedObjectMark.html"
---

# SetSelectedObjectMark Method (ISelectionMgr)

Sets the mark value for the specified selection.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetSelectedObjectMark( _
   ByVal AtIndex As System.Integer, _
   ByVal Mark As System.Integer, _
   ByVal Action As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectionMgr
Dim AtIndex As System.Integer
Dim Mark As System.Integer
Dim Action As System.Integer
Dim value As System.Boolean

value = instance.SetSelectedObjectMark(AtIndex, Mark, Action)
```

### C#

```csharp
System.bool SetSelectedObjectMark(
   System.int AtIndex,
   System.int Mark,
   System.int Action
)
```

### C++/CLI

```cpp
System.bool SetSelectedObjectMark(
   System.int AtIndex,
   System.int Mark,
   System.int Action
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AtIndex`: 1 <= Index position within the current list of selected items <= [ISelectionMgr::GetSelectedObjectCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectedObjectCount2.html)
- `Mark`: Number to use as a mark for the selected item; this number is used by certain API functions that require ordered entity selection
- `Action`: Action to take as defined in [swSelectionMarkAction_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectionMarkAction_e.html)

### Return Value

True if the selection is successfully set, false if not

## VBA Syntax

See [SelectionMgr::SetSelectedObjectMark](ms-its:sldworksapivb6.chm::/sldworks~SelectionMgr~SetSelectedObjectMark.html).

## Examples

[Thicken Surface and Generate Boss (VBA)](Thicken_Surface_and_Generate_Boss_Example_VB.htm)
[Thicken Surface and Generate Boss (VB.NET)](Thicken_Surface_and_Generate_Boss_Example_VBNET.htm)
[Thicken Surface and Generate Boss (C#)](Thicken_Surface_and_Generate_Boss_Example_CSharp.htm)

## See Also

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html)
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.html)
[ISelectionMgr::GetSelectedObjectMark Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectMark.html)
[ISelectionMgr::GetSelectedObject6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.html)
[ISelectionMgr::GetSelectedObjectCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectCount2.html)
[ISelectionMgr::GetSelectedObjectLoop2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectLoop2.html)
[ISelectionMgr::GetSelectedObjectsComponent3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsComponent3.html)
[ISelectionMgr::GetSelectedObjectsDrawingView2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsDrawingView2.html)
[ISelectionMgr::GetSelectedObjectType3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectType3.html)
[ISelectionMgr::GetSelectionPoint2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionPoint2.html)
[ISelectionMgr::GetSelectionPointInSketchSpace2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionPointInSketchSpace2.html)
[ISelectionMgr::IGetSelectedObjectsComponent2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IGetSelectedObjectsComponent2.html)
[ISelectionMgr::IGetSelectionPointInSketchSpace2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IGetSelectionPointInSketchSpace2.html)
[ISelectionMgr::SetSelectionPoint2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~SetSelectionPoint2.html)
[ISelectionMgr::DeSelect2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~DeSelect2.html)
[ISelectionMgr::IDeSelect2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IDeSelect2.html)
[ISelectionMgr::GetSelectByIdSpecification Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectByIdSpecification.html)
[ISelectionMgr::GetSelectionSpecification Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionSpecification.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0

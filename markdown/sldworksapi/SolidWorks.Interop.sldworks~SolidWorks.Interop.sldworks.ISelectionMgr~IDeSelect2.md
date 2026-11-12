---
title: "IDeSelect2 Method (ISelectionMgr)"
project: "SOLIDWORKS API Help"
interface: "ISelectionMgr"
member: "IDeSelect2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IDeSelect2.html"
---

# IDeSelect2 Method (ISelectionMgr)

Deselects the specified entity.

## Syntax

### Visual Basic (Declaration)

```vb
Function IDeSelect2( _
   ByVal Count As System.Integer, _
   ByRef AtIndex As System.Integer, _
   ByVal Mark As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectionMgr
Dim Count As System.Integer
Dim AtIndex As System.Integer
Dim Mark As System.Integer
Dim value As System.Integer

value = instance.IDeSelect2(Count, AtIndex, Mark)
```

### C#

```csharp
System.int IDeSelect2(
   System.int Count,
   ref System.int AtIndex,
   System.int Mark
)
```

### C++/CLI

```cpp
System.int IDeSelect2(
   System.int Count,
   System.int% AtIndex,
   System.int Mark
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of objects to deselect
- `AtIndex`: Index position within the current list of selected items where index ranges from 1 to [ISelectionMgr::GetSelectedObjectCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectedObjectCount2.html) (see **Remarks**)
- `Mark`: - -1 = All selections regardless of marks

  0 = only the selections without marks

  Any other value = Value that was used to mark and select an object

### Return Value

1 if the specified entity is deselected, 0 if not

## VBA Syntax

See [SelectionMgr::IDeSelect2](ms-its:sldworksapivb6.chm::/sldworks~SelectionMgr~IDeSelect2.html).

## Remarks

AtIndex should be either an array of 32-bit integers or a single 32-bit integer. See [Long vs. Integer](sldworksapiprogguide.chm::/overview/Long_vs_Integer.htm) for details about data types.

## See Also

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html)
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.html)
[ISelectionMgr::DeSelect2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~DeSelect2.html)
[ISelectionMgr::GetSelectedObject6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.html)
[ISelectionMgr::GetSelectedObjectCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectCount2.html)
[ISelectionMgr::GetSelectedObjectLoop2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectLoop2.html)
[ISelectionMgr::GetSelectedObjectMark Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectMark.html)
[ISelectionMgr::GetSelectedObjectsComponent3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsComponent3.html)
[ISelectionMgr::GetSelectedObjectsDrawingView2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsDrawingView2.html)
[ISelectionMgr::GetSelectedObjectType3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectType3.html)
[ISelectionMgr::GetSelectionPoint2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionPoint2.html)
[ISelectionMgr::GetSelectionPointInSketchSpace2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionPointInSketchSpace2.html)
[ISelectionMgr::IGetSelectionPoint2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IGetSelectionPoint2.html)
[ISelectionMgr::IGetSelectionPointInSketchSpace2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IGetSelectionPointInSketchSpace2.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0

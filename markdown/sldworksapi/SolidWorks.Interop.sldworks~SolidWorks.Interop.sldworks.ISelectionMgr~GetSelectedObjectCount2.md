---
title: "GetSelectedObjectCount2 Method (ISelectionMgr)"
project: "SOLIDWORKS API Help"
interface: "ISelectionMgr"
member: "GetSelectedObjectCount2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectCount2.html"
---

# GetSelectedObjectCount2 Method (ISelectionMgr)

Gets the number of selected objects.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSelectedObjectCount2( _
   ByVal Mark As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectionMgr
Dim Mark As System.Integer
Dim value As System.Integer

value = instance.GetSelectedObjectCount2(Mark)
```

### C#

```csharp
System.int GetSelectedObjectCount2(
   System.int Mark
)
```

### C++/CLI

```cpp
System.int GetSelectedObjectCount2(
   System.int Mark
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Mark`: - -1 = All selections regardless of marks

  0 = only the selections without marks

  Any other value = Value that was used to mark and select an object

### Return Value

Number of selected objects

## VBA Syntax

See [SelectionMgr::GetSelectedObjectCount2](ms-its:sldworksapivb6.chm::/sldworks~SelectionMgr~GetSelectedObjectCount2.html).

## Examples

[Create Multi-row Callouts (VBA)](Create_Multi-row_Callouts_Example_VB.htm)
[Selection Lists (VBA)](Selection_Lists_VB.htm)
[Create Library Feature With References (C#)](Create_Library_Feature_With_References_Example_CSharp.htm)
[Create Library Feature With References (VB.NET)](Create_Library_Feature_With_References_Example_VBNET.htm)
[Create Library Feature With References (VBA)](Create_Library_Feature_With_References_Example_VB.htm)

## Remarks

This method can be used to determine if a valid selection was made.

## See Also

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html)
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.html)
[ISelectionMgr::GetSelectedObject6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.html)
[ISelectionMgr::GetSelectedObjectLoop2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectLoop2.html)
[ISelectionMgr::GetSelectedObjectMark Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectMark.html)
[ISelectionMgr::GetSelectedObjectsComponent3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsComponent3.html)
[ISelectionMgr::GetSelectedObjectsDrawingView2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsDrawingView2.html)
[ISelectionMgr::GetSelectedObjectType3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectType3.html)
[ISelectionMgr::GetSelectionPoint2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionPoint2.html)
[ISelectionMgr::GetSelectionPointInSketchSpace2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionPointInSketchSpace2.html)
[ISelectionMgr::IGetSelectionPointInSketchSpace2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IGetSelectionPointInSketchSpace2.html)
[ISelectionMgr::DeSelect2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~DeSelect2.html)
[ISelectionMgr::IDeSelect2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IDeSelect2.html)
[ISelectionMgr::IGetSelectionPoint2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IGetSelectionPoint2.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0

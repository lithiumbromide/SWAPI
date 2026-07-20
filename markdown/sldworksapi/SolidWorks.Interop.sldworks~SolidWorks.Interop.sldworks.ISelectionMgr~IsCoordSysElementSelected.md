---
title: "IsCoordSysElementSelected Method (ISelectionMgr)"
project: "SOLIDWORKS API Help"
interface: "ISelectionMgr"
member: "IsCoordSysElementSelected"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IsCoordSysElementSelected.html"
---

# IsCoordSysElementSelected Method (ISelectionMgr)

Gets whether the selection is a coordinate system element.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsCoordSysElementSelected( _
   ByVal Index As System.Integer, _
   ByVal Mark As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectionMgr
Dim Index As System.Integer
Dim Mark As System.Integer
Dim value As System.Boolean

value = instance.IsCoordSysElementSelected(Index, Mark)
```

### C#

```csharp
System.bool IsCoordSysElementSelected(
   System.int Index,
   System.int Mark
)
```

### C++/CLI

```cpp
System.bool IsCoordSysElementSelected(
   System.int Index,
   System.int Mark
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `Index`: Index position within the current list of selected items, where Index ranges from 1 to[ISelectionMgr::GetSelectedObjectCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectedObjectCount2.html)(see**Remarks**)
- `Mark`: - -1 = All selections regardless of marks

- 0 = only the selections without marks

Any other value = Value that was used to mark and select an object

### Return Value

True if coordinate system element selected, false if not

## VBA Syntax

See

[SelectionMgr::IsCoordSysElementSelected](ms-its:sldworksapivb6.chm::/sldworks~SelectionMgr~IsCoordSysElementSelected.html)

.

## Examples

See the

[ICoordinateSystemElement](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemElement.html)

examples.

## Remarks

Call this method after calling

[ISelectionMgr::GetSelectedCoordSysElement](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedCoordSysElement.html)

to confirm that a coordinate system element is retrieved.

## See Also

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html)

[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.html)

## Availability

SOLIDWORKS 2025 SP01, Revision Number 33.1

---
title: "GetSelectedCoordSysElement Method (ISelectionMgr)"
project: "SOLIDWORKS API Help"
interface: "ISelectionMgr"
member: "GetSelectedCoordSysElement"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedCoordSysElement.html"
---

# GetSelectedCoordSysElement Method (ISelectionMgr)

Gets the selected coordinate system element.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSelectedCoordSysElement( _
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

value = instance.GetSelectedCoordSysElement(Index, Mark)
```

### C#

```csharp
System.object GetSelectedCoordSysElement(
   System.int Index,
   System.int Mark
)
```

### C++/CLI

```cpp
System.Object^ GetSelectedCoordSysElement(
   System.int Index,
   System.int Mark
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `Index`: Index position within the current list of selected items, where Index ranges from 1 to

[ISelectionMgr::GetSelectedObjectCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectedObjectCount2.html)

(see

Remarks

)
- `Mark`: - -1 = All selections regardless of marks

- 0 = only the selections without marks

Any other value = Value that was used to mark and select an object

### Return Value

[ICoordinateSystemElement](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemElement.html)

## VBA Syntax

See

[SelectionMgr::GetSelectedCoordSysElement](ms-its:sldworksapivb6.chm::/sldworks~SelectionMgr~GetSelectedCoordSysElement.html)

.

## Examples

See the

[ICoordinateSystemElement](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemElement.html)

examples.

## Remarks

After calling this method, call

[ISelectionMgr::IsCoordSysElementSelected](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IsCoordSysElementSelected.html)

.

## See Also

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html)

[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.html)

## Availability

SOLIDWORKS 2025 SP01, Revision Number 33.1

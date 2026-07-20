---
title: "IsInEditTarget2 Method (ISelectionMgr)"
project: "SOLIDWORKS API Help"
interface: "ISelectionMgr"
member: "IsInEditTarget2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IsInEditTarget2.html"
---

# IsInEditTarget2 Method (ISelectionMgr)

Gets whether the selected object is in the edit target.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsInEditTarget2( _
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

value = instance.IsInEditTarget2(Index, Mark)
```

### C#

```csharp
System.bool IsInEditTarget2(
   System.int Index,
   System.int Mark
)
```

### C++/CLI

```cpp
System.bool IsInEditTarget2(
   System.int Index,
   System.int Mark
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `Index`: Index position with in the current list of selected items, where AtIndex ranges from 1 to[ISelectionMgr::GetSelectedObjectCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectedObjectCount2.html)(see**Remarks**)
- `Mark`: - -1 = All selections regardless of marks

- 0 = only the selections without marks

Any other value = Value that was used to mark and select an object

### Return Value

True if the selected item specified by AtIndex belongs to a model that is the current edit target, false if not

## VBA Syntax

See

[SelectionMgr::IsInEditTarget2](ms-its:sldworksapivb6.chm::/sldworks~SelectionMgr~IsInEditTarget2.html)

.

## Remarks

Calling this method is necessary in assemblies when the end-user performs in-context editing of a part. This method allows you to determine if a selected item belongs to the model that is the current edit target.

The index starts at 1, even when using C++. However, if you specify -1 for the Index argument, then the Mark argument is ignored and the dynamically highlighted view is selected if dynamic highlighting is turned on. See also IAssemblyDoc event[DynamicHighlightNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DAssemblyDocEvents_DynamicHighlightNotifyEventHandler.html), IDrawingDoc event[DynamicHighlightNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_DynamicHighlightNotifyEventHandler.html), and IPartDoc event[DynamicHighlightNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_DynamicHighlightNotifyEventHandler.html).

## See Also

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html)

[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0

---
title: "GetSelectedObjectsDrawingView Method (ISelectionMgr)"
project: "SOLIDWORKS API Help"
interface: "ISelectionMgr"
member: "GetSelectedObjectsDrawingView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsDrawingView.html"
---

# GetSelectedObjectsDrawingView Method (ISelectionMgr)

Obsolete. Superseded by [ISelectionMgr::GetSelectedObjectsDrawingView2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectedObjectsDrawingView2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSelectedObjectsDrawingView( _
   ByVal AtIndex As System.Integer _
) As View
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectionMgr
Dim AtIndex As System.Integer
Dim value As View

value = instance.GetSelectedObjectsDrawingView(AtIndex)
```

### C#

```csharp
View GetSelectedObjectsDrawingView(
   System.int AtIndex
)
```

### C++/CLI

```cpp
View^ GetSelectedObjectsDrawingView(
   System.int AtIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AtIndex`:

## VBA Syntax

See [SelectionMgr::GetSelectedObjectsDrawingView](ms-its:sldworksapivb6.chm::/sldworks~SelectionMgr~GetSelectedObjectsDrawingView.html).

## See Also

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html)
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.html)

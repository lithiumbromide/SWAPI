---
title: "GetSelectedObjectsFace Method (ISelectionMgr)"
project: "SOLIDWORKS API Help"
interface: "ISelectionMgr"
member: "GetSelectedObjectsFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsFace.html"
---

# GetSelectedObjectsFace Method (ISelectionMgr)

Gets the face of the specified selection if the specified selection is a [silhouette edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISilhouetteEdge.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSelectedObjectsFace( _
   ByVal AtIndex As System.Integer, _
   ByVal Mark As System.Integer _
) As Face2
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectionMgr
Dim AtIndex As System.Integer
Dim Mark As System.Integer
Dim value As Face2

value = instance.GetSelectedObjectsFace(AtIndex, Mark)
```

### C#

```csharp
Face2 GetSelectedObjectsFace(
   System.int AtIndex,
   System.int Mark
)
```

### C++/CLI

```cpp
Face2^ GetSelectedObjectsFace(
   System.int AtIndex,
   System.int Mark
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AtIndex`: Index position within the current list of selected items, where AtIndex ranges from 1 to [ISelectionMgr::GetSelectedObjectCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectedObjectCount2.html)
- `Mark`: - 1 = All selections regardless of marks

  0 = only the selections without marks

  Any other value = Value that was used to mark and select an object

### Return Value

[Face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

## VBA Syntax

See [SelectionMgr::GetSelectedObjectsFace](ms-its:sldworksapivb6.chm::/Sldworks~SelectionMgr~GetSelectedObjectsFace.html).

## See Also

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html)
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0

---
title: "GetSelectionPointInSketchSpace Method (ISelectionMgr)"
project: "SOLIDWORKS API Help"
interface: "ISelectionMgr"
member: "GetSelectionPointInSketchSpace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionPointInSketchSpace.html"
---

# GetSelectionPointInSketchSpace Method (ISelectionMgr)

Obsolete. Superseded by [ISelectionMgr::GetSelectionPointInSketchSpace2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectionPointInSketchSpace2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSelectionPointInSketchSpace( _
   ByVal AtIndex As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectionMgr
Dim AtIndex As System.Integer
Dim value As System.Object

value = instance.GetSelectionPointInSketchSpace(AtIndex)
```

### C#

```csharp
System.object GetSelectionPointInSketchSpace(
   System.int AtIndex
)
```

### C++/CLI

```cpp
System.Object^ GetSelectionPointInSketchSpace(
   System.int AtIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AtIndex`:

## VBA Syntax

See [SelectionMgr::GetSelectionPointInSketchSpace](ms-its:sldworksapivb6.chm::/sldworks~SelectionMgr~GetSelectionPointInSketchSpace.html).

## See Also

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html)
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.html)

---
title: "IGetSelectedObjectsComponent Method (ISelectionMgr)"
project: "SOLIDWORKS API Help"
interface: "ISelectionMgr"
member: "IGetSelectedObjectsComponent"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IGetSelectedObjectsComponent.html"
---

# IGetSelectedObjectsComponent Method (ISelectionMgr)

Obsolete. Superseded by [ISelectionMgr::GetSelectedObjectsComponent3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectedObjectsComponent3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSelectedObjectsComponent( _
   ByVal AtIndex As System.Integer _
) As Component
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectionMgr
Dim AtIndex As System.Integer
Dim value As Component

value = instance.IGetSelectedObjectsComponent(AtIndex)
```

### C#

```csharp
Component IGetSelectedObjectsComponent(
   System.int AtIndex
)
```

### C++/CLI

```cpp
Component^ IGetSelectedObjectsComponent(
   System.int AtIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AtIndex`:

## VBA Syntax

See [SelectionMgr::IGetSelectedObjectsComponent](ms-its:sldworksapivb6.chm::/sldworks~SelectionMgr~IGetSelectedObjectsComponent.html).

## See Also

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html)
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.html)

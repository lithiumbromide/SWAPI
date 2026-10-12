---
title: "IGetSelectedObjectsComponent2 Method (ISelectionMgr)"
project: "SOLIDWORKS API Help"
interface: "ISelectionMgr"
member: "IGetSelectedObjectsComponent2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IGetSelectedObjectsComponent2.html"
---

# IGetSelectedObjectsComponent2 Method (ISelectionMgr)

Obsolete. Superseded by [ISelectionMgr::GetSelectedObjectsComponent3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectedObjectsComponent3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSelectedObjectsComponent2( _
   ByVal AtIndex As System.Integer _
) As Component2
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectionMgr
Dim AtIndex As System.Integer
Dim value As Component2

value = instance.IGetSelectedObjectsComponent2(AtIndex)
```

### C#

```csharp
Component2 IGetSelectedObjectsComponent2(
   System.int AtIndex
)
```

### C++/CLI

```cpp
Component2^ IGetSelectedObjectsComponent2(
   System.int AtIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AtIndex`:

## VBA Syntax

See [SelectionMgr::IGetSelectedObjectsComponent2](ms-its:sldworksapivb6.chm::/sldworks~SelectionMgr~IGetSelectedObjectsComponent2.html).

## See Also

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html)
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.html)

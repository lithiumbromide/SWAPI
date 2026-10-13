---
title: "GetSelectedObjectLoop Method (ISelectionMgr)"
project: "SOLIDWORKS API Help"
interface: "ISelectionMgr"
member: "GetSelectedObjectLoop"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectLoop.html"
---

# GetSelectedObjectLoop Method (ISelectionMgr)

Obsolete. Superseded by [ISelectionMgr::GetSelectedObjectLoop2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectedObjectLoop2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSelectedObjectLoop( _
   ByVal AtIndex As System.Integer _
) As Loop2
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectionMgr
Dim AtIndex As System.Integer
Dim value As Loop2

value = instance.GetSelectedObjectLoop(AtIndex)
```

### C#

```csharp
Loop2 GetSelectedObjectLoop(
   System.int AtIndex
)
```

### C++/CLI

```cpp
Loop2^ GetSelectedObjectLoop(
   System.int AtIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AtIndex`:

## VBA Syntax

See [SelectionMgr::GetSelectedObjectLoop](ms-its:sldworksapivb6.chm::/sldworks~SelectionMgr~GetSelectedObjectLoop.html).

## See Also

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html)
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.html)

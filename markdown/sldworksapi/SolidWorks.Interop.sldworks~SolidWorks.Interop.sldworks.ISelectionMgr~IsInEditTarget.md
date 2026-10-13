---
title: "IsInEditTarget Method (ISelectionMgr)"
project: "SOLIDWORKS API Help"
interface: "ISelectionMgr"
member: "IsInEditTarget"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IsInEditTarget.html"
---

# IsInEditTarget Method (ISelectionMgr)

Obsolete. Superseded by [ISelectionMgr::IsInEditTarget2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~IsInEditTarget2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IsInEditTarget( _
   ByVal AtIndex As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectionMgr
Dim AtIndex As System.Integer
Dim value As System.Boolean

value = instance.IsInEditTarget(AtIndex)
```

### C#

```csharp
System.bool IsInEditTarget(
   System.int AtIndex
)
```

### C++/CLI

```cpp
System.bool IsInEditTarget(
   System.int AtIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AtIndex`:

## VBA Syntax

See [SelectionMgr::IsInEditTarget](ms-its:sldworksapivb6.chm::/sldworks~SelectionMgr~IsInEditTarget.html).

## See Also

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html)
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.html)

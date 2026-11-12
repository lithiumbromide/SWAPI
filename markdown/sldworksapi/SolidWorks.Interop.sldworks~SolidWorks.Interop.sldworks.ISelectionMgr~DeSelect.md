---
title: "DeSelect Method (ISelectionMgr)"
project: "SOLIDWORKS API Help"
interface: "ISelectionMgr"
member: "DeSelect"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~DeSelect.html"
---

# DeSelect Method (ISelectionMgr)

Obsolete. Superseded by [ISelectionMgr::DeSelect2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~DeSelect2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function DeSelect( _
   ByVal AtIndex As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectionMgr
Dim AtIndex As System.Object
Dim value As System.Integer

value = instance.DeSelect(AtIndex)
```

### C#

```csharp
System.int DeSelect(
   System.object AtIndex
)
```

### C++/CLI

```cpp
System.int DeSelect(
   System.Object^ AtIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AtIndex`:

## VBA Syntax

See [SelectionMgr::DeSelect](ms-its:sldworksapivb6.chm::/sldworks~SelectionMgr~DeSelect.html).

## See Also

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html)
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.html)

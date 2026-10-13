---
title: "IDeSelect Method (ISelectionMgr)"
project: "SOLIDWORKS API Help"
interface: "ISelectionMgr"
member: "IDeSelect"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IDeSelect.html"
---

# IDeSelect Method (ISelectionMgr)

Obsolete. Superseded by [ISelectionMgr::IDeSelect2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~IDeSelect2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IDeSelect( _
   ByVal Count As System.Integer, _
   ByRef AtIndex As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectionMgr
Dim Count As System.Integer
Dim AtIndex As System.Integer
Dim value As System.Integer

value = instance.IDeSelect(Count, AtIndex)
```

### C#

```csharp
System.int IDeSelect(
   System.int Count,
   ref System.int AtIndex
)
```

### C++/CLI

```cpp
System.int IDeSelect(
   System.int Count,
   System.int% AtIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`:
- `AtIndex`:

## VBA Syntax

See [SelectionMgr::IDeSelect](ms-its:sldworksapivb6.chm::/sldworks~SelectionMgr~IDeSelect.html).

## See Also

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html)
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.html)

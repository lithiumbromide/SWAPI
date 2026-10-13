---
title: "IGetSelectedObject Method (ISelectionMgr)"
project: "SOLIDWORKS API Help"
interface: "ISelectionMgr"
member: "IGetSelectedObject"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IGetSelectedObject.html"
---

# IGetSelectedObject Method (ISelectionMgr)

Obsolete. Superseded by [ISelectionMgr::GetSelectedObject6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectedObject6.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSelectedObject( _
   ByVal AtIndex As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectionMgr
Dim AtIndex As System.Integer
Dim value As System.Object

value = instance.IGetSelectedObject(AtIndex)
```

### C#

```csharp
System.object IGetSelectedObject(
   System.int AtIndex
)
```

### C++/CLI

```cpp
System.Object^ IGetSelectedObject(
   System.int AtIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AtIndex`:

## VBA Syntax

See [SelectionMgr::IGetSelectedObject](ms-its:sldworksapivb6.chm::/sldworks~SelectionMgr~IGetSelectedObject.html).

## See Also

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html)
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.html)

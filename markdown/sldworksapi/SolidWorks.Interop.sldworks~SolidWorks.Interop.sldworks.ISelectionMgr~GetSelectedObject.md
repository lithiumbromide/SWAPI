---
title: "GetSelectedObject Method (ISelectionMgr)"
project: "SOLIDWORKS API Help"
interface: "ISelectionMgr"
member: "GetSelectedObject"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject.html"
---

# GetSelectedObject Method (ISelectionMgr)

Obsolete. Superseded by [ISelectionMgr::GetSelectedObject6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectedObject6.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSelectedObject( _
   ByVal AtIndex As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectionMgr
Dim AtIndex As System.Integer
Dim value As System.Object

value = instance.GetSelectedObject(AtIndex)
```

### C#

```csharp
System.object GetSelectedObject(
   System.int AtIndex
)
```

### C++/CLI

```cpp
System.Object^ GetSelectedObject(
   System.int AtIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AtIndex`:

## VBA Syntax

See [SelectionMgr::GetSelectedObject](ms-its:sldworksapivb6.chm::/sldworks~SelectionMgr~GetSelectedObject.html).

## See Also

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html)
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.html)

---
title: "GetSelectedObjectType Method (ISelectionMgr)"
project: "SOLIDWORKS API Help"
interface: "ISelectionMgr"
member: "GetSelectedObjectType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectType.html"
---

# GetSelectedObjectType Method (ISelectionMgr)

Obsolete. Superseded by [ISelectionMgr::GetSelectedObjectType3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectedObjectType3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSelectedObjectType( _
   ByVal AtIndex As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectionMgr
Dim AtIndex As System.Integer
Dim value As System.Integer

value = instance.GetSelectedObjectType(AtIndex)
```

### C#

```csharp
System.int GetSelectedObjectType(
   System.int AtIndex
)
```

### C++/CLI

```cpp
System.int GetSelectedObjectType(
   System.int AtIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AtIndex`:

## VBA Syntax

See [SelectionMgr::GetSelectedObjectType](ms-its:sldworksapivb6.chm::/sldworks~SelectionMgr~GetSelectedObjectType.html).

## See Also

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html)
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.html)

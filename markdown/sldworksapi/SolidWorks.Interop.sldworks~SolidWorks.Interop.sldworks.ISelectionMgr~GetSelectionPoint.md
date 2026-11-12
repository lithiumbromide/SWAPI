---
title: "GetSelectionPoint Method (ISelectionMgr)"
project: "SOLIDWORKS API Help"
interface: "ISelectionMgr"
member: "GetSelectionPoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionPoint.html"
---

# GetSelectionPoint Method (ISelectionMgr)

Obsolete. Superseded by [ISelectionMgr::GetSelectionPoint2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~IGetSelectionPoint2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSelectionPoint( _
   ByVal AtIndex As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectionMgr
Dim AtIndex As System.Integer
Dim value As System.Object

value = instance.GetSelectionPoint(AtIndex)
```

### C#

```csharp
System.object GetSelectionPoint(
   System.int AtIndex
)
```

### C++/CLI

```cpp
System.Object^ GetSelectionPoint(
   System.int AtIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AtIndex`:

## VBA Syntax

See [SelectionMgr::GetSelectionPoint](ms-its:sldworksapivb6.chm::/sldworks~SelectionMgr~GetSelectionPoint.html).

## See Also

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html)
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.html)

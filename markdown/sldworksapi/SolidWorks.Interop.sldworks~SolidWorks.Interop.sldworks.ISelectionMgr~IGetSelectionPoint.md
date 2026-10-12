---
title: "IGetSelectionPoint Method (ISelectionMgr)"
project: "SOLIDWORKS API Help"
interface: "ISelectionMgr"
member: "IGetSelectionPoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IGetSelectionPoint.html"
---

# IGetSelectionPoint Method (ISelectionMgr)

Obsolete. Superseded by [ISelectionMgr::IGetSelectionPoint2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~IGetSelectionPoint2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSelectionPoint( _
   ByVal AtIndex As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectionMgr
Dim AtIndex As System.Integer
Dim value As System.Double

value = instance.IGetSelectionPoint(AtIndex)
```

### C#

```csharp
System.double IGetSelectionPoint(
   System.int AtIndex
)
```

### C++/CLI

```cpp
System.double IGetSelectionPoint(
   System.int AtIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AtIndex`:

## VBA Syntax

See [SelectionMgr::IGetSelectionPoint](ms-its:sldworksapivb6.chm::/sldworks~SelectionMgr~IGetSelectionPoint.html).

## See Also

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html)
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.html)

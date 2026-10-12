---
title: "IGetSelectionPointInSketchSpace Method (ISelectionMgr)"
project: "SOLIDWORKS API Help"
interface: "ISelectionMgr"
member: "IGetSelectionPointInSketchSpace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IGetSelectionPointInSketchSpace.html"
---

# IGetSelectionPointInSketchSpace Method (ISelectionMgr)

Obsolete. Superseded by [ISelectionMgr::IGetSelectionPointInSketchSpace2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~IGetSelectionPointInSketchSpace2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSelectionPointInSketchSpace( _
   ByVal AtIndex As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectionMgr
Dim AtIndex As System.Integer
Dim value As System.Double

value = instance.IGetSelectionPointInSketchSpace(AtIndex)
```

### C#

```csharp
System.double IGetSelectionPointInSketchSpace(
   System.int AtIndex
)
```

### C++/CLI

```cpp
System.double IGetSelectionPointInSketchSpace(
   System.int AtIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AtIndex`:

## VBA Syntax

See [SelectionMgr::IGetSelectionPointInSketchSpace](ms-its:sldworksapivb6.chm::/sldworks~SelectionMgr~IGetSelectionPointInSketchSpace.html).

## See Also

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html)
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.html)

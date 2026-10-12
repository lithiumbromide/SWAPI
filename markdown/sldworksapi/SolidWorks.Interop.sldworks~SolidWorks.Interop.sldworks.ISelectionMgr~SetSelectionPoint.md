---
title: "SetSelectionPoint Method (ISelectionMgr)"
project: "SOLIDWORKS API Help"
interface: "ISelectionMgr"
member: "SetSelectionPoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~SetSelectionPoint.html"
---

# SetSelectionPoint Method (ISelectionMgr)

Obsolete. Superseded by [ISelectionMgr::SetSelectionPoint2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~SetSelectionPoint2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetSelectionPoint( _
   ByVal AtIndex As System.Integer, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectionMgr
Dim AtIndex As System.Integer
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Boolean

value = instance.SetSelectionPoint(AtIndex, X, Y, Z)
```

### C#

```csharp
System.bool SetSelectionPoint(
   System.int AtIndex,
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
System.bool SetSelectionPoint(
   System.int AtIndex,
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AtIndex`:
- `X`:
- `Y`:
- `Z`:

## VBA Syntax

See [SelectionMgr::SetSelectionPoint](ms-its:sldworksapivb6.chm::/sldworks~SelectionMgr~SetSelectionPoint.html).

## See Also

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html)
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.html)

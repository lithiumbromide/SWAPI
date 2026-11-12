---
title: "IGetLeaderAtIndex Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "IGetLeaderAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetLeaderAtIndex.html"
---

# IGetLeaderAtIndex Method (IGtol)

Obsolete. Superseded by [IGtol::IGetLeaderAtIndex2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~IGetLeaderAtIndex2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetLeaderAtIndex( _
   ByVal Index As System.Integer, _
   ByRef PointCount As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim Index As System.Integer
Dim PointCount As System.Integer
Dim value As System.Double

value = instance.IGetLeaderAtIndex(Index, PointCount)
```

### C#

```csharp
System.double IGetLeaderAtIndex(
   System.int Index,
   out System.int PointCount
)
```

### C++/CLI

```cpp
System.double IGetLeaderAtIndex(
   System.int Index,
   [Out] System.int PointCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`:
- `PointCount`:

## VBA Syntax

See [Gtol::IGetLeaderAtIndex](ms-its:sldworksapivb6.chm::/sldworks~Gtol~IGetLeaderAtIndex.html).

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)

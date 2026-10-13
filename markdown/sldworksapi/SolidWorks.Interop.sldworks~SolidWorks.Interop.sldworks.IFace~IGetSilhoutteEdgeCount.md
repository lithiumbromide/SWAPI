---
title: "IGetSilhoutteEdgeCount Method (IFace)"
project: "SOLIDWORKS API Help"
interface: "IFace"
member: "IGetSilhoutteEdgeCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace~IGetSilhoutteEdgeCount.html"
---

# IGetSilhoutteEdgeCount Method (IFace)

Obsolete. Superseded by [IFace2::IGetSilhoutteEdgeCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~IGetSilhoutteEdgeCount.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSilhoutteEdgeCount( _
   ByRef Root As System.Double, _
   ByRef Normal As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFace
Dim Root As System.Double
Dim Normal As System.Double
Dim value As System.Integer

value = instance.IGetSilhoutteEdgeCount(Root, Normal)
```

### C#

```csharp
System.int IGetSilhoutteEdgeCount(
   ref System.double Root,
   ref System.double Normal
)
```

### C++/CLI

```cpp
System.int IGetSilhoutteEdgeCount(
   System.double% Root,
   System.double% Normal
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Root`:
- `Normal`:

## VBA Syntax

See [Face::IGetSilhoutteEdgeCount](ms-its:sldworksapivb6.chm::/sldworks~Face~IGetSilhoutteEdgeCount.html).

## See Also

[IFace Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace.html)
[IFace Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace_members.html)

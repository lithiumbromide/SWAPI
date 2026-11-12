---
title: "IGetSilhoutteEdges Method (IFace)"
project: "SOLIDWORKS API Help"
interface: "IFace"
member: "IGetSilhoutteEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace~IGetSilhoutteEdges.html"
---

# IGetSilhoutteEdges Method (IFace)

Obsolete. Superseded by [IFace2::IGetSilhoutteEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~IGetSilhoutteEdges.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSilhoutteEdges( _
   ByRef Root As System.Double, _
   ByRef Normal As System.Double _
) As System.IntPtr
```

### Visual Basic (Usage)

```vb
Dim instance As IFace
Dim Root As System.Double
Dim Normal As System.Double
Dim value As System.IntPtr

value = instance.IGetSilhoutteEdges(Root, Normal)
```

### C#

```csharp
System.IntPtr IGetSilhoutteEdges(
   ref System.double Root,
   ref System.double Normal
)
```

### C++/CLI

```cpp
System.IntPtr IGetSilhoutteEdges(
   System.double% Root,
   System.double% Normal
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Root`:
- `Normal`:

## VBA Syntax

See [Face::IGetSilhoutteEdges](ms-its:sldworksapivb6.chm::/sldworks~Face~IGetSilhoutteEdges.html).

## See Also

[IFace Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace.html)
[IFace Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace_members.html)

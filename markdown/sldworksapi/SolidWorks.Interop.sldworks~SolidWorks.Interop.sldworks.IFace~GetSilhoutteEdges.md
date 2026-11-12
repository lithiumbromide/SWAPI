---
title: "GetSilhoutteEdges Method (IFace)"
project: "SOLIDWORKS API Help"
interface: "IFace"
member: "GetSilhoutteEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace~GetSilhoutteEdges.html"
---

# GetSilhoutteEdges Method (IFace)

Obsolete. Superseded by [IFace2::GetSilhoutteEdgesVB](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetSilhoutteEdgesVB.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSilhoutteEdges( _
   ByRef Root As System.Double, _
   ByRef Normal As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFace
Dim Root As System.Double
Dim Normal As System.Double
Dim value As System.Object

value = instance.GetSilhoutteEdges(Root, Normal)
```

### C#

```csharp
System.object GetSilhoutteEdges(
   ref System.double Root,
   ref System.double Normal
)
```

### C++/CLI

```cpp
System.Object^ GetSilhoutteEdges(
   System.double% Root,
   System.double% Normal
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Root`:
- `Normal`:

## VBA Syntax

See [Face::GetSilhoutteEdges](ms-its:sldworksapivb6.chm::/sldworks~Face~GetSilhoutteEdges.html).

## See Also

[IFace Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace.html)
[IFace Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace_members.html)

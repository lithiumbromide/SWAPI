---
title: "GetSilhoutteEdges Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "GetSilhoutteEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetSilhoutteEdges.html"
---

# GetSilhoutteEdges Method (IFace2)

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
Dim instance As IFace2
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

See [Face2::GetSilhoutteEdges](ms-its:sldworksapivb6.chm::/sldworks~Face2~GetSilhoutteEdges.html).

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)

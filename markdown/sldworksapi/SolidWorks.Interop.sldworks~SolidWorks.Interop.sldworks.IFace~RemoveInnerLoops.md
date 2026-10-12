---
title: "RemoveInnerLoops Method (IFace)"
project: "SOLIDWORKS API Help"
interface: "IFace"
member: "RemoveInnerLoops"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace~RemoveInnerLoops.html"
---

# RemoveInnerLoops Method (IFace)

Obsolete. Superseded by [IFace2::RemoveInnterLoops](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~RemoveInnerLoops.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveInnerLoops( _
   ByVal NumOfLoops As System.Integer, _
   ByVal InnerLoopsIn As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFace
Dim NumOfLoops As System.Integer
Dim InnerLoopsIn As System.Object
Dim value As System.Object

value = instance.RemoveInnerLoops(NumOfLoops, InnerLoopsIn)
```

### C#

```csharp
System.object RemoveInnerLoops(
   System.int NumOfLoops,
   System.object InnerLoopsIn
)
```

### C++/CLI

```cpp
System.Object^ RemoveInnerLoops(
   System.int NumOfLoops,
   System.Object^ InnerLoopsIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumOfLoops`:
- `InnerLoopsIn`:

## VBA Syntax

See [Face::RemoveInnerLoops](ms-its:sldworksapivb6.chm::/sldworks~Face~RemoveInnerLoops.html).

## See Also

[IFace Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace.html)
[IFace Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace_members.html)

---
title: "IRemoveInnerLoops Method (IFace)"
project: "SOLIDWORKS API Help"
interface: "IFace"
member: "IRemoveInnerLoops"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace~IRemoveInnerLoops.html"
---

# IRemoveInnerLoops Method (IFace)

Obsolete. Superseded by [IFace2::IRemoveInnterLoops](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~IRemoveInnerLoops.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IRemoveInnerLoops( _
   ByVal NumOfLoops As System.Integer, _
   ByRef InnerLoopsIn As Loop _
) As Face
```

### Visual Basic (Usage)

```vb
Dim instance As IFace
Dim NumOfLoops As System.Integer
Dim InnerLoopsIn As Loop
Dim value As Face

value = instance.IRemoveInnerLoops(NumOfLoops, InnerLoopsIn)
```

### C#

```csharp
Face IRemoveInnerLoops(
   System.int NumOfLoops,
   ref Loop InnerLoopsIn
)
```

### C++/CLI

```cpp
Face^ IRemoveInnerLoops(
   System.int NumOfLoops,
   Loop^% InnerLoopsIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumOfLoops`:
- `InnerLoopsIn`:

## VBA Syntax

See [Face::IRemoveInnerLoops](ms-its:sldworksapivb6.chm::/sldworks~Face~IRemoveInnerLoops.html).

## See Also

[IFace Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace.html)
[IFace Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace_members.html)

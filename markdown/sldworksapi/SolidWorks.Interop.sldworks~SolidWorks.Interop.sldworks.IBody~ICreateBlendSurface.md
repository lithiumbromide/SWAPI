---
title: "ICreateBlendSurface Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "ICreateBlendSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~ICreateBlendSurface.html"
---

# ICreateBlendSurface Method (IBody)

Obsolete. Superseded by [IBody2::ICreateBlendSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ICreateBlendSurface.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateBlendSurface( _
   ByVal Surface1 As Surface, _
   ByVal Range1 As System.Double, _
   ByVal Surface2 As Surface, _
   ByVal Range2 As System.Double, _
   ByRef StartVec As System.Double, _
   ByRef EndVec As System.Double, _
   ByVal HaveHelpVec As System.Integer, _
   ByRef HelpVec As System.Double, _
   ByVal HaveHelpBox As System.Integer, _
   ByRef HelpBox As System.Double _
) As Surface
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim Surface1 As Surface
Dim Range1 As System.Double
Dim Surface2 As Surface
Dim Range2 As System.Double
Dim StartVec As System.Double
Dim EndVec As System.Double
Dim HaveHelpVec As System.Integer
Dim HelpVec As System.Double
Dim HaveHelpBox As System.Integer
Dim HelpBox As System.Double
Dim value As Surface

value = instance.ICreateBlendSurface(Surface1, Range1, Surface2, Range2, StartVec, EndVec, HaveHelpVec, HelpVec, HaveHelpBox, HelpBox)
```

### C#

```csharp
Surface ICreateBlendSurface(
   Surface Surface1,
   System.double Range1,
   Surface Surface2,
   System.double Range2,
   ref System.double StartVec,
   ref System.double EndVec,
   System.int HaveHelpVec,
   ref System.double HelpVec,
   System.int HaveHelpBox,
   ref System.double HelpBox
)
```

### C++/CLI

```cpp
Surface^ ICreateBlendSurface(
   Surface^ Surface1,
   System.double Range1,
   Surface^ Surface2,
   System.double Range2,
   System.double% StartVec,
   System.double% EndVec,
   System.int HaveHelpVec,
   System.double% HelpVec,
   System.int HaveHelpBox,
   System.double% HelpBox
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Surface1`:
- `Range1`:
- `Surface2`:
- `Range2`:
- `StartVec`:
- `EndVec`:
- `HaveHelpVec`:
- `HelpVec`:
- `HaveHelpBox`:
- `HelpBox`:

## VBA Syntax

See [Body::ICreateBlendSurface](ms-its:sldworksapivb6.chm::/sldworks~Body~ICreateBlendSurface.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)

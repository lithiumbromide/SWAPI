---
title: "CreateBlendSurface Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "CreateBlendSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~CreateBlendSurface.html"
---

# CreateBlendSurface Method (IBody)

Obsolete. Superseded by [IBody2::CreateBlendSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~CreateBlendSurface.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateBlendSurface( _
   ByVal Surface1 As System.Object, _
   ByVal Range1 As System.Double, _
   ByVal Surface2 As System.Object, _
   ByVal Range2 As System.Double, _
   ByVal StartVec As System.Object, _
   ByVal EndVec As System.Object, _
   ByVal HaveHelpVec As System.Integer, _
   ByVal HelpVec As System.Object, _
   ByVal HaveHelpBox As System.Integer, _
   ByVal HelpBox As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim Surface1 As System.Object
Dim Range1 As System.Double
Dim Surface2 As System.Object
Dim Range2 As System.Double
Dim StartVec As System.Object
Dim EndVec As System.Object
Dim HaveHelpVec As System.Integer
Dim HelpVec As System.Object
Dim HaveHelpBox As System.Integer
Dim HelpBox As System.Object
Dim value As System.Object

value = instance.CreateBlendSurface(Surface1, Range1, Surface2, Range2, StartVec, EndVec, HaveHelpVec, HelpVec, HaveHelpBox, HelpBox)
```

### C#

```csharp
System.object CreateBlendSurface(
   System.object Surface1,
   System.double Range1,
   System.object Surface2,
   System.double Range2,
   System.object StartVec,
   System.object EndVec,
   System.int HaveHelpVec,
   System.object HelpVec,
   System.int HaveHelpBox,
   System.object HelpBox
)
```

### C++/CLI

```cpp
System.Object^ CreateBlendSurface(
   System.Object^ Surface1,
   System.double Range1,
   System.Object^ Surface2,
   System.double Range2,
   System.Object^ StartVec,
   System.Object^ EndVec,
   System.int HaveHelpVec,
   System.Object^ HelpVec,
   System.int HaveHelpBox,
   System.Object^ HelpBox
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

See [Body::CreateBlendSurface](ms-its:sldworksapivb6.chm::/sldworks~Body~CreateBlendSurface.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)

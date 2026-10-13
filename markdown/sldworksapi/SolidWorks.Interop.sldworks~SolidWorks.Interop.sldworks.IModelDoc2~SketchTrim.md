---
title: "SketchTrim Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SketchTrim"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchTrim.html"
---

# SketchTrim Method (IModelDoc2)

Obsolete. Superseded by [ISketchManager::SketchExtend](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~SketchExtend.html) and [ISketchManager::SketchTrim](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~SketchTrim.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SketchTrim( _
   ByVal Op As System.Integer, _
   ByVal SelEnd As System.Integer, _
   ByVal X As System.Double, _
   ByVal Y As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Op As System.Integer
Dim SelEnd As System.Integer
Dim X As System.Double
Dim Y As System.Double

instance.SketchTrim(Op, SelEnd, X, Y)
```

### C#

```csharp
void SketchTrim(
   System.int Op,
   System.int SelEnd,
   System.double X,
   System.double Y
)
```

### C++/CLI

```cpp
void SketchTrim(
   System.int Op,
   System.int SelEnd,
   System.double X,
   System.double Y
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Op`:
- `SelEnd`:
- `X`:
- `Y`:

## VBA Syntax

See [ModelDoc2::SketchTrim](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SketchTrim.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

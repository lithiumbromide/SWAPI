---
title: "SketchTrim Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SketchTrim"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SketchTrim.html"
---

# SketchTrim Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SketchTrim](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SketchTrim.html).

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
Dim instance As IModelDoc
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

See [ModelDoc::SketchTrim](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SketchTrim.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)

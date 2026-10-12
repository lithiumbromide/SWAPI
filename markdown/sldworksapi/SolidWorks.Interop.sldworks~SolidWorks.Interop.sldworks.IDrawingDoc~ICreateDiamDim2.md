---
title: "ICreateDiamDim2 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "ICreateDiamDim2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateDiamDim2.html"
---

# ICreateDiamDim2 Method (IDrawingDoc)

Obsolete. Superseded by [IDrawingDoc::ICreateDiamDim4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~ICreateDiamDim4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub ICreateDiamDim2( _
   ByVal DimValue As System.Double, _
   ByRef P0 As System.Double, _
   ByRef P1 As System.Double, _
   ByRef P2 As System.Double, _
   ByRef P3 As System.Double, _
   ByVal ArrowSize As System.Double, _
   ByVal Text As System.String, _
   ByVal TextHeight As System.Double, _
   ByVal WitnessGap As System.Double, _
   ByVal WitnessOvershoot As System.Double, _
   ByRef TextPoint As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim DimValue As System.Double
Dim P0 As System.Double
Dim P1 As System.Double
Dim P2 As System.Double
Dim P3 As System.Double
Dim ArrowSize As System.Double
Dim Text As System.String
Dim TextHeight As System.Double
Dim WitnessGap As System.Double
Dim WitnessOvershoot As System.Double
Dim TextPoint As System.Double

instance.ICreateDiamDim2(DimValue, P0, P1, P2, P3, ArrowSize, Text, TextHeight, WitnessGap, WitnessOvershoot, TextPoint)
```

### C#

```csharp
void ICreateDiamDim2(
   System.double DimValue,
   ref System.double P0,
   ref System.double P1,
   ref System.double P2,
   ref System.double P3,
   System.double ArrowSize,
   System.string Text,
   System.double TextHeight,
   System.double WitnessGap,
   System.double WitnessOvershoot,
   ref System.double TextPoint
)
```

### C++/CLI

```cpp
void ICreateDiamDim2(
   System.double DimValue,
   System.double% P0,
   System.double% P1,
   System.double% P2,
   System.double% P3,
   System.double ArrowSize,
   System.String^ Text,
   System.double TextHeight,
   System.double WitnessGap,
   System.double WitnessOvershoot,
   System.double% TextPoint
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DimValue`:
- `P0`:
- `P1`:
- `P2`:
- `P3`:
- `ArrowSize`:
- `Text`:
- `TextHeight`:
- `WitnessGap`:
- `WitnessOvershoot`:
- `TextPoint`:

## VBA Syntax

See [DrawingDoc::ICreateDiamDim2](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~ICreateDiamDim2.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)

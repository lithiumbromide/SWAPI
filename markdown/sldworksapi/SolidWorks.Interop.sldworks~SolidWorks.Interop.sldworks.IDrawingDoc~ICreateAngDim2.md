---
title: "ICreateAngDim2 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "ICreateAngDim2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateAngDim2.html"
---

# ICreateAngDim2 Method (IDrawingDoc)

Obsolete. Superseded by [IDrawingDoc::ICreateAngDim4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~ICreateAngDim4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub ICreateAngDim2( _
   ByRef P0 As System.Double, _
   ByRef P1 As System.Double, _
   ByRef P2 As System.Double, _
   ByRef P3 As System.Double, _
   ByRef P4 As System.Double, _
   ByRef P5 As System.Double, _
   ByRef P6 As System.Double, _
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
Dim P0 As System.Double
Dim P1 As System.Double
Dim P2 As System.Double
Dim P3 As System.Double
Dim P4 As System.Double
Dim P5 As System.Double
Dim P6 As System.Double
Dim ArrowSize As System.Double
Dim Text As System.String
Dim TextHeight As System.Double
Dim WitnessGap As System.Double
Dim WitnessOvershoot As System.Double
Dim TextPoint As System.Double

instance.ICreateAngDim2(P0, P1, P2, P3, P4, P5, P6, ArrowSize, Text, TextHeight, WitnessGap, WitnessOvershoot, TextPoint)
```

### C#

```csharp
void ICreateAngDim2(
   ref System.double P0,
   ref System.double P1,
   ref System.double P2,
   ref System.double P3,
   ref System.double P4,
   ref System.double P5,
   ref System.double P6,
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
void ICreateAngDim2(
   System.double% P0,
   System.double% P1,
   System.double% P2,
   System.double% P3,
   System.double% P4,
   System.double% P5,
   System.double% P6,
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

- `P0`:
- `P1`:
- `P2`:
- `P3`:
- `P4`:
- `P5`:
- `P6`:
- `ArrowSize`:
- `Text`:
- `TextHeight`:
- `WitnessGap`:
- `WitnessOvershoot`:
- `TextPoint`:

## VBA Syntax

See [DrawingDoc::ICreateAngDim2](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~ICreateAngDim2.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)

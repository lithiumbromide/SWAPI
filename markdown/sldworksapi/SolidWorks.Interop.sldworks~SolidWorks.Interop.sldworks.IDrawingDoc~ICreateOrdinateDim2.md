---
title: "ICreateOrdinateDim2 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "ICreateOrdinateDim2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateOrdinateDim2.html"
---

# ICreateOrdinateDim2 Method (IDrawingDoc)

Obsolete. Superseded by [IDrawingDoc::ICreateOrdinateDim4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~CreateOrdinateDim4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub ICreateOrdinateDim2( _
   ByRef P0 As System.Double, _
   ByRef P1 As System.Double, _
   ByRef P2 As System.Double, _
   ByRef P3 As System.Double, _
   ByRef P4 As System.Double, _
   ByVal Angle As System.Double, _
   ByVal ArrowSize As System.Double, _
   ByVal Text As System.String, _
   ByVal TextHeight As System.Double, _
   ByVal WitnessGap As System.Double, _
   ByVal WitnessOvershoot As System.Double, _
   ByRef P5 As System.Double _
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
Dim Angle As System.Double
Dim ArrowSize As System.Double
Dim Text As System.String
Dim TextHeight As System.Double
Dim WitnessGap As System.Double
Dim WitnessOvershoot As System.Double
Dim P5 As System.Double

instance.ICreateOrdinateDim2(P0, P1, P2, P3, P4, Angle, ArrowSize, Text, TextHeight, WitnessGap, WitnessOvershoot, P5)
```

### C#

```csharp
void ICreateOrdinateDim2(
   ref System.double P0,
   ref System.double P1,
   ref System.double P2,
   ref System.double P3,
   ref System.double P4,
   System.double Angle,
   System.double ArrowSize,
   System.string Text,
   System.double TextHeight,
   System.double WitnessGap,
   System.double WitnessOvershoot,
   ref System.double P5
)
```

### C++/CLI

```cpp
void ICreateOrdinateDim2(
   System.double% P0,
   System.double% P1,
   System.double% P2,
   System.double% P3,
   System.double% P4,
   System.double Angle,
   System.double ArrowSize,
   System.String^ Text,
   System.double TextHeight,
   System.double WitnessGap,
   System.double WitnessOvershoot,
   System.double% P5
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `P0`:
- `P1`:
- `P2`:
- `P3`:
- `P4`:
- `Angle`:
- `ArrowSize`:
- `Text`:
- `TextHeight`:
- `WitnessGap`:
- `WitnessOvershoot`:
- `P5`:

## VBA Syntax

See [DrawingDoc::ICreateOrdinateDim2](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~ICreateOrdinateDim2.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)

---
title: "ICreateLinearDim3 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "ICreateLinearDim3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateLinearDim3.html"
---

# ICreateLinearDim3 Method (IDrawingDoc)

Obsolete. Superseded by [IDrawingDoc::ICreateLinearDim4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~CreateLinearDim4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateLinearDim3( _
   ByRef P0 As System.Double, _
   ByRef P1 As System.Double, _
   ByRef P2 As System.Double, _
   ByRef P3 As System.Double, _
   ByRef P4 As System.Double, _
   ByVal Val As System.Double, _
   ByVal PrimPrec As System.Integer, _
   ByVal Text As System.String, _
   ByRef TextPoint As System.Double, _
   ByVal Angle As System.Double, _
   ByVal TextHeight As System.Double, _
   ByVal Prefix As System.String, _
   ByVal Suffix As System.String, _
   ByVal Callout1 As System.String, _
   ByVal Callout2 As System.String, _
   ByVal TolType As System.Integer, _
   ByVal TolMin As System.String, _
   ByVal TolMax As System.String, _
   ByVal TolPrec As System.Integer, _
   ByVal ArrowSize As System.Double, _
   ByVal ArrowStyle As System.Integer, _
   ByVal ArrowDir As System.Integer, _
   ByVal WitnessGap As System.Double, _
   ByVal WitnessOvershoot As System.Double, _
   ByVal DualDisplay As System.Boolean, _
   ByVal DualPrecision As System.Integer _
) As DisplayDimension
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim P0 As System.Double
Dim P1 As System.Double
Dim P2 As System.Double
Dim P3 As System.Double
Dim P4 As System.Double
Dim Val As System.Double
Dim PrimPrec As System.Integer
Dim Text As System.String
Dim TextPoint As System.Double
Dim Angle As System.Double
Dim TextHeight As System.Double
Dim Prefix As System.String
Dim Suffix As System.String
Dim Callout1 As System.String
Dim Callout2 As System.String
Dim TolType As System.Integer
Dim TolMin As System.String
Dim TolMax As System.String
Dim TolPrec As System.Integer
Dim ArrowSize As System.Double
Dim ArrowStyle As System.Integer
Dim ArrowDir As System.Integer
Dim WitnessGap As System.Double
Dim WitnessOvershoot As System.Double
Dim DualDisplay As System.Boolean
Dim DualPrecision As System.Integer
Dim value As DisplayDimension

value = instance.ICreateLinearDim3(P0, P1, P2, P3, P4, Val, PrimPrec, Text, TextPoint, Angle, TextHeight, Prefix, Suffix, Callout1, Callout2, TolType, TolMin, TolMax, TolPrec, ArrowSize, ArrowStyle, ArrowDir, WitnessGap, WitnessOvershoot, DualDisplay, DualPrecision)
```

### C#

```csharp
DisplayDimension ICreateLinearDim3(
   ref System.double P0,
   ref System.double P1,
   ref System.double P2,
   ref System.double P3,
   ref System.double P4,
   System.double Val,
   System.int PrimPrec,
   System.string Text,
   ref System.double TextPoint,
   System.double Angle,
   System.double TextHeight,
   System.string Prefix,
   System.string Suffix,
   System.string Callout1,
   System.string Callout2,
   System.int TolType,
   System.string TolMin,
   System.string TolMax,
   System.int TolPrec,
   System.double ArrowSize,
   System.int ArrowStyle,
   System.int ArrowDir,
   System.double WitnessGap,
   System.double WitnessOvershoot,
   System.bool DualDisplay,
   System.int DualPrecision
)
```

### C++/CLI

```cpp
DisplayDimension^ ICreateLinearDim3(
   System.double% P0,
   System.double% P1,
   System.double% P2,
   System.double% P3,
   System.double% P4,
   System.double Val,
   System.int PrimPrec,
   System.String^ Text,
   System.double% TextPoint,
   System.double Angle,
   System.double TextHeight,
   System.String^ Prefix,
   System.String^ Suffix,
   System.String^ Callout1,
   System.String^ Callout2,
   System.int TolType,
   System.String^ TolMin,
   System.String^ TolMax,
   System.int TolPrec,
   System.double ArrowSize,
   System.int ArrowStyle,
   System.int ArrowDir,
   System.double WitnessGap,
   System.double WitnessOvershoot,
   System.bool DualDisplay,
   System.int DualPrecision
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `P0`:
- `P1`:
- `P2`:
- `P3`:
- `P4`:
- `Val`:
- `PrimPrec`:
- `Text`:
- `TextPoint`:
- `Angle`:
- `TextHeight`:
- `Prefix`:
- `Suffix`:
- `Callout1`:
- `Callout2`:
- `TolType`:
- `TolMin`:
- `TolMax`:
- `TolPrec`:
- `ArrowSize`:
- `ArrowStyle`:
- `ArrowDir`:
- `WitnessGap`:
- `WitnessOvershoot`:
- `DualDisplay`:
- `DualPrecision`:

## VBA Syntax

See [DrawingDoc::ICreateLinearDim3](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~ICreateLinearDim3.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)

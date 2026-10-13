---
title: "IAddTrimmingLoop Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "IAddTrimmingLoop"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IAddTrimmingLoop.html"
---

# IAddTrimmingLoop Method (ISurface)

Obsolete. Superseded by [ISurface::IAddTrimmingLoop2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~IAddTrimmingLoop2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub IAddTrimmingLoop( _
   ByVal CurveCount As System.Integer, _
   ByRef Order As System.Integer, _
   ByRef Dim As System.Integer, _
   ByRef Periodic As System.Integer, _
   ByRef NumKnots As System.Integer, _
   ByRef NumCtrlPoints As System.Integer, _
   ByRef Knots As System.Double, _
   ByRef CtrlPointDbls As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim CurveCount As System.Integer
Dim Order As System.Integer
Dim Dim As System.Integer
Dim Periodic As System.Integer
Dim NumKnots As System.Integer
Dim NumCtrlPoints As System.Integer
Dim Knots As System.Double
Dim CtrlPointDbls As System.Double

instance.IAddTrimmingLoop(CurveCount, Order, Dim, Periodic, NumKnots, NumCtrlPoints, Knots, CtrlPointDbls)
```

### C#

```csharp
void IAddTrimmingLoop(
   System.int CurveCount,
   ref System.int Order,
   ref System.int Dim,
   ref System.int Periodic,
   ref System.int NumKnots,
   ref System.int NumCtrlPoints,
   ref System.double Knots,
   ref System.double CtrlPointDbls
)
```

### C++/CLI

```cpp
void IAddTrimmingLoop(
   System.int CurveCount,
   System.int% Order,
   System.int% Dim,
   System.int% Periodic,
   System.int% NumKnots,
   System.int% NumCtrlPoints,
   System.double% Knots,
   System.double% CtrlPointDbls
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CurveCount`:
- `Order`:
- `Dim`:
- `Periodic`:
- `NumKnots`:
- `NumCtrlPoints`:
- `Knots`:
- `CtrlPointDbls`:

## VBA Syntax

See [Surface::IAddTrimmingLoop](ms-its:sldworksapivb6.chm::/sldworks~Surface~IAddTrimmingLoop.html).

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)

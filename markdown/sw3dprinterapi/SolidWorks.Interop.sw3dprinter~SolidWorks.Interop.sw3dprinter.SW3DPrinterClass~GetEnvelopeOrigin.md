---
title: "GetEnvelopeOrigin Method (SW3DPrinterClass)"
project: "SOLIDWORKS 3D Printer API Help"
interface: "SW3DPrinterClass"
member: "GetEnvelopeOrigin"
kind: "method"
source: "sw3dprinterapi/SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.SW3DPrinterClass~GetEnvelopeOrigin.html"
---

# GetEnvelopeOrigin Method (SW3DPrinterClass)

See [ISw3DPrinter](SOLIDWORKS.Interop.sw3dprinter~SOLIDWORKS.Interop.sw3dprinter.ISw3DPrinter.html).

## Syntax

### Visual Basic (Declaration)

```vb
Public Overridable Sub GetEnvelopeOrigin( _
   ByRef X As swBuildEnvelopeStartingPoint_e, _
   ByRef y As swBuildEnvelopeStartingPoint_e, _
   ByRef __MIDL__ISw3DPrinter0000 As swBuildEnvelopeStartingPoint_e _
)
```

### Visual Basic (Usage)

```vb
Dim instance As SW3DPrinterClass
Dim X As swBuildEnvelopeStartingPoint_e
Dim y As swBuildEnvelopeStartingPoint_e
Dim __MIDL__ISw3DPrinter0000 As swBuildEnvelopeStartingPoint_e

instance.GetEnvelopeOrigin(X, y, __MIDL__ISw3DPrinter0000)
```

### C#

```csharp
public virtual void GetEnvelopeOrigin(
   out swBuildEnvelopeStartingPoint_e X,
   out swBuildEnvelopeStartingPoint_e y,
   out swBuildEnvelopeStartingPoint_e __MIDL__ISw3DPrinter0000
)
```

### C++/CLI

```cpp
public:
virtual void GetEnvelopeOrigin(
   [Out] swBuildEnvelopeStartingPoint_e X,
   [Out] swBuildEnvelopeStartingPoint_e y,
   [Out] swBuildEnvelopeStartingPoint_e __MIDL__ISw3DPrinter0000
)
```

### Parameters

- `X`:
- `y`:
- `__MIDL__ISw3DPrinter0000`:

## See Also

[SW3DPrinterClass Class](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.SW3DPrinterClass.html)
[SW3DPrinterClass Members](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.SW3DPrinterClass_members.html)

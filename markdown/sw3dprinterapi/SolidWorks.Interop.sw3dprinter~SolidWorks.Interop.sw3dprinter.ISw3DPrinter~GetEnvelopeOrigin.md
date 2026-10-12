---
title: "GetEnvelopeOrigin Method (ISw3DPrinter)"
project: "SOLIDWORKS 3D Printer API Help"
interface: "ISw3DPrinter"
member: "GetEnvelopeOrigin"
kind: "method"
source: "sw3dprinterapi/SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetEnvelopeOrigin.html"
---

# GetEnvelopeOrigin Method (ISw3DPrinter)

Gets the default starting location for the item to be built in the build envelope, e.g. x-min, y-min, z-min.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetEnvelopeOrigin( _
   ByRef X As swBuildEnvelopeStartingPoint_e, _
   ByRef y As swBuildEnvelopeStartingPoint_e, _
   ByRef __MIDL__ISw3DPrinter0000 As swBuildEnvelopeStartingPoint_e _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISw3DPrinter
Dim X As swBuildEnvelopeStartingPoint_e
Dim y As swBuildEnvelopeStartingPoint_e
Dim __MIDL__ISw3DPrinter0000 As swBuildEnvelopeStartingPoint_e

instance.GetEnvelopeOrigin(X, y, __MIDL__ISw3DPrinter0000)
```

### C#

```csharp
void GetEnvelopeOrigin(
   out swBuildEnvelopeStartingPoint_e X,
   out swBuildEnvelopeStartingPoint_e y,
   out swBuildEnvelopeStartingPoint_e __MIDL__ISw3DPrinter0000
)
```

### C++/CLI

```cpp
void GetEnvelopeOrigin(
   [Out] swBuildEnvelopeStartingPoint_e X,
   [Out] swBuildEnvelopeStartingPoint_e y,
   [Out] swBuildEnvelopeStartingPoint_e __MIDL__ISw3DPrinter0000
)
```

### Parameters

- `X`: x coordinate for starting location as defined in [swBuildEnvelopeStartingPoint_e](SOLIDWORKS.Interop.sw3dprinter~SOLIDWORKS.Interop.sw3dprinter.swBuildEnvelopeStartingPoint_e.html)
- `y`: y coordinate for starting location as defined in [swBuildEnvelopeStartingPoint_e](SOLIDWORKS.Interop.sw3dprinter~SOLIDWORKS.Interop.sw3dprinter.swBuildEnvelopeStartingPoint_e.html)
- `__MIDL__ISw3DPrinter0000`: z coordinate for starting location as defined in [swBuildEnvelopeStartingPoint_e](SOLIDWORKS.Interop.sw3dprinter~SOLIDWORKS.Interop.sw3dprinter.swBuildEnvelopeStartingPoint_e.html)

## VBA Syntax

See [Sw3DPrinter::GetEnvelopeOrigin](ms-its:sw3dprinterapivb6.chm::/sw3dprinter~Sw3DPrinter~GetEnvelopeOrigin.html).

## Remarks

In almost all cases, the printer's driver has set the Z origin to 0.0.

## See Also

[ISw3DPrinter Interface](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter.html)
[ISw3DPrinter Members](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter_members.html)
[ISw3DPrinter::GetBuildEnvelope Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetBuildEnvelope.html)
[ISw3DPrinter::GetDefaultBuildOrientation Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetDefaultBuildOrientation.html)
[ISw3DPrinter::GetDefaultPrintQuality Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetDefaultPrintQuality.html)
[ISw3DPrinter::GetDialogConfiguration Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetDialogConfiguration.html)
[ISw3DPrinter::GetOutputOptions Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetOutputOptions.html)
[ISw3DPrinter::GetPrinterComment Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrinterComment.html)
[ISw3DPrinter::GetPrinterImageBitmap Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrinterImageBitmap.html)
[ISw3DPrinter::GetPrinterLocation Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrinterLocation.html)
[ISw3DPrinter::GetPrinterNames Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrinterNames.html)
[ISw3DPrinter::GetPrinterType Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrinterType.html)
[ISw3DPrinter::OnStartup Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~OnStartup.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0

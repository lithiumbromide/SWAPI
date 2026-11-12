---
title: "GetBuildEnvelope Method (ISw3DPrinter)"
project: "SOLIDWORKS 3D Printer API Help"
interface: "ISw3DPrinter"
member: "GetBuildEnvelope"
kind: "method"
source: "sw3dprinterapi/SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetBuildEnvelope.html"
---

# GetBuildEnvelope Method (ISw3DPrinter)

Gets the dimensions of the printer envelope.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetBuildEnvelope( _
   ByRef xDimension As System.Double, _
   ByRef yDimension As System.Double, _
   ByRef zDimension As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISw3DPrinter
Dim xDimension As System.Double
Dim yDimension As System.Double
Dim zDimension As System.Double

instance.GetBuildEnvelope(xDimension, yDimension, zDimension)
```

### C#

```csharp
void GetBuildEnvelope(
   out System.double xDimension,
   out System.double yDimension,
   out System.double zDimension
)
```

### C++/CLI

```cpp
void GetBuildEnvelope(
   [Out] System.double xDimension,
   [Out] System.double yDimension,
   [Out] System.double zDimension
)
```

### Parameters

- `xDimension`: x dimension
- `yDimension`: y dimension
- `zDimension`: z dimension

## VBA Syntax

See [Sw3DPrinter::GetBuildEnvelope](ms-its:sw3dprinterapivb6.chm::/sw3dprinter~Sw3DPrinter~GetBuildEnvelope.html).

## See Also

[ISw3DPrinter Interface](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter.html)
[ISw3DPrinter Members](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter_members.html)
[ISw3DPrinter::GetEnvelopeOrigin Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetEnvelopeOrigin.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0

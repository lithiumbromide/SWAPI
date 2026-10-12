---
title: "GetBuildEnvelope Method (SW3DPrinterClass)"
project: "SOLIDWORKS 3D Printer API Help"
interface: "SW3DPrinterClass"
member: "GetBuildEnvelope"
kind: "method"
source: "sw3dprinterapi/SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.SW3DPrinterClass~GetBuildEnvelope.html"
---

# GetBuildEnvelope Method (SW3DPrinterClass)

See [ISw3DPrinter](SOLIDWORKS.Interop.sw3dprinter~SOLIDWORKS.Interop.sw3dprinter.ISw3DPrinter.html).

## Syntax

### Visual Basic (Declaration)

```vb
Public Overridable Sub GetBuildEnvelope( _
   ByRef xDimension As System.Double, _
   ByRef yDimension As System.Double, _
   ByRef zDimension As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As SW3DPrinterClass
Dim xDimension As System.Double
Dim yDimension As System.Double
Dim zDimension As System.Double

instance.GetBuildEnvelope(xDimension, yDimension, zDimension)
```

### C#

```csharp
public virtual void GetBuildEnvelope(
   out System.double xDimension,
   out System.double yDimension,
   out System.double zDimension
)
```

### C++/CLI

```cpp
public:
virtual void GetBuildEnvelope(
   [Out] System.double xDimension,
   [Out] System.double yDimension,
   [Out] System.double zDimension
)
```

### Parameters

- `xDimension`:
- `yDimension`:
- `zDimension`:

## See Also

[SW3DPrinterClass Class](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.SW3DPrinterClass.html)
[SW3DPrinterClass Members](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.SW3DPrinterClass_members.html)

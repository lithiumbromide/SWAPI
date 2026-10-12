---
title: "GetScaleParametersForActiveDocument Method (SW3DPrinterClass)"
project: "SOLIDWORKS 3D Printer API Help"
interface: "SW3DPrinterClass"
member: "GetScaleParametersForActiveDocument"
kind: "method"
source: "sw3dprinterapi/SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.SW3DPrinterClass~GetScaleParametersForActiveDocument.html"
---

# GetScaleParametersForActiveDocument Method (SW3DPrinterClass)

See [ISw3DPrinter](SOLIDWORKS.Interop.sw3dprinter~SOLIDWORKS.Interop.sw3dprinter.ISw3DPrinter.html).

## Syntax

### Visual Basic (Declaration)

```vb
Public Overridable Sub GetScaleParametersForActiveDocument( _
   ByRef minimumScale As System.Integer, _
   ByRef maximumScale As System.Integer, _
   ByRef scaleIncrement As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As SW3DPrinterClass
Dim minimumScale As System.Integer
Dim maximumScale As System.Integer
Dim scaleIncrement As System.Integer

instance.GetScaleParametersForActiveDocument(minimumScale, maximumScale, scaleIncrement)
```

### C#

```csharp
public virtual void GetScaleParametersForActiveDocument(
   out System.int minimumScale,
   out System.int maximumScale,
   out System.int scaleIncrement
)
```

### C++/CLI

```cpp
public:
virtual void GetScaleParametersForActiveDocument(
   [Out] System.int minimumScale,
   [Out] System.int maximumScale,
   [Out] System.int scaleIncrement
)
```

### Parameters

- `minimumScale`:
- `maximumScale`:
- `scaleIncrement`:

## See Also

[SW3DPrinterClass Class](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.SW3DPrinterClass.html)
[SW3DPrinterClass Members](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.SW3DPrinterClass_members.html)

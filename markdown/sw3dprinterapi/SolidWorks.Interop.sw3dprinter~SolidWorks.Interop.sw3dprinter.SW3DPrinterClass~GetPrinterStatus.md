---
title: "GetPrinterStatus Method (SW3DPrinterClass)"
project: "SOLIDWORKS 3D Printer API Help"
interface: "SW3DPrinterClass"
member: "GetPrinterStatus"
kind: "method"
source: "sw3dprinterapi/SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.SW3DPrinterClass~GetPrinterStatus.html"
---

# GetPrinterStatus Method (SW3DPrinterClass)

See [ISw3DPrinter](SOLIDWORKS.Interop.sw3dprinter~SOLIDWORKS.Interop.sw3dprinter.ISw3DPrinter.html).

## Syntax

### Visual Basic (Declaration)

```vb
Public Overridable Function GetPrinterStatus( _
   ByRef StatusMessage As System.String _
) As swPrinterStatus_e
```

### Visual Basic (Usage)

```vb
Dim instance As SW3DPrinterClass
Dim StatusMessage As System.String
Dim value As swPrinterStatus_e

value = instance.GetPrinterStatus(StatusMessage)
```

### C#

```csharp
public virtual swPrinterStatus_e GetPrinterStatus(
   out System.string StatusMessage
)
```

### C++/CLI

```cpp
public:
virtual swPrinterStatus_e GetPrinterStatus(
   [Out] System.String^ StatusMessage
)
```

### Parameters

- `StatusMessage`:

## See Also

[SW3DPrinterClass Class](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.SW3DPrinterClass.html)
[SW3DPrinterClass Members](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.SW3DPrinterClass_members.html)

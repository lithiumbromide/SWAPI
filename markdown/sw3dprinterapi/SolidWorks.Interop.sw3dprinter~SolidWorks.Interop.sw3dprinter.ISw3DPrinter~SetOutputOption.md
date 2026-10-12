---
title: "SetOutputOption Method (ISw3DPrinter)"
project: "SOLIDWORKS 3D Printer API Help"
interface: "ISw3DPrinter"
member: "SetOutputOption"
kind: "method"
source: "sw3dprinterapi/SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~SetOutputOption.html"
---

# SetOutputOption Method (ISw3DPrinter)

Called when a user specifies how to create the rapid prototype by making a selection in the **Output** box on the 3D Printer tab.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetOutputOption( _
   ByVal OutputOption As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISw3DPrinter
Dim OutputOption As System.String

instance.SetOutputOption(OutputOption)
```

### C#

```csharp
void SetOutputOption(
   System.string OutputOption
)
```

### C++/CLI

```cpp
void SetOutputOption(
   System.String^ OutputOption
)
```

### Parameters

- `OutputOption`: Selection that specifies how to create the rapid prototype

## VBA Syntax

See [Sw3DPrinter::SetOutputOption](ms-its:sw3dprinterapivb6.chm::/sw3dprinter~Sw3DPrinter~SetOutputOption.html).

## See Also

[ISw3DPrinter Interface](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter.html)
[ISw3DPrinter Members](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter_members.html)
[ISw3DPrinter::GetOutputOption Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetOutputOption.html)
[ISw3DPrinter::GetOutputOptions Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetOutputOptions.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0

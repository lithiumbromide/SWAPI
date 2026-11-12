---
title: "SetQuantity Method (ISw3DPrinter)"
project: "SOLIDWORKS 3D Printer API Help"
interface: "ISw3DPrinter"
member: "SetQuantity"
kind: "method"
source: "sw3dprinterapi/SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~SetQuantity.html"
---

# SetQuantity Method (ISw3DPrinter)

Called when a user sets the number of copies to print in the **Number** of copies box on the 3D Printer tab.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetQuantity( _
   ByVal Quantity As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISw3DPrinter
Dim Quantity As System.Integer

instance.SetQuantity(Quantity)
```

### C#

```csharp
void SetQuantity(
   System.int Quantity
)
```

### C++/CLI

```cpp
void SetQuantity(
   System.int Quantity
)
```

### Parameters

- `Quantity`: Number of copies to print

## VBA Syntax

See [Sw3DPrinter::SetQuantity](ms-its:sw3dprinterapivb6.chm::/sw3dprinter~Sw3DPrinter~SetQuantity.html).

## Remarks

This method is called in reaction to the user changing the number of copies to print in the Print dialog. You must write the code for this method to do anything useful.

## See Also

[ISw3DPrinter Interface](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter.html)
[ISw3DPrinter Members](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter_members.html)
[ISw3DPrinter::GetQuantity Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetQuantity.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0

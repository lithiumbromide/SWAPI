---
title: "GetCalculatedCost Method (ISw3DPrinter)"
project: "SOLIDWORKS 3D Printer API Help"
interface: "ISw3DPrinter"
member: "GetCalculatedCost"
kind: "method"
source: "sw3dprinterapi/SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetCalculatedCost.html"
---

# GetCalculatedCost Method (ISw3DPrinter)

Gets the calculated cost in vendor-defined units, e.g., dollars, euros, liters of material, etc.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCalculatedCost() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISw3DPrinter
Dim value As System.String

value = instance.GetCalculatedCost()
```

### C#

```csharp
System.string GetCalculatedCost()
```

### C++/CLI

```cpp
System.String^ GetCalculatedCost();
```

### Return Value

Calculated cost in vendor-defined units

## VBA Syntax

See [Sw3DPrinter::GetCalculatedCost](ms-its:sw3dprinterapivb6.chm::/sw3dprinter~Sw3DPrinter~GetCalculatedCost.html).

## See Also

[ISw3DPrinter Interface](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter.html)
[ISw3DPrinter Members](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter_members.html)
[ISw3DPrinter::GetCalculatedBoundingVolume Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetCalculatedBoundingVolume.html)
[ISw3DPrinter::GetCalculatedBuildTime Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetCalculatedBuildTime.html)
[ISw3DPrinter::GetCalculatedSurfaceArea Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetCalculatedSurfaceArea.html)
[ISw3DPrinter::GetCalculatedVolume Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetCalculatedVolume.html)
[ISw3DPrinter::OnUpdateStatistics Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~OnUpdateStatistics.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0

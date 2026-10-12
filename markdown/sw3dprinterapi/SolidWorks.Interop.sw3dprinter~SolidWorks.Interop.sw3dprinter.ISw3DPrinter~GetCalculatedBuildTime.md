---
title: "GetCalculatedBuildTime Method (ISw3DPrinter)"
project: "SOLIDWORKS 3D Printer API Help"
interface: "ISw3DPrinter"
member: "GetCalculatedBuildTime"
kind: "method"
source: "sw3dprinterapi/SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetCalculatedBuildTime.html"
---

# GetCalculatedBuildTime Method (ISw3DPrinter)

Gets the estimated time in minutes to build the current document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCalculatedBuildTime() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISw3DPrinter
Dim value As System.String

value = instance.GetCalculatedBuildTime()
```

### C#

```csharp
System.string GetCalculatedBuildTime()
```

### C++/CLI

```cpp
System.String^ GetCalculatedBuildTime();
```

### Return Value

Estimated build time in minutes

## VBA Syntax

See [Sw3DPrinter::GetCalculatedBuildTime](ms-its:sw3dprinterapivb6.chm::/sw3dprinter~Sw3DPrinter~GetCalculatedBuildTime.html).

## See Also

[ISw3DPrinter Interface](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter.html)
[ISw3DPrinter Members](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter_members.html)
[ISw3DPrinter::GetCalculatedBoundingVolume Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetCalculatedBoundingVolume.html)
[ISw3DPrinter::GetCalculatedCost Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetCalculatedCost.html)
[ISw3DPrinter::GetCalculatedSurfaceArea Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetCalculatedSurfaceArea.html)
[ISw3DPrinter::GetCalculatedVolume Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetCalculatedVolume.html)
[ISw3DPrinter::OnUpdateStatistics Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~OnUpdateStatistics.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0

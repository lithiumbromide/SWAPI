---
title: "HeatFluxBeginEdit Method (ICWHeatFlux)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWHeatFlux"
member: "HeatFluxBeginEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~HeatFluxBeginEdit.html"
---

# HeatFluxBeginEdit Method (ICWHeatFlux)

Starts editing heat flux.

## Syntax

### Visual Basic (Declaration)

```vb
Sub HeatFluxBeginEdit()
```

### Visual Basic (Usage)

```vb
Dim instance As ICWHeatFlux

instance.HeatFluxBeginEdit()
```

### C#

```csharp
void HeatFluxBeginEdit()
```

### C++/CLI

```cpp
void HeatFluxBeginEdit();
```

## VBA Syntax

See [CWHeatFlux::HeatFluxBeginEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWHeatFlux~HeatFluxBeginEdit.html).

## Examples

See the [ICWHeatFlux](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux.html) examples.

## Remarks

To start editing heat flux, you must call this method. You must call [ICWHeatFlux::HeatFluxEndEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWHeatFlux~HeatFluxEndEdit.html) to end editing heat flux. Changes are not applied unless you call both methods.

## See Also

[ICWHeatFlux Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux.html)
[ICWHeatFlux Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0

---
title: "HeatFluxEndEdit Method (ICWHeatFlux)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWHeatFlux"
member: "HeatFluxEndEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~HeatFluxEndEdit.html"
---

# HeatFluxEndEdit Method (ICWHeatFlux)

Ends editing heat flux.

## Syntax

### Visual Basic (Declaration)

```vb
Function HeatFluxEndEdit() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWHeatFlux
Dim value As System.Integer

value = instance.HeatFluxEndEdit()
```

### C#

```csharp
System.int HeatFluxEndEdit()
```

### C++/CLI

```cpp
System.int HeatFluxEndEdit();
```

### Return Value

Error as defined in [swsHeatFluxEndEditError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsHeatFluxEndEditError_e.html)

## VBA Syntax

See [CWHeatFlux::HeatFluxEndEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWHeatFlux~HeatFluxEndEdit.html).

## Examples

See the [ICWHeatFlux](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux.html) examples.

## Remarks

You must call [ICWHeatFlux::HeatFluxBeginEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWHeatFlux~HeatFluxBeginEdit.html) to start editing heat flux. To end editing heat flux, you must call this method. Changes are not applied unless you call both methods.

## See Also

[ICWHeatFlux Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux.html)
[ICWHeatFlux Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0

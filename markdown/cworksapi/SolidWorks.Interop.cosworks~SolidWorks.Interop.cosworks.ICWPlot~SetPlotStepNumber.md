---
title: "SetPlotStepNumber Method (ICWPlot)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPlot"
member: "SetPlotStepNumber"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot~SetPlotStepNumber.html"
---

# SetPlotStepNumber Method (ICWPlot)

Sets the number of the solution step to plot.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetPlotStepNumber( _
   ByVal NStepNumber As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPlot
Dim NStepNumber As System.Integer
Dim value As System.Integer

value = instance.SetPlotStepNumber(NStepNumber)
```

### C#

```csharp
System.int SetPlotStepNumber(
   System.int NStepNumber
)
```

### C++/CLI

```cpp
System.int SetPlotStepNumber(
   System.int NStepNumber
)
```

### Parameters

- `NStepNumber`: Number of solution step to plot

### Return Value

Error code as defined in [swsResultPlotErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsResultPlotErrorCode_e.html)

## VBA Syntax

See [CWPlot::SetPlotStepNumber](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPlot~SetPlotStepNumber.html).

## Examples

[Create Nonlinear Dynamic Plots (VBA)](Create_Nonlinear_Dynamic_Plots_Example_VB.htm)
[Create Nonlinear Dynamic Plots (VB.NET)](Create_Nonlinear_Dynamic_Plots_Example_VBNET.htm)
[Create Nonlinear Dynamic Plots (C#)](Create_Nonlinear_Dynamic_Plots_Example_CSharp.htm)

## Remarks

This method is valid only for the following plots:

- Acceleration
- Displacement
- Strain
- Stress
- Transient thermal
- Velocity

## See Also

[ICWPlot Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot.html)
[ICWPlot Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot_members.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0

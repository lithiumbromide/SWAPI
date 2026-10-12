---
title: "SetModeShape Method (ICWPlot)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPlot"
member: "SetModeShape"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot~SetModeShape.html"
---

# SetModeShape Method (ICWPlot)

Sets the mode shape number for this amplitude or displacement plot.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetModeShape( _
   ByVal NModeShape As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPlot
Dim NModeShape As System.Integer
Dim value As System.Integer

value = instance.SetModeShape(NModeShape)
```

### C#

```csharp
System.int SetModeShape(
   System.int NModeShape
)
```

### C++/CLI

```cpp
System.int SetModeShape(
   System.int NModeShape
)
```

### Parameters

- `NModeShape`: Mode shape number for which amplitudes or displacements are plotted

### Return Value

Error code as defined in [swsResultPlotErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsResultPlotErrorCode_e.html)

## VBA Syntax

See [CWPlot::SetModeShape](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPlot~SetModeShape.html).

## Examples

[Create Amplitude Plot and Set Mode Shape (VBA)](Create_Amplitude_Plot_Example_VB.htm)
[Create Amplitude Plot and Set Mode Shape (VB.NET)](Create_Amplitude_Plot_Example_VBNET.htm)
[Create Amplitude Plot and Set Mode Shape (C#)](Create_Amplitude_Plot_Example_CSharp.htm)

## See Also

[ICWPlot Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot.html)
[ICWPlot Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot_members.html)
[ICWPlot::SetNormalizeModeShape Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot~SetNormalizeModeShape.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0

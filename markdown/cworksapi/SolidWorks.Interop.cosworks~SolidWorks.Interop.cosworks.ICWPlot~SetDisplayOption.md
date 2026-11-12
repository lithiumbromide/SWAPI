---
title: "SetDisplayOption Method (ICWPlot)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPlot"
member: "SetDisplayOption"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot~SetDisplayOption.html"
---

# SetDisplayOption Method (ICWPlot)

Sets the display option for this stress results plot of a mixed mesh model.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetDisplayOption( _
   ByVal NDisplayOption As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPlot
Dim NDisplayOption As System.Integer
Dim value As System.Integer

value = instance.SetDisplayOption(NDisplayOption)
```

### C#

```csharp
System.int SetDisplayOption(
   System.int NDisplayOption
)
```

### C++/CLI

```cpp
System.int SetDisplayOption(
   System.int NDisplayOption
)
```

### Parameters

- `NDisplayOption`: Display option as defined in [swsDisplayOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsDisplayOption_e.html)

### Return Value

Error code as defined in [swsResultPlotErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsResultPlotErrorCode_e.html)

## VBA Syntax

See [CWPlot::SetDisplayOption](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPlot~SetDisplayOption.html).

## Remarks

This method is valid only for stress plots of mixed mesh models having beams and solids/shells. At least one joint group must be present in the study.

## See Also

[ICWPlot Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot.html)
[ICWPlot Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0

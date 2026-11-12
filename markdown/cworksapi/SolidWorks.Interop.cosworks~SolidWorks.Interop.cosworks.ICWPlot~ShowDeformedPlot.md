---
title: "ShowDeformedPlot Method (ICWPlot)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPlot"
member: "ShowDeformedPlot"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot~ShowDeformedPlot.html"
---

# ShowDeformedPlot Method (ICWPlot)

Sets whether and how to plot on the deformed shape of the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function ShowDeformedPlot( _
   ByVal BShowDeformed As System.Boolean, _
   ByVal NDeformOption As System.Integer, _
   ByVal DUserDefValue As System.Double, _
   ByVal BShowColors As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPlot
Dim BShowDeformed As System.Boolean
Dim NDeformOption As System.Integer
Dim DUserDefValue As System.Double
Dim BShowColors As System.Boolean
Dim value As System.Integer

value = instance.ShowDeformedPlot(BShowDeformed, NDeformOption, DUserDefValue, BShowColors)
```

### C#

```csharp
System.int ShowDeformedPlot(
   System.bool BShowDeformed,
   System.int NDeformOption,
   System.double DUserDefValue,
   System.bool BShowColors
)
```

### C++/CLI

```cpp
System.int ShowDeformedPlot(
   System.bool BShowDeformed,
   System.int NDeformOption,
   System.double DUserDefValue,
   System.bool BShowColors
)
```

### Parameters

- `BShowDeformed`: True to plot on the deformed shape, false to not
- `NDeformOption`: Deformed shape option as defined in [swsDeformType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsDeformType_e.html)
- `DUserDefValue`: User-defined scale factor; valid only if NDeformOption is swsDeformType_e.swsUserDefined
- `BShowColors`: True to show colors, false to not

### Return Value

Error code as defined in [swsResultPlotErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsResultPlotErrorCode_e.html)

## VBA Syntax

See [CWPlot::ShowDeformedPlot](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPlot~ShowDeformedPlot.html).

## Examples

See the [ICWPlot](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot.html) examples.

## Remarks

This method is valid for the following plots:

- Acceleration
- Displacement
- Mode shape/amplitude
- Strain
- Strain energy density
- Stress
- Vector

## See Also

[ICWPlot Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot.html)
[ICWPlot Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot_members.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0

---
title: "SetComponentUnitAndValueByElem Method (ICWPlot)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPlot"
member: "SetComponentUnitAndValueByElem"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot~SetComponentUnitAndValueByElem.html"
---

# SetComponentUnitAndValueByElem Method (ICWPlot)

Sets the component, units, and values to plot.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetComponentUnitAndValueByElem( _
   ByVal NComponent As System.Integer, _
   ByVal NUnits As System.Integer, _
   ByVal BValueByElem As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPlot
Dim NComponent As System.Integer
Dim NUnits As System.Integer
Dim BValueByElem As System.Boolean
Dim value As System.Integer

value = instance.SetComponentUnitAndValueByElem(NComponent, NUnits, BValueByElem)
```

### C#

```csharp
System.int SetComponentUnitAndValueByElem(
   System.int NComponent,
   System.int NUnits,
   System.bool BValueByElem
)
```

### C++/CLI

```cpp
System.int SetComponentUnitAndValueByElem(
   System.int NComponent,
   System.int NUnits,
   System.bool BValueByElem
)
```

### Parameters

- `NComponent`: Component to plot (see **Remarks**)
- `NUnits`: Units as appropriate for NComponent (see **Remarks**)
- `BValueByElem`: True to plot element values, false to plot node values

### Return Value

Error code as defined by [swsResultPlotErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsResultPlotErrorCode_e.html)

## VBA Syntax

See [CWPlot::SetComponentUnitAndValueByElem](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPlot~SetComponentUnitAndValueByElem.html).

## Examples

See the [ICWPlot](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot.html) examples.

## Remarks

| If this plot's result type is swsPlotResultTypes_e... | Then NComponent contains the component to plot as defined by... | And NUnits contains the units as defined by... |
| --- | --- | --- |
| swsResultAcceleration | swsAccelerationComponent_e | swsAccelerationUnit_e |
| swsResultBeamDiagram | swsBeamForceType_e | swsForceUnit_e |
| swsResultBeamStress | swsBeamStressType_e | swsStrengthUnit_e |
| swsResultDesignInsight | N/A | N/A |
| swsResultDisplacementOrAmplitude | swsDisplacementComponent_e (Displacement) swsFrequencyBucklingResultDisplacementComponentTypes_e (Amplitude for frequency and buckling) | swsLinearUnit_e (displacement) or swsForceUnit_e (reaction force) |
| swsResultEdgeWeldConnector | N/A | N/A |
| swsResultFactorOfSafety | swsFOS_NonCompositeCriterion_e (Non-composite shells) swsFOS_CompositeCriterion_e (Composite shells) | N/A |
| swsResultFatigue | swsFatigueComponent_e | N/A |
| swsResultPinBoltBearing | N/A | N/A |
| swsResultStrain | swsStrainComponent_e | swsStrengthUnit_e |
| swsResultStress | swsStressComponent_e | swsStrengthUnit_e |
| swsResultThermal | swsThermalComponent_e | swsTemperatureUnit_e |
| swsResultVelocity | swsVelocityComponent_e | swsVelocityUnit_e |

## See Also

[ICWPlot Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot.html)
[ICWPlot Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot_members.html)
[ICWResults::CreatePlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreatePlot.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0

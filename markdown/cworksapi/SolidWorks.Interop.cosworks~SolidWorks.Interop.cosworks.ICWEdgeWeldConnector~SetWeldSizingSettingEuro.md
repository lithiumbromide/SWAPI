---
title: "SetWeldSizingSettingEuro Method (ICWEdgeWeldConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWEdgeWeldConnector"
member: "SetWeldSizingSettingEuro"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~SetWeldSizingSettingEuro.html"
---

# SetWeldSizingSettingEuro Method (ICWEdgeWeldConnector)

Sets the European Standard settings for weld sizing calculations.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetWeldSizingSettingEuro( _
   ByVal NWeakMaterial As System.Integer, _
   ByVal DUltimateTensileStrength As System.Double, _
   ByVal NTensileStrengthUnit As System.Integer, _
   ByVal DCorrelationFactor As System.Double, _
   ByVal DPartialSafetyFactor As System.Double, _
   ByVal BIsEstimatedWeldSize As System.Boolean, _
   ByVal DEstimatedWeldSize As System.Double, _
   ByVal NEstimatedWeldSizeUnit As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWEdgeWeldConnector
Dim NWeakMaterial As System.Integer
Dim DUltimateTensileStrength As System.Double
Dim NTensileStrengthUnit As System.Integer
Dim DCorrelationFactor As System.Double
Dim DPartialSafetyFactor As System.Double
Dim BIsEstimatedWeldSize As System.Boolean
Dim DEstimatedWeldSize As System.Double
Dim NEstimatedWeldSizeUnit As System.Integer
Dim value As System.Integer

value = instance.SetWeldSizingSettingEuro(NWeakMaterial, DUltimateTensileStrength, NTensileStrengthUnit, DCorrelationFactor, DPartialSafetyFactor, BIsEstimatedWeldSize, DEstimatedWeldSize, NEstimatedWeldSizeUnit)
```

### C#

```csharp
System.int SetWeldSizingSettingEuro(
   System.int NWeakMaterial,
   System.double DUltimateTensileStrength,
   System.int NTensileStrengthUnit,
   System.double DCorrelationFactor,
   System.double DPartialSafetyFactor,
   System.bool BIsEstimatedWeldSize,
   System.double DEstimatedWeldSize,
   System.int NEstimatedWeldSizeUnit
)
```

### C++/CLI

```cpp
System.int SetWeldSizingSettingEuro(
   System.int NWeakMaterial,
   System.double DUltimateTensileStrength,
   System.int NTensileStrengthUnit,
   System.double DCorrelationFactor,
   System.double DPartialSafetyFactor,
   System.bool BIsEstimatedWeldSize,
   System.double DEstimatedWeldSize,
   System.int NEstimatedWeldSizeUnit
)
```

### Parameters

- `NWeakMaterial`: Material of weaker joined part as defined in [swsWeakMaterial_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsWeakMaterial_e.html)
- `DUltimateTensileStrength`: Ultimate tensile strength of NWeakMaterial
- `NTensileStrengthUnit`: DUltimateTensileStrength units as defined in [swsWeldStrengthUnits_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsWeldStrengthUnits_e.html)
- `DCorrelationFactor`: 0.8 <= correlation factor for weld calculations <= 1.0
- `DPartialSafetyFactor`: 1.0 <= partial safety factor for joints <= 1.25
- `BIsEstimatedWeldSize`: True to calculate the appropriate size for the weld connector and compare it to DEstimatedWeldSize in the Weld Check Plot; false to just use DEstimatedWeldSize
- `DEstimatedWeldSize`: Estimated weld size
- `NEstimatedWeldSizeUnit`: DEstimatedWeldSize units as defined in [swsEstimatedWeldSizeUnits_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsEstimatedWeldSizeUnits_e.html)

### Return Value

Error code as defined in [swsWeldResultErrorCode_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsWeldResultErrorCode_e.html)

## VBA Syntax

See [CWEdgeWeldConnector::SetWeldSizingSettingEuro](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWEdgeWeldConnector~SetWeldSizingSettingEuro.html).

## Examples

See the [ICWEdgeWeldConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector.html) examples.

## Remarks

This method is valid only if [ICWEdgeWeldConnector::GetCodeType](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWEdgeWeldConnector~GetCodeType.html) returns [swsEdgeWeldSolverCode_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsEdgeWeldSolverCode_e.html).swsEdgeWeldSolverCodeEURO.

## See Also

[ICWEdgeWeldConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector.html)
[ICWEdgeWeldConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector_members.html)
[ICWEdgeWeldConnector::GetWeldSizingSettingEuro Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~GetWeldSizingSettingEuro.html)
[ICWEdgeWeldConnector::SetWeldSizingSettingUS Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~SetWeldSizingSettingUS.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0

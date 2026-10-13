---
title: "SetWeldSizingSettingUS Method (ICWEdgeWeldConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWEdgeWeldConnector"
member: "SetWeldSizingSettingUS"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~SetWeldSizingSettingUS.html"
---

# SetWeldSizingSettingUS Method (ICWEdgeWeldConnector)

Sets the American Standard settings for weld sizing calculations.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetWeldSizingSettingUS( _
   ByVal NElectrodeMaterial As System.Integer, _
   ByVal DWeldStrength As System.Double, _
   ByVal NWeldStrengthUnit As System.Integer, _
   ByVal NSafetyFactorLiftOption As System.Integer, _
   ByVal DSafetyFactor As System.Double, _
   ByVal BIsEstimatedWeldSize As System.Boolean, _
   ByVal DEstimatedWeldSize As System.Double, _
   ByVal NEstimatedWeldSizeUnit As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWEdgeWeldConnector
Dim NElectrodeMaterial As System.Integer
Dim DWeldStrength As System.Double
Dim NWeldStrengthUnit As System.Integer
Dim NSafetyFactorLiftOption As System.Integer
Dim DSafetyFactor As System.Double
Dim BIsEstimatedWeldSize As System.Boolean
Dim DEstimatedWeldSize As System.Double
Dim NEstimatedWeldSizeUnit As System.Integer
Dim value As System.Integer

value = instance.SetWeldSizingSettingUS(NElectrodeMaterial, DWeldStrength, NWeldStrengthUnit, NSafetyFactorLiftOption, DSafetyFactor, BIsEstimatedWeldSize, DEstimatedWeldSize, NEstimatedWeldSizeUnit)
```

### C#

```csharp
System.int SetWeldSizingSettingUS(
   System.int NElectrodeMaterial,
   System.double DWeldStrength,
   System.int NWeldStrengthUnit,
   System.int NSafetyFactorLiftOption,
   System.double DSafetyFactor,
   System.bool BIsEstimatedWeldSize,
   System.double DEstimatedWeldSize,
   System.int NEstimatedWeldSizeUnit
)
```

### C++/CLI

```cpp
System.int SetWeldSizingSettingUS(
   System.int NElectrodeMaterial,
   System.double DWeldStrength,
   System.int NWeldStrengthUnit,
   System.int NSafetyFactorLiftOption,
   System.double DSafetyFactor,
   System.bool BIsEstimatedWeldSize,
   System.double DEstimatedWeldSize,
   System.int NEstimatedWeldSizeUnit
)
```

### Parameters

- `NElectrodeMaterial`: Electrode material as defined in [swsElectrodeMaterialTypes_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsElectrodeMaterialTypes_e.html)
- `DWeldStrength`: Ultimate shear strength of NElectrodeMaterial; if NElectrodeMaterial is swsElectrodeMaterialTypes_e.swsElectrodeMaterialCustomAl or swsElectrodeMaterialTypes_e.swsElectrodeMaterialCustomSteel, ultimate shear strength for the weld throat
- `NWeldStrengthUnit`: DWeldStrength units as defined in [swsWeldStrengthUnits_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsWeldStrengthUnits_e.html)
- `NSafetyFactorLiftOption`: Lift safety factor by which to reduce DWeldStrength as defined in [swsEdgeWeldConnectorSafetyFactorLiftOption_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsEdgeWeldConnectorSafetyFactorLiftOption_e.html)
- `DSafetyFactor`: Custom safety factor by which to reduce DWeldStrength; overrides the lift safety factor specified in NSafetyFactorLiftOption
- `BIsEstimatedWeldSize`: True to calculate the appropriate size for the weld connector and compare it to DEstimatedWeldSize in the Weld Check Plot; false to just use DEstimatedWeldSize
- `DEstimatedWeldSize`: Estimated weld size
- `NEstimatedWeldSizeUnit`: DEstimatedWeldSize units as defined in [swsEstimatedWeldSizeUnits_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsEstimatedWeldSizeUnits_e.html)

### Return Value

Error code as defined in [swsWeldResultErrorCode_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsWeldResultErrorCode_e.html)

## VBA Syntax

See [CWEdgeWeldConnector::SetWeldSizingSettingUS](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWEdgeWeldConnector~SetWeldSizingSettingUS.html).

## Examples

See the [ICWEdgeWeldConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector.html) examples.

## Remarks

This method is valid only if [ICWEdgeWeldConnector::GetCodeType](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWEdgeWeldConnector~GetCodeType.html) returns [swsEdgeWeldSolverCode_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsEdgeWeldSolverCode_e.html).swsEdgeWeldSolverCodeAWS.

## See Also

[ICWEdgeWeldConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector.html)
[ICWEdgeWeldConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector_members.html)
[ICWEdgeWeldConnector::GetWeldSizingSettingUS Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~GetWeldSizingSettingUS.html)
[ICWEdgeWeldConnector::SetWeldSizingSettingEuro Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~SetWeldSizingSettingEuro.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0

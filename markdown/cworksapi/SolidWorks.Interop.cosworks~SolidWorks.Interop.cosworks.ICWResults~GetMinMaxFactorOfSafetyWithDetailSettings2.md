---
title: "GetMinMaxFactorOfSafetyWithDetailSettings2 Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetMinMaxFactorOfSafetyWithDetailSettings2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxFactorOfSafetyWithDetailSettings2.html"
---

# GetMinMaxFactorOfSafetyWithDetailSettings2 Method (ICWResults)

Gets the algebraic minimum and maximum factors of safety (FOS) for non-composite shells and the specified detail settings.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMinMaxFactorOfSafetyWithDetailSettings2( _
   ByVal BAllBodies As System.Boolean, _
   ByVal ArraySelectedEntities As System.Object, _
   ByVal NComponent As System.Integer, _
   ByVal BUpperLimit As System.Boolean, _
   ByVal DUpperValue As System.Double, _
   ByVal NStressUnit As System.Integer, _
   ByVal NStressLimitOption As System.Integer, _
   ByVal DStressValue As System.Double, _
   ByVal NCompressiveStressLimitOption As System.Integer, _
   ByVal DCompressiveStressValue As System.Double, _
   ByVal DMultiplicationFactor As System.Double, _
   ByVal DCompressiveStressMultiplicationFactor As System.Double, _
   ByVal BCombinedStressOnBeams As System.Boolean, _
   ByVal NShellOptions As System.Integer, _
   ByVal NStepNumber As System.Integer, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim BAllBodies As System.Boolean
Dim ArraySelectedEntities As System.Object
Dim NComponent As System.Integer
Dim BUpperLimit As System.Boolean
Dim DUpperValue As System.Double
Dim NStressUnit As System.Integer
Dim NStressLimitOption As System.Integer
Dim DStressValue As System.Double
Dim NCompressiveStressLimitOption As System.Integer
Dim DCompressiveStressValue As System.Double
Dim DMultiplicationFactor As System.Double
Dim DCompressiveStressMultiplicationFactor As System.Double
Dim BCombinedStressOnBeams As System.Boolean
Dim NShellOptions As System.Integer
Dim NStepNumber As System.Integer
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetMinMaxFactorOfSafetyWithDetailSettings2(BAllBodies, ArraySelectedEntities, NComponent, BUpperLimit, DUpperValue, NStressUnit, NStressLimitOption, DStressValue, NCompressiveStressLimitOption, DCompressiveStressValue, DMultiplicationFactor, DCompressiveStressMultiplicationFactor, BCombinedStressOnBeams, NShellOptions, NStepNumber, ErrorCode)
```

### C#

```csharp
System.object GetMinMaxFactorOfSafetyWithDetailSettings2(
   System.bool BAllBodies,
   System.object ArraySelectedEntities,
   System.int NComponent,
   System.bool BUpperLimit,
   System.double DUpperValue,
   System.int NStressUnit,
   System.int NStressLimitOption,
   System.double DStressValue,
   System.int NCompressiveStressLimitOption,
   System.double DCompressiveStressValue,
   System.double DMultiplicationFactor,
   System.double DCompressiveStressMultiplicationFactor,
   System.bool BCombinedStressOnBeams,
   System.int NShellOptions,
   System.int NStepNumber,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetMinMaxFactorOfSafetyWithDetailSettings2(
   System.bool BAllBodies,
   System.Object^ ArraySelectedEntities,
   System.int NComponent,
   System.bool BUpperLimit,
   System.double DUpperValue,
   System.int NStressUnit,
   System.int NStressLimitOption,
   System.double DStressValue,
   System.int NCompressiveStressLimitOption,
   System.double DCompressiveStressValue,
   System.double DMultiplicationFactor,
   System.double DCompressiveStressMultiplicationFactor,
   System.bool BCombinedStressOnBeams,
   System.int NShellOptions,
   System.int NStepNumber,
   [Out] System.int ErrorCode
)
```

### Parameters

- `BAllBodies`: True to use all bodies to plot the factor of safety, false to use specific bodies
- `ArraySelectedEntities`: Array of bodies for which to plot the factor of safety; valid only if BAllBodies is set to false
- `NComponent`: Failure criterion as defined by [swsFOS_NonCompositeCriterion_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFOS_NonCompositeCriterion_e.html) (see **Remarks**)
- `BUpperLimit`: True to set an upper limit, false to not
- `DUpperValue`: Upper limit; valid only if BUpperLimit is true
- `NStressUnit`: Units of stress as defined in [swsStrengthUnit_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsStrengthUnit_e.html)
- `NStressLimitOption`: Limit stress types as defined in [swsFactorOfSafetyStressLimitOption_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFactorOfSafetyStressLimitOption_e.html) (see **Remarks**)
- `DStressValue`: Stress value; valid only if NStressLimitOption is swsFactorOfSafetyStressLimitOption_e.swsFactorOfSafetyStressLimitOption_UserDefined
- `NCompressiveStressLimitOption`: Compressive stress limit as defined in swsFactorOfSafetyStressLimitOption_e (see **Remarks**)
- `DCompressiveStressValue`: Compressive stress value; valid only if NCompressiveStressLimitOption is swsFactorOfSafetyStressLimitOption_e.swsFactorOfSafetyStressLimitOption_UserDefined
- `DMultiplicationFactor`: Stress limit multiplication factor
- `DCompressiveStressMultiplicationFactor`: Compressive stress limit multiplication factor
- `BCombinedStressOnBeams`: True to combine stress on beams, false to not
- `NShellOptions`: Shell face on which to perform the factor of safety as defined by [swsFOS_ShellFaceOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsFOS_ShellFaceOption_e.html)
- `NStepNumber`: Plot step number or 0; 0 gets step 1 for linear static studies and the last available plot step for nonlinear static studies
- `ErrorCode`: Error code as defined by [swsFosPlotErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsFosPlotErrorCode_e.html)

### Return Value

Array of two doubles of the minimum and maximum factors of safety

## VBA Syntax

See [CWResults::GetMinMaxFactorOfSafetyWithDetailSettings2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetMinMaxFactorOfSafetyWithDetailSettings2.html).

## Examples

[Get Factor of Safety Values (VBA)](Get_Factor_of_Safety_Values_for_Composites_Example_VB.htm)
[Get Factor of Safety Values (VB.NET)](Get_Factor_of_Safety_Values_for_Composites_Example_VBNET.htm)
[Get Factor of Safety Values (C#)](Get_Factor_of_Safety_Values_for_Composites_Example_CSharp.htm)

## Remarks

If nonlinearities exist in the study, be advised to not use Factor of Safety to estimate the load-bearing capacity of the system.

| For... | Specify NComponent with swsFOS_NonCompositeCriterion_e.... |
| --- | --- |
| Ductile materials | swsFOSNonCompositeCriterion_VonMisesHencky - or - swsFOSNonCompositeCriterion_Tresca |
| Brittle materials | swsFOSNonCompositeCriterion_MohrCoulomb - or swsFOSNonCompositeCriterion_Coulomb |
| Pure beam studies | swsFOSNonCompositeCriterion_Automatic |

How you set stress limits using NStressLimitOption and NCompressiveStressLimitOption depends on the [model material](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~ModelType.html).

| Specify NStressLimitOption and NCompressiveStressLimitOption with swsFactorOfSafetyStressLimitOption_e... | For swsMaterialModelType_e ... |
| --- | --- |
| swsFactorOfSafetyStressLimitOption_YieldStrength | swsMaterialModelTypeLinearElasticIsotropic swsMaterialModelTypeLinearElasticOrthtropic swsMaterialModelTypeElastoPlasticvonMisesKinematic swsMaterialModelTypeElastoPlasticTrescaKinematic |
| swsFactorOfSafetyStressLimitOption_UltimateStrength | swsMaterialModelTypeLinearElasticIsotropic swsMaterialModelTypeLinearElasticOrthtropic swsMaterialModelTypeNonlinearElastic swsMaterialModelTypeElastoPlasticvonMmisesKinematic swsMaterialModelTypeElastoPlasticTrescaKinematic swsMaterialModelTypeElastoPlasticDruckerPrager swsMaterialModelTypeHyperElasticBlatzko swsMaterialModelTypeHyperElasticMooneyRivlin swsMaterialModelTypeHyperElasticOgden swsMaterialModelTypeViscoElastic swsMaterialModelTypeNitinol |

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetMinMaxFactorOfSafety2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxFactorOfSafety2.html)
[ICWResults::GetFactorOfSafetyForComposites Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetFactorOfSafetyForComposites.html)

## Availability

SOLIDWORKS Simulation API 2018 SP0

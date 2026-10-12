---
title: "GetFactorOfSafetyForComposites Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetFactorOfSafetyForComposites"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetFactorOfSafetyForComposites.html"
---

# GetFactorOfSafetyForComposites Method (ICWResults)

Gets the range of stress or buckling factors of safety for the specified shell type, surface bodies, failure criteria, and other options.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFactorOfSafetyForComposites( _
   ByVal BIsComposite As System.Boolean, _
   ByVal ArraySelectedEntities As System.Object, _
   ByVal NonCompositeCriterion As System.Integer, _
   ByVal CompositeCriterion As System.Integer, _
   ByVal PlyNumber As System.Integer, _
   ByVal ShellFaceOption As System.Integer, _
   ByVal NormalShellFaceOption As System.Integer, _
   ByVal FosDistributionOption As System.Integer, _
   ByVal MinFOSVal As System.Integer, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim BIsComposite As System.Boolean
Dim ArraySelectedEntities As System.Object
Dim NonCompositeCriterion As System.Integer
Dim CompositeCriterion As System.Integer
Dim PlyNumber As System.Integer
Dim ShellFaceOption As System.Integer
Dim NormalShellFaceOption As System.Integer
Dim FosDistributionOption As System.Integer
Dim MinFOSVal As System.Integer
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetFactorOfSafetyForComposites(BIsComposite, ArraySelectedEntities, NonCompositeCriterion, CompositeCriterion, PlyNumber, ShellFaceOption, NormalShellFaceOption, FosDistributionOption, MinFOSVal, ErrorCode)
```

### C#

```csharp
System.object GetFactorOfSafetyForComposites(
   System.bool BIsComposite,
   System.object ArraySelectedEntities,
   System.int NonCompositeCriterion,
   System.int CompositeCriterion,
   System.int PlyNumber,
   System.int ShellFaceOption,
   System.int NormalShellFaceOption,
   System.int FosDistributionOption,
   System.int MinFOSVal,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetFactorOfSafetyForComposites(
   System.bool BIsComposite,
   System.Object^ ArraySelectedEntities,
   System.int NonCompositeCriterion,
   System.int CompositeCriterion,
   System.int PlyNumber,
   System.int ShellFaceOption,
   System.int NormalShellFaceOption,
   System.int FosDistributionOption,
   System.int MinFOSVal,
   [Out] System.int ErrorCode
)
```

### Parameters

- `BIsComposite`: True for a composite shell type, false for a thin or thick shell type
- `ArraySelectedEntities`: Array of selected surface body objects
- `NonCompositeCriterion`: Criterion for non-composite shells as defined in [swsFOS_NonCompositeCriterion_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFOS_NonCompositeCriterion_e.html)
- `CompositeCriterion`: Criterion for composite shells as defined in [swsFOS_CompositeCriterion_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFOS_CompositeCriterion_e.html)
- `PlyNumber`: Number of plies; 0 = across all plies (worst case)
- `ShellFaceOption`: Shell face option as defined in [swsFOS_ShellfaceOption_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFOS_ShellFaceOption_e.html); valid only if PlyNumber > 0
- `NormalShellFaceOption`: Normal shell face option as defined in [swsFOS_NormalShellFaceOption_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFOS_NormalShellFaceOption_e.html)
- `FosDistributionOption`: Plot type as defined in [swsFOS_DistributionOpt_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFOS_DistributionOpt_e.html)
- `MinFOSVal`: Minimum factor of safety; default is 1
- `ErrorCode`: Result status as defined in [swsFOS_ErrorCode_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFOS_ErrorCode_e.html)

### Return Value

Array of two doubles of the minimum and maximum factors of safety

## VBA Syntax

See [CWResults::GetFactorOfSafetyForComposites](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetFactorOfSafetyForComposites.html).

## Examples

[Get Factor of Safety Values for Composites (VBA)](Get_Factor_of_Safety_Values_for_Composites_Example_VB.htm)
[Get Factor of Safety Values for Composites (VB.NET)](Get_Factor_of_Safety_Values_for_Composites_Example_VBNET.htm)
[Get Factor of Safety Values for Composites (C#)](Get_Factor_of_Safety_Values_for_Composites_Example_CSharp.htm)

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetMinMaxFactorOfSafety Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxFactorOfSafety.html)
[ICWResults::GetMinMaxFactorOfSafetyWithDetailSettings Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxFactorOfSafetyWithDetailSettings.html)

## Availability

SOLIDWORKS Simulation API 2013 SP0

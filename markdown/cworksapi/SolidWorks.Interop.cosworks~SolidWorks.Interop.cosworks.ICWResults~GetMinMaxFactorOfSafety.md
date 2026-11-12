---
title: "GetMinMaxFactorOfSafety Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetMinMaxFactorOfSafety"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxFactorOfSafety.html"
---

# GetMinMaxFactorOfSafety Method (ICWResults)

Obsolete. Superseded by [ICWResults::GetMinMaxFactorOfSafety2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxFactorOfSafety2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMinMaxFactorOfSafety( _
   ByVal BAllBodies As System.Boolean, _
   ByVal ArraySelectedEntities As System.Object, _
   ByVal NComponent As System.Integer, _
   ByVal NShellOptions As System.Integer, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim BAllBodies As System.Boolean
Dim ArraySelectedEntities As System.Object
Dim NComponent As System.Integer
Dim NShellOptions As System.Integer
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetMinMaxFactorOfSafety(BAllBodies, ArraySelectedEntities, NComponent, NShellOptions, ErrorCode)
```

### C#

```csharp
System.object GetMinMaxFactorOfSafety(
   System.bool BAllBodies,
   System.object ArraySelectedEntities,
   System.int NComponent,
   System.int NShellOptions,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetMinMaxFactorOfSafety(
   System.bool BAllBodies,
   System.Object^ ArraySelectedEntities,
   System.int NComponent,
   System.int NShellOptions,
   [Out] System.int ErrorCode
)
```

### Parameters

- `BAllBodies`: True to select all bodies to plot the factor of safety, false to select specific bodies
- `ArraySelectedEntities`: Array of bodies for which to plot the factor of safety; valid only if BAllBodies is set to false
- `NComponent`: Failure criterion as defined by [swsFOS_NonCompositeCriterion_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFOS_NonCompositeCriterion_e.html) (see **Remarks**)
- `NShellOptions`: Shell face on which to perform the factor of safety as defined by [swsFOS_ShellFaceOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsFOS_ShellFaceOption_e.html)
- `ErrorCode`: Error code as defined by [swsFosPlotErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsFosPlotErrorCode_e.html)

### Return Value

Array of two doubles of the minimum and maximum factors of safety

## VBA Syntax

See [CWResults::GetMinMaxFactorOfSafety](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetMinMaxFactorOfSafety.html).

## Remarks

For pure beam studies, you can only specify NComponent with swsFOS_NonCompositeCriterion_e.swsFOSNonCompositeCriterion_Automatic.

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetFactorOfSafetyForComposites Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetFactorOfSafetyForComposites.html)
[ICWResults::GetMinMaxFactorOfSafetyWithDetailSettings Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxFactorOfSafetyWithDetailSettings.html)

## Availability

SOLIDWORKS Simulation API 2013 SP5.0

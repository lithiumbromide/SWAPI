---
title: "GetSaveStressAndReactionsOptions Method (ICWStudyResultOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudyResultOptions"
member: "GetSaveStressAndReactionsOptions"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions~GetSaveStressAndReactionsOptions.html"
---

# GetSaveStressAndReactionsOptions Method (ICWStudyResultOptions)

Obsolete. Superseded by [ICWStudyResultOptions::GetSaveStressAndReactionsOptions2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions~GetSaveStressAndReactionsOptions2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSaveStressAndReactionsOptions( _
   ByRef BSaveStressAndReactions As System.Integer, _
   ByRef BVonMisesOnly As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudyResultOptions
Dim BSaveStressAndReactions As System.Integer
Dim BVonMisesOnly As System.Integer
Dim value As System.Boolean

value = instance.GetSaveStressAndReactionsOptions(BSaveStressAndReactions, BVonMisesOnly)
```

### C#

```csharp
System.bool GetSaveStressAndReactionsOptions(
   out System.int BSaveStressAndReactions,
   out System.int BVonMisesOnly
)
```

### C++/CLI

```cpp
System.bool GetSaveStressAndReactionsOptions(
   [Out] System.int BSaveStressAndReactions,
   [Out] System.int BVonMisesOnly
)
```

### Parameters

- `BSaveStressAndReactions`: 1 to save stress and reaction results, 0 to not
- `BVonMisesOnly`: 1 to save nodal von Mises stresses only, 0 to save all stress components; valid only if BSaveStressAndReactions is set to 1

### Return Value

True if successful, false if not

## VBA Syntax

See [CWStudyResultOptions::GetSaveStressAndReactionsOptions](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudyResultOptions~GetSaveStressAndReactionsOptions.html).

## See Also

[ICWStudyResultOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions.html)
[ICWStudyResultOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions_members.html)
[ICWStudyResultOptions::SetSaveStressAndReactionsOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions~SetSaveStressAndReactionsOptions.html)
[ICWStudyResultOptions::SaveDisplacementsAndVelocitiesOption Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions~SaveDisplacementsAndVelocitiesOption.html)
[ICWStudyResultOptions::SaveResultsForSolutionStepsOption Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions~SaveResultsForSolutionStepsOption.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0

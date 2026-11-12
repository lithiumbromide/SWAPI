---
title: "SetSaveStressAndReactionsOptions Method (ICWStudyResultOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudyResultOptions"
member: "SetSaveStressAndReactionsOptions"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions~SetSaveStressAndReactionsOptions.html"
---

# SetSaveStressAndReactionsOptions Method (ICWStudyResultOptions)

Obsolete. Superseded by [ICWStudyResultOptions::SetSaveStressAndReactionsOptions2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions~SetSaveStressAndReactionsOptions2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetSaveStressAndReactionsOptions( _
   ByVal BSaveStressAndReactions As System.Integer, _
   ByVal BVonMisesOnly As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudyResultOptions
Dim BSaveStressAndReactions As System.Integer
Dim BVonMisesOnly As System.Integer
Dim value As System.Boolean

value = instance.SetSaveStressAndReactionsOptions(BSaveStressAndReactions, BVonMisesOnly)
```

### C#

```csharp
System.bool SetSaveStressAndReactionsOptions(
   System.int BSaveStressAndReactions,
   System.int BVonMisesOnly
)
```

### C++/CLI

```cpp
System.bool SetSaveStressAndReactionsOptions(
   System.int BSaveStressAndReactions,
   System.int BVonMisesOnly
)
```

### Parameters

- `BSaveStressAndReactions`: 1 to save stress and reaction results, 0 to not
- `BVonMisesOnly`: 1 to save nodal von Mises stresses only, 0 to save all stress components; valid only if BSaveStressAndReactions is set to 1

### Return Value

True if successful, false if not

## VBA Syntax

See [CWStudyResultOptions::SetSaveStressAndReactionsOptions](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudyResultOptions~SetSaveStressAndReactionsOptions.html).

## See Also

[ICWStudyResultOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions.html)
[ICWStudyResultOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions_members.html)
[ICWStudyResultOptions::GetSaveStressAndReactionsOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions~GetSaveStressAndReactionsOptions.html)
[ICWStudyResultOptions::SaveDisplacementsAndVelocitiesOption Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions~SaveDisplacementsAndVelocitiesOption.html)
[ICWStudyResultOptions::SaveResultsForSolutionStepsOption Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions~SaveResultsForSolutionStepsOption.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0

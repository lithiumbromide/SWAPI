---
title: "SaveStresses Property (ICWStudyResultOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudyResultOptions"
member: "SaveStresses"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions~SaveStresses.html"
---

# SaveStresses Property (ICWStudyResultOptions)

Obsolete. Superseded by [ICWStudyResultOptions::GetSaveStressAndReactionsOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions~GetSaveStressAndReactionsOptions.html) and [ICWStudyResultOptions::SetSaveStressAndReactionsOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions~SetSaveStressAndReactionsOptions.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property SaveStresses As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudyResultOptions
Dim value As System.Integer

instance.SaveStresses = value

value = instance.SaveStresses
```

### C#

```csharp
System.int SaveStresses {get; set;}
```

### C++/CLI

```cpp
property System.int SaveStresses {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to save stress results, 0 to not (see **Remarks**)

## VBA Syntax

See [CWStudyResultOptions::SaveStresses](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudyResultOptions~SaveStresses.html).

## Remarks

This property is valid only for linear dynamic studies and only if [ICWStudyResultOptions::SaveResultsForSolutionStepsOption](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWStudyResultOptions~SaveResultsForSolutionStepsOption.html) = swsSaveResultsOption_e.swsSaveResultsOption_ForSpecifiedSolutionSteps.

## See Also

[ICWStudyResultOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions.html)
[ICWStudyResultOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions_members.html)
[ICWStudyResultOptions::SaveDisplacementsAndVelocitiesOption Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions~SaveDisplacementsAndVelocitiesOption.html)
[ICWStudyResultOptions::SaveReactions Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions~SaveReactions.html)
[ICWStudyResultOptions::SaveResultsForSolutionStepsOption Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions~SaveResultsForSolutionStepsOption.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0

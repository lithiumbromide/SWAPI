---
title: "SaveResultsForSolutionStepsOption Property (ICWStudyResultOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudyResultOptions"
member: "SaveResultsForSolutionStepsOption"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions~SaveResultsForSolutionStepsOption.html"
---

# SaveResultsForSolutionStepsOption Property (ICWStudyResultOptions)

Gets or sets whether results for specified solution steps are saved.

## Syntax

### Visual Basic (Declaration)

```vb
Property SaveResultsForSolutionStepsOption As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudyResultOptions
Dim value As System.Integer

instance.SaveResultsForSolutionStepsOption = value

value = instance.SaveResultsForSolutionStepsOption
```

### C#

```csharp
System.int SaveResultsForSolutionStepsOption {get; set;}
```

### C++/CLI

```cpp
property System.int SaveResultsForSolutionStepsOption {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Save results option as defined in [swsSaveResultsOption_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsSaveResultsOption_e.html)

## VBA Syntax

See [CWStudyResultOptions::SaveResultsForSolutionStepsOption](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudyResultOptions~SaveResultsForSolutionStepsOption.html).

## Examples

See the [ICWStudyResultOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions.html) examples.

## See Also

[ICWStudyResultOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions.html)
[ICWStudyResultOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions_members.html)
[ICWStudyResultOptions::SaveDisplacementsAndVelocitiesOption Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions~SaveDisplacementsAndVelocitiesOption.html)
[ICWStudyResultOptions::SaveReactions Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions~SaveReactions.html)
[ICWStudyResultOptions::SaveStresses Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions~SaveStresses.html)
[ICWStudyResultOptions::GetSolutionStepsSetInformation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions~GetSolutionStepsSetInformation.html)
[ICWStudyResultOptions::SetSolutionStepsSetInformation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions~SetSolutionStepsSetInformation.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0

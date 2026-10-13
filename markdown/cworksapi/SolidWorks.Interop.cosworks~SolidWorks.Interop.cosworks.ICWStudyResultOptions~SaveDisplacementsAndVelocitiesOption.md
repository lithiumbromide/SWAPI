---
title: "SaveDisplacementsAndVelocitiesOption Property (ICWStudyResultOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudyResultOptions"
member: "SaveDisplacementsAndVelocitiesOption"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions~SaveDisplacementsAndVelocitiesOption.html"
---

# SaveDisplacementsAndVelocitiesOption Property (ICWStudyResultOptions)

Gets or sets the displacement and velocity option.

## Syntax

### Visual Basic (Declaration)

```vb
Property SaveDisplacementsAndVelocitiesOption As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudyResultOptions
Dim value As System.Integer

instance.SaveDisplacementsAndVelocitiesOption = value

value = instance.SaveDisplacementsAndVelocitiesOption
```

### C#

```csharp
System.int SaveDisplacementsAndVelocitiesOption {get; set;}
```

### C++/CLI

```cpp
property System.int SaveDisplacementsAndVelocitiesOption {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Option as defined in [swsResultsDisplacementAndVelocityOption_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsDisplacementAndVelocityOption_e.html) (see **Remarks**)

## VBA Syntax

See [CWStudyResultOptions::SaveDisplacementsAndVelocitiesOption](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudyResultOptions~SaveDisplacementsAndVelocitiesOption.html).

## Examples

See the [ICWStudyResultOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions.html) examples.

## Remarks

This property is valid only for linear dynamic studies and only if [ICWStudyResultOptions::SaveResultsForSolutionStepsOption](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWStudyResultOptions~SaveResultsForSolutionStepsOption.html) = swsSaveResultsOption_e.swsSaveResultsOption_ForSpecifiedSolutionSteps.

## See Also

[ICWStudyResultOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions.html)
[ICWStudyResultOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions_members.html)
[ICWStudyResultOptions::SaveReactions Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions~SaveReactions.html)
[ICWStudyResultOptions::SaveStresses Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions~SaveStresses.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0

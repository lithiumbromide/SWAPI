---
title: "SaveDataForRestartingAnalysis Property (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "SaveDataForRestartingAnalysis"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~SaveDataForRestartingAnalysis.html"
---

# SaveDataForRestartingAnalysis Property (ICWNonLinearStudyOptions)

Obsolete. Superseded by [ICWNonLinearStudyOptions::SaveDataForRestartingAnalysis2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~SaveDataForRestartingAnalysis2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property SaveDataForRestartingAnalysis As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
Dim value As System.Integer

instance.SaveDataForRestartingAnalysis = value

value = instance.SaveDataForRestartingAnalysis
```

### C#

```csharp
System.int SaveDataForRestartingAnalysis {get; set;}
```

### C++/CLI

```cpp
property System.int SaveDataForRestartingAnalysis {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

- 1 = Save data for restarting the analysis
- 0 = Do not save data for restarting the analysis

## VBA Syntax

See [CWNonLinearStudyOptions::SaveDataForRestartingAnalysis](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~SaveDataForRestartingAnalysis.html).

## Examples

See the [ICWNonLinearStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html) examples.

## Remarks

After running a nonlinear problem with the option to save data for restarting the analysis, you can continue the solution from the last solution step when you run the problem again.

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0

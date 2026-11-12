---
title: "SaveDataForRestartingAnalysis2 Property (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "SaveDataForRestartingAnalysis2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~SaveDataForRestartingAnalysis2.html"
---

# SaveDataForRestartingAnalysis2 Property (ICWNonLinearStudyOptions)

Gets or sets whether to save data for restarting the analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property SaveDataForRestartingAnalysis2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
Dim value As System.Boolean

instance.SaveDataForRestartingAnalysis2 = value

value = instance.SaveDataForRestartingAnalysis2
```

### C#

```csharp
System.bool SaveDataForRestartingAnalysis2 {get; set;}
```

### C++/CLI

```cpp
property System.bool SaveDataForRestartingAnalysis2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

- -1 or true = Save data for restarting the analysis
- 0 or false = Do not save data for restarting the analysis

(see **Remarks**)

## VBA Syntax

See [CWNonLinearStudyOptions::SaveDataForRestartingAnalysis2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~SaveDataForRestartingAnalysis2.html).

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

After running a nonlinear problem with the option to save data for restarting the analysis, you can continue the solution from the last solution step when you run the problem again.

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2021 SP04

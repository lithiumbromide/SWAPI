---
title: "CreateNewStudy3 Method (ICWStudyManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudyManager"
member: "CreateNewStudy3"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~CreateNewStudy3.html"
---

# CreateNewStudy3 Method (ICWStudyManager)

Creates a new study.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateNewStudy3( _
   ByVal SName As System.String, _
   ByVal NAnalysisType As System.Integer, _
   ByVal NStudySubOptions As System.Integer, _
   ByRef Errors As System.Integer _
) As CWStudy
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudyManager
Dim SName As System.String
Dim NAnalysisType As System.Integer
Dim NStudySubOptions As System.Integer
Dim Errors As System.Integer
Dim value As CWStudy

value = instance.CreateNewStudy3(SName, NAnalysisType, NStudySubOptions, Errors)
```

### C#

```csharp
CWStudy CreateNewStudy3(
   System.string SName,
   System.int NAnalysisType,
   System.int NStudySubOptions,
   out System.int Errors
)
```

### C++/CLI

```cpp
CWStudy^ CreateNewStudy3(
   System.String^ SName,
   System.int NAnalysisType,
   System.int NStudySubOptions,
   [Out] System.int Errors
)
```

### Parameters

- `SName`: New study name
- `NAnalysisType`: Type of study as defined in [swsAnalysisStudyType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsAnalysisStudyType_e.html)
- `NStudySubOptions`:

  | If NAnalysisType is ... | Then NStudySubOptions is a sub-study as defined in ... |
  | --- | --- |
  | swsAnalysisStudyType_e.swsAnalysisStudyTypeDynamic | swsDynamicAnalysisSubType_e |
  | swsAnalysisStudyType_e.swsAnalysisStudyTypeFatigue | swsFatigueStudySubOption_e |
- `Errors`: Error as defined in [swsStudyError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsStudyError_e.html)

### Return Value

[ICWStudy](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWStudy.html)

## VBA Syntax

See [CWStudyManager::CreateNewStudy3](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudyManager~CreateNewStudy3.html).

## Examples

[Create Linear Dynamic Study (VBA)](Create_Dynamic_Harmonic_Study_Example_VB.htm)
[Create Linear Dynamic Study (VB.NET)](Create_Dynamic_Harmonic_Study_Example_VBNET.htm)
[Create Linear Dynamic Study (C#)](Create_Dynamic_Harmonic_Study_Example_CSharp.htm)
[Create Fatigue Study (VBA)](Create_Fatigue_Study_Example_VB.htm)
[Create Fatigue Study (VB.NET)](Create_Fatigue_Study_Example_VBNET.htm)
[Create Fatigue Study (C#)](Create_Fatigue_Study_Example_CSharp.htm)
[Add Remote Load (VBA)](Add_Remote_Load_Example_VB.htm)
[Add Remote Load (VB.NET)](Add_Remote_Load_Example_VBNET.htm)
[Add Remote Load (C#)](Add_Remote_Load_Example_CSharp.htm)
[Create Drop Test Study (VBA)](Create_Drop_Test_Study_Example_VB.htm)
[Create Drop Test Study (VB.NET)](Create_Drop_Test_Study_Example_VBNET.htm)
[Create Drop Test Study (C#)](Create_Drop_Test_Study_Example_CSharp.htm)

## See Also

[ICWStudyManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager.html)
[ICWStudyManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager_members.html)
[ICWStudyManager::DuplicateStudy Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~DuplicateStudy.html)
[ICWStudyManager::ConvertStudy Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~ConvertStudy.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0

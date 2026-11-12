---
title: "GetStudy Method (ICWStudyManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudyManager"
member: "GetStudy"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~GetStudy.html"
---

# GetStudy Method (ICWStudyManager)

Gets the study at the specified index.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetStudy( _
   ByVal NIndex As System.Integer _
) As CWStudy
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudyManager
Dim NIndex As System.Integer
Dim value As CWStudy

value = instance.GetStudy(NIndex)
```

### C#

```csharp
CWStudy GetStudy(
   System.int NIndex
)
```

### C++/CLI

```cpp
CWStudy^ GetStudy(
   System.int NIndex
)
```

### Parameters

- `NIndex`: 0-based index of the study to get

### Return Value

[Study](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWStudy.html)

## VBA Syntax

See [CWStudyManager::GetStudy](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudyManager~GetStudy.html).

## Examples

[Change Beam to Solid Body and Back (C#)](Change_Beam_to_Solid_Body_and_Back_Example_CSharp.htm)
[Change Beam to Solid Body and Back (VB.NET)](Change_Beam_to_Solid_Body_and_Back_Example_VBNET.htm)
[Change Beam to Solid Body and Back (VBA)](Change_Beam_to_Solid_Body_and_Back_Example_VB.htm)

## Remarks

Before calling this method, call [ICWStudyManager::ActiveStudy](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWStudyManager~ActiveStudy.html) to set the index of the active study or [ICWStudyManager::StudyCount](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWStudyManager~StudyCount.html) to get a valid value for NIndex.

## See Also

[ICWStudyManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager.html)
[ICWStudyManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager_members.html)
[ICWStudyManager::DuplicateStudy Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~DuplicateStudy.html)
[ICWStudyManager::ConvertStudy Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~ConvertStudy.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0

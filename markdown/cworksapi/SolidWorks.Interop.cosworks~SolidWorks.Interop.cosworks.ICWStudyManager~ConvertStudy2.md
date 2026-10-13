---
title: "ConvertStudy2 Method (ICWStudyManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudyManager"
member: "ConvertStudy2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~ConvertStudy2.html"
---

# ConvertStudy2 Method (ICWStudyManager)

Converts the specified source study to the specified target study.

## Syntax

### Visual Basic (Declaration)

```vb
Function ConvertStudy2( _
   ByVal SName As System.String, _
   ByVal NSrcStudyType As System.Integer, _
   ByVal SNewName As System.String, _
   ByVal NTargetStudyType As System.Integer, _
   ByVal SConfiguration As System.String, _
   ByVal NTargetStudySubType As System.Integer, _
   ByVal BIncludeMesh As System.Boolean, _
   ByVal BIncludeResults As System.Boolean, _
   ByRef Errors As System.Integer _
) As CWStudy
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudyManager
Dim SName As System.String
Dim NSrcStudyType As System.Integer
Dim SNewName As System.String
Dim NTargetStudyType As System.Integer
Dim SConfiguration As System.String
Dim NTargetStudySubType As System.Integer
Dim BIncludeMesh As System.Boolean
Dim BIncludeResults As System.Boolean
Dim Errors As System.Integer
Dim value As CWStudy

value = instance.ConvertStudy2(SName, NSrcStudyType, SNewName, NTargetStudyType, SConfiguration, NTargetStudySubType, BIncludeMesh, BIncludeResults, Errors)
```

### C#

```csharp
CWStudy ConvertStudy2(
   System.string SName,
   System.int NSrcStudyType,
   System.string SNewName,
   System.int NTargetStudyType,
   System.string SConfiguration,
   System.int NTargetStudySubType,
   System.bool BIncludeMesh,
   System.bool BIncludeResults,
   out System.int Errors
)
```

### C++/CLI

```cpp
CWStudy^ ConvertStudy2(
   System.String^ SName,
   System.int NSrcStudyType,
   System.String^ SNewName,
   System.int NTargetStudyType,
   System.String^ SConfiguration,
   System.int NTargetStudySubType,
   System.bool BIncludeMesh,
   System.bool BIncludeResults,
   [Out] System.int Errors
)
```

### Parameters

- `SName`: Name of study to convert
- `NSrcStudyType`: [swsAnalysisStudyType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsAnalysisStudyType_e.html).swsAnalysisStudyTypeStatic
- `SNewName`: Name of target study to which to convert
- `NTargetStudyType`: (see **Remarks**)
- `SConfiguration`: Name of model configuration
- `NTargetStudySubType`: (see **Remarks**)
- `BIncludeMesh`: True to include mesh when copying the study, false to not
- `BIncludeResults`: True to include results when copying the study, false to not
- `Errors`: Error as defined in [swsStudyError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsStudyError_e.html)

### Return Value

[ICWStudy](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)

## VBA Syntax

See [CWStudyManager::ConvertStudy2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudyManager~ConvertStudy2.html).

## Examples

[Convert Study (VBA)](Convert_Study_Example_VB.htm)
[Convert Study (VB.NET)](Convert_Study_Example_VBNET.htm)
[Convert Study (C#)](Convert_Study_Example_CSharp.htm)

## Remarks

This method is valid only for SOLIDWORKS Simulation Premium.

| If NTargetStudyType is swsAnalysisStudyType_e ... | Then NTargetStudySubType is... |
| --- | --- |
| swsAnalysisStudyTypeDynamic | As defined in swsDynamicAnalysisSubType_e |
| swsAnalysisStudyTypeNonlinear | 0 = Static 1 = Dynamic |
| swsAnalysisStudyTypeStatic | Ignored |

The following boundary conditions are transferred to the target study during conversion:

- Material properties
- Connections
- External loads
- Fixtures
- Mesh
- Study properties

## See Also

[ICWStudyManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager.html)
[ICWStudyManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager_members.html)
[ICWStudyManager::CreateNewStudy3 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~CreateNewStudy3.html)
[ICWStudyManager::DeleteStudy Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~DeleteStudy.html)
[ICWStudyManager::DuplicateStudy2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~DuplicateStudy2.html)
[ICWStudyManager::GetStudy Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~GetStudy.html)
[ICWStudyManager::RenameStudyFromID Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~RenameStudyFromID.html)

## Availability

SOLIDWORKS Simulation API 2024 SP0

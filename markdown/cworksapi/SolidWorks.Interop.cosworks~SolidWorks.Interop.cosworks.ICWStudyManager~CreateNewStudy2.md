---
title: "CreateNewStudy2 Method (ICWStudyManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudyManager"
member: "CreateNewStudy2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~CreateNewStudy2.html"
---

# CreateNewStudy2 Method (ICWStudyManager)

Obsolete. Superseded by [ICWStudyManager::CreateNewStudy3.](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWStudyManager~CreateNewStudy3.html)

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateNewStudy2( _
   ByVal SName As System.String, _
   ByVal NAnalysisType As System.Integer, _
   ByRef Errors As System.Integer _
) As CWStudy
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudyManager
Dim SName As System.String
Dim NAnalysisType As System.Integer
Dim Errors As System.Integer
Dim value As CWStudy

value = instance.CreateNewStudy2(SName, NAnalysisType, Errors)
```

### C#

```csharp
CWStudy CreateNewStudy2(
   System.string SName,
   System.int NAnalysisType,
   out System.int Errors
)
```

### C++/CLI

```cpp
CWStudy^ CreateNewStudy2(
   System.String^ SName,
   System.int NAnalysisType,
   [Out] System.int Errors
)
```

### Parameters

- `SName`: New study name
- `NAnalysisType`: Type of study as defined in [swsAnalysisStudyType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsAnalysisStudyType_e.html)
- `Errors`: Error as defined in [swsStudyError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsStudyError_e.html)

### Return Value

[Study](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWStudy.html)

## VBA Syntax

See [CWStudyManager::CreateNewStudy2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudyManager~CreateNewStudy2.html).

## Examples

[Create Frequency Study with Mixed Mesh (C#)](Create_Frequency_Study_with_Mixed_Mesh_Example_CSharp.htm)
[Create Frequency Study with Mixed Mesh (VB.NET)](Create_Frequency_Study_with_Mixed_Mesh_Example_VBNET.htm)
[Create Frequency Study with Mixed Mesh (VBA)](Create_Frequency_Study_with_Mixed_Mesh_Example_VB.htm)

## See Also

[ICWStudyManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager.html)
[ICWStudyManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager_members.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0

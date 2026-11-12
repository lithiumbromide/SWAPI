---
title: "CreateNewStudy Method (ICWStudyManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudyManager"
member: "CreateNewStudy"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~CreateNewStudy.html"
---

# CreateNewStudy Method (ICWStudyManager)

Obsolete. Superseded by [ICWStudyManager::CreateNewStudy2.](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWStudyManager~CreateNewStudy2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateNewStudy( _
   ByVal SName As System.String, _
   ByVal NAnalysisType As System.Integer, _
   ByVal NMeshType As System.Integer, _
   ByRef Errors As System.Integer _
) As CWStudy
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudyManager
Dim SName As System.String
Dim NAnalysisType As System.Integer
Dim NMeshType As System.Integer
Dim Errors As System.Integer
Dim value As CWStudy

value = instance.CreateNewStudy(SName, NAnalysisType, NMeshType, Errors)
```

### C#

```csharp
CWStudy CreateNewStudy(
   System.string SName,
   System.int NAnalysisType,
   System.int NMeshType,
   out System.int Errors
)
```

### C++/CLI

```cpp
CWStudy^ CreateNewStudy(
   System.String^ SName,
   System.int NAnalysisType,
   System.int NMeshType,
   [Out] System.int Errors
)
```

### Parameters

- `SName`: New study name
- `NAnalysisType`: Type of study as defined in [swsAnalysisStudyType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsAnalysisStudyType_e.html)
- `NMeshType`: Mesh type as defined in [swsMeshType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsMeshType_e.html) (see **Remarks**)
- `Errors`: Error as defined in [swsStudyError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsStudyError_e.html)

### Return Value

[Study](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWStudy.html)

## VBA Syntax

See [CWStudyManager::CreateNewStudy](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudyManager~CreateNewStudy.html).

## Examples

[Create Nonlinear Study and Apply Materials (C#)](Create_Nonlinear_Study_and_Apply_Materials_Example_CSharp.htm)
[Create Nonlinear Study and Apply Materials (VB.NET)](Create_Nonlinear_Study_and_Apply_Materials_Example_VBNET.htm)
[Create Nonlinear Study and Apply Materials (VBA)](Create_Nonlinear_Study_and_Apply_Materials_Example_VB.htm)

## Remarks

Valid mesh types for different types of studies:

| Study Type | Solid Mesh | Shell Mesh | Mixed Mesh (Solid & Shell) | Beam Mesh |
| --- | --- | --- | --- | --- |
| Static | Supported | Supported | Supported | Supported |
| Frequency | Supported | Supported | Supported | Supported |
| Buckling | Supported | Supported | Supported | Supported |
| Thermal | Supported | Supported | Supported | Supported |
| Nonlinear | Supported | Supported | Supported | Not Supported |
| Linear Dynamic | Supported | Supported | Supported | Not Supported |
| Drop Test | Supported | Not Supported | Not Supported | Not Supported |
| Fatigue | Not Applicable | Not Applicable | Not Applicable | Not Applicable |
| Optimization | Not Applicable | Not Applicable | Not Applicable | Not Applicable |

**NOTES:**

- For documents with surface geometry only (no solids), only RefSurfShellElementMesh is supported.
- BeamElementMesh is supported only for static, buckling, and frequency studies.
- Drop test studies support solid mesh only.
- For optimization and fatigue studies do not have mesh on their own. They use mesh of referenced studies. Mesh type is set to SolidElementMesh.

## See Also

[ICWStudyManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager.html)
[ICWStudyManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0

---
title: "GetSymmetryControl Method (ICWTopologyStudyManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyStudyManager"
member: "GetSymmetryControl"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager~GetSymmetryControl.html"
---

# GetSymmetryControl Method (ICWTopologyStudyManager)

Gets the specified symmetry manufacturing control for this topology study.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSymmetryControl( _
   ByVal SControlName As System.String, _
   ByRef ErrorCode As System.Integer _
) As CWTopologySymmetryControl
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyStudyManager
Dim SControlName As System.String
Dim ErrorCode As System.Integer
Dim value As CWTopologySymmetryControl

value = instance.GetSymmetryControl(SControlName, ErrorCode)
```

### C#

```csharp
CWTopologySymmetryControl GetSymmetryControl(
   System.string SControlName,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWTopologySymmetryControl^ GetSymmetryControl(
   System.String^ SControlName,
   [Out] System.int ErrorCode
)
```

### Parameters

- `SControlName`: Name of the symmetry control to retrieve
- `ErrorCode`: Result code as defined in [swsTopologyStudyError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyError_e.html)

### Return Value

[ICWTopologySymmetryControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologySymmetryControl.html); null if failure

## VBA Syntax

See [CWTopologyStudyManager::GetSymmetryControl](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyStudyManager~GetSymmetryControl.html).

## Examples

See the [ICWTopologyStudyManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager.html) example.

## See Also

[ICWTopologyStudyManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager.html)
[ICWTopologyStudyManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0

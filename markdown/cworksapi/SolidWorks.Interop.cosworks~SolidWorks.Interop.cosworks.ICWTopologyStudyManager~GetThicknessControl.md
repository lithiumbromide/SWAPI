---
title: "GetThicknessControl Method (ICWTopologyStudyManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyStudyManager"
member: "GetThicknessControl"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager~GetThicknessControl.html"
---

# GetThicknessControl Method (ICWTopologyStudyManager)

Gets the specified thickness manufacturing control for this topology study.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetThicknessControl( _
   ByVal SControlName As System.String, _
   ByRef ErrorCode As System.Integer _
) As CWTopologyThicknessControl
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyStudyManager
Dim SControlName As System.String
Dim ErrorCode As System.Integer
Dim value As CWTopologyThicknessControl

value = instance.GetThicknessControl(SControlName, ErrorCode)
```

### C#

```csharp
CWTopologyThicknessControl GetThicknessControl(
   System.string SControlName,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWTopologyThicknessControl^ GetThicknessControl(
   System.String^ SControlName,
   [Out] System.int ErrorCode
)
```

### Parameters

- `SControlName`: Name of the thickness control to retrieve
- `ErrorCode`: Result code as defined in [swsTopologyStudyError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyError_e.html)

### Return Value

[ICWTopologyThicknessControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl.html); null if failure

## VBA Syntax

See [CWTopologyStudyManager::GetThicknessControl](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyStudyManager~GetThicknessControl.html).

## See Also

[ICWTopologyStudyManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager.html)
[ICWTopologyStudyManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0

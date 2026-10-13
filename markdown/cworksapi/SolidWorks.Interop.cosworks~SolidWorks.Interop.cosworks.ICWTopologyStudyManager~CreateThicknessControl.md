---
title: "CreateThicknessControl Method (ICWTopologyStudyManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyStudyManager"
member: "CreateThicknessControl"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager~CreateThicknessControl.html"
---

# CreateThicknessControl Method (ICWTopologyStudyManager)

Adds a thickness manufacturing control to this topology study.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateThicknessControl( _
   ByRef ErrorCode As System.Integer _
) As CWTopologyThicknessControl
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyStudyManager
Dim ErrorCode As System.Integer
Dim value As CWTopologyThicknessControl

value = instance.CreateThicknessControl(ErrorCode)
```

### C#

```csharp
CWTopologyThicknessControl CreateThicknessControl(
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWTopologyThicknessControl^ CreateThicknessControl(
   [Out] System.int ErrorCode
)
```

### Parameters

- `ErrorCode`: Result code as defined in [swsTopologyStudyError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyError_e.html)

### Return Value

[ICWTopologyThicknessControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl.html); null if failure

## VBA Syntax

See [CWTopologyStudyManager::CreateThicknessControl](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyStudyManager~CreateThicknessControl.html).

## Examples

See the [ICWTopologyStudyManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager.html) example.

## See Also

[ICWTopologyStudyManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager.html)
[ICWTopologyStudyManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0

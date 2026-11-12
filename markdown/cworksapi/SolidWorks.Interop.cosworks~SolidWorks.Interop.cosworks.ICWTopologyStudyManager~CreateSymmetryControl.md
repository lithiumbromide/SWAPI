---
title: "CreateSymmetryControl Method (ICWTopologyStudyManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyStudyManager"
member: "CreateSymmetryControl"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager~CreateSymmetryControl.html"
---

# CreateSymmetryControl Method (ICWTopologyStudyManager)

Adds a symmetry manufacturing control to this topology study.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateSymmetryControl( _
   ByRef ErrorCode As System.Integer _
) As CWTopologySymmetryControl
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyStudyManager
Dim ErrorCode As System.Integer
Dim value As CWTopologySymmetryControl

value = instance.CreateSymmetryControl(ErrorCode)
```

### C#

```csharp
CWTopologySymmetryControl CreateSymmetryControl(
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWTopologySymmetryControl^ CreateSymmetryControl(
   [Out] System.int ErrorCode
)
```

### Parameters

- `ErrorCode`: Result code as defined in [swsTopologyStudyError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyError_e.html)

### Return Value

[ICWTopologySymmetryControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologySymmetryControl.html); null if failure

## VBA Syntax

See [CWTopologyStudyManager::CreateSymmetryControl](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyStudyManager~CreateSymmetryControl.html).

## Examples

See the [ICWTopologyStudyManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager.html) example.

## See Also

[ICWTopologyStudyManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager.html)
[ICWTopologyStudyManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0

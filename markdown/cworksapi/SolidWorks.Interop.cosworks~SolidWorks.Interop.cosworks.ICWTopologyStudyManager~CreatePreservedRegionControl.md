---
title: "CreatePreservedRegionControl Method (ICWTopologyStudyManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyStudyManager"
member: "CreatePreservedRegionControl"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager~CreatePreservedRegionControl.html"
---

# CreatePreservedRegionControl Method (ICWTopologyStudyManager)

Adds a preserved region manufacturing control to this topology study.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreatePreservedRegionControl( _
   ByRef ErrorCode As System.Integer _
) As CWTopologyPreservedRegion
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyStudyManager
Dim ErrorCode As System.Integer
Dim value As CWTopologyPreservedRegion

value = instance.CreatePreservedRegionControl(ErrorCode)
```

### C#

```csharp
CWTopologyPreservedRegion CreatePreservedRegionControl(
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWTopologyPreservedRegion^ CreatePreservedRegionControl(
   [Out] System.int ErrorCode
)
```

### Parameters

- `ErrorCode`: Result code as defined in [swsTopologyStudyError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyError_e.html)

### Return Value

[ICWTopologyPreservedRegionControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyPreservedRegionControl.html); null if failure

## VBA Syntax

See [CWTopologyStudyManager::CreatePreservedRegionControl](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyStudyManager~CreatePreservedRegionControl.html).

## Examples

See the [ICWTopologyStudyManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager.html) example.

## See Also

[ICWTopologyStudyManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager.html)
[ICWTopologyStudyManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0

---
title: "GetPreservedRegionControl Method (ICWTopologyStudyManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyStudyManager"
member: "GetPreservedRegionControl"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager~GetPreservedRegionControl.html"
---

# GetPreservedRegionControl Method (ICWTopologyStudyManager)

Gets the specified preserved region manufacturing control for this topology study.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPreservedRegionControl( _
   ByVal SControlName As System.String, _
   ByRef ErrorCode As System.Integer _
) As CWTopologyPreservedRegion
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyStudyManager
Dim SControlName As System.String
Dim ErrorCode As System.Integer
Dim value As CWTopologyPreservedRegion

value = instance.GetPreservedRegionControl(SControlName, ErrorCode)
```

### C#

```csharp
CWTopologyPreservedRegion GetPreservedRegionControl(
   System.string SControlName,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWTopologyPreservedRegion^ GetPreservedRegionControl(
   System.String^ SControlName,
   [Out] System.int ErrorCode
)
```

### Parameters

- `SControlName`: Name of the preserved region control to retrieve
- `ErrorCode`: Result code as defined in [swsTopologyStudyError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyError_e.html)

### Return Value

[ICWTopologyPreservedRegionControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyPreservedRegionControl.html); null if failure

## VBA Syntax

See [CWTopologyStudyManager::GetPreservedRegionControl](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyStudyManager~GetPreservedRegionControl.html).

## Examples

See the [ICWTopologyStudyManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager.html) example.

## See Also

[ICWTopologyStudyManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager.html)
[ICWTopologyStudyManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0

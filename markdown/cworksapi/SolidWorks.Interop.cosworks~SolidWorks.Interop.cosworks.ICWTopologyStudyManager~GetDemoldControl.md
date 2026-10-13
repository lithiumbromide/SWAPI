---
title: "GetDemoldControl Method (ICWTopologyStudyManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyStudyManager"
member: "GetDemoldControl"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager~GetDemoldControl.html"
---

# GetDemoldControl Method (ICWTopologyStudyManager)

Gets the specified demold manufacturing control for this topology study.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDemoldControl( _
   ByVal SControlName As System.String, _
   ByRef ErrorCode As System.Integer _
) As CWTopologyDemoldControl
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyStudyManager
Dim SControlName As System.String
Dim ErrorCode As System.Integer
Dim value As CWTopologyDemoldControl

value = instance.GetDemoldControl(SControlName, ErrorCode)
```

### C#

```csharp
CWTopologyDemoldControl GetDemoldControl(
   System.string SControlName,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWTopologyDemoldControl^ GetDemoldControl(
   System.String^ SControlName,
   [Out] System.int ErrorCode
)
```

### Parameters

- `SControlName`: Name of the demold control to retrieve
- `ErrorCode`: Result code as defined in [swsTopologyStudyError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyError_e.html)

### Return Value

[ICWTopologyDemoldControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl.html); null if failure

## VBA Syntax

See [CWTopologyStudyManager::GetDemoldControl](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyStudyManager~GetDemoldControl.html).

## Examples

See the [ICWTopologyStudyManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager.html) example.

## See Also

[ICWTopologyStudyManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager.html)
[ICWTopologyStudyManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0

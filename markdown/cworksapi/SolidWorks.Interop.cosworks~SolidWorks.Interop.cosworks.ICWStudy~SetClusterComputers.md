---
title: "SetClusterComputers Method (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "SetClusterComputers"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~SetClusterComputers.html"
---

# SetClusterComputers Method (ICWStudy)

Sets the list of names of the computers participating in this study's distributed simulation.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetClusterComputers( _
   ByVal ComputerNames As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim ComputerNames As System.Object
Dim value As System.Integer

value = instance.SetClusterComputers(ComputerNames)
```

### C#

```csharp
System.int SetClusterComputers(
   System.object ComputerNames
)
```

### C++/CLI

```cpp
System.int SetClusterComputers(
   System.Object^ ComputerNames
)
```

### Parameters

- `ComputerNames`: Array of computer names

### Return Value

Error code as defined in [swsDistributedSimulationError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsDistributedSimulationError_e.html)

## VBA Syntax

See [CWStudy::SetClusterComputers](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~SetClusterComputers.html).

## Remarks

This method is valid only if:

- The license is SOLIDWORKS Simulation Professional or Premium.
- [ICWStudy::IsSimulationDistributable](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~IsSimulationDistributable.html) is true.
- [ICWStudy::OffLoad](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~OffLoad.html) is true.

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)
[ICWStudy::GetClusterComputers Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~GetClusterComputers.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0

---
title: "RemoveControl Method (ICWTopologyStudyManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyStudyManager"
member: "RemoveControl"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager~RemoveControl.html"
---

# RemoveControl Method (ICWTopologyStudyManager)

Removes the specified manufacturing control from this topology study.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveControl( _
   ByVal SControlName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyStudyManager
Dim SControlName As System.String
Dim value As System.Integer

value = instance.RemoveControl(SControlName)
```

### C#

```csharp
System.int RemoveControl(
   System.string SControlName
)
```

### C++/CLI

```cpp
System.int RemoveControl(
   System.String^ SControlName
)
```

### Parameters

- `SControlName`: Name of the control to remove

### Return Value

Result code as defined in [swsTopologyStudyError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyError_e.html)

## VBA Syntax

See [CWTopologyStudyManager::RemoveControl](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyStudyManager~RemoveControl.html).

## See Also

[ICWTopologyStudyManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager.html)
[ICWTopologyStudyManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0

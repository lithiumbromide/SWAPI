---
title: "CreateMassConstraint Method (ICWTopologyStudyManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyStudyManager"
member: "CreateMassConstraint"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager~CreateMassConstraint.html"
---

# CreateMassConstraint Method (ICWTopologyStudyManager)

Adds a mass constraint to this topology study.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateMassConstraint( _
   ByRef ErrorCode As System.Integer _
) As CWTopologyMassConstraint
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyStudyManager
Dim ErrorCode As System.Integer
Dim value As CWTopologyMassConstraint

value = instance.CreateMassConstraint(ErrorCode)
```

### C#

```csharp
CWTopologyMassConstraint CreateMassConstraint(
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWTopologyMassConstraint^ CreateMassConstraint(
   [Out] System.int ErrorCode
)
```

### Parameters

- `ErrorCode`: Result code as defined in [swsTopologyStudyError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyError_e.html)

### Return Value

[ICWTopologyMassConstraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMassConstraint.html); null if failure

## VBA Syntax

See [CWTopologyStudyManager::CreateMassConstraint](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyStudyManager~CreateMassConstraint.html).

## See Also

[ICWTopologyStudyManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager.html)
[ICWTopologyStudyManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager_members.html)
[ICWTopologyStudyManager::RemoveConstraint Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager~RemoveConstraint.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0

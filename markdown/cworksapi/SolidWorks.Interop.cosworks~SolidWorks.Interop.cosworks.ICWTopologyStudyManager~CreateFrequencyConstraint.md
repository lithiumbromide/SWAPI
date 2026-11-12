---
title: "CreateFrequencyConstraint Method (ICWTopologyStudyManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyStudyManager"
member: "CreateFrequencyConstraint"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager~CreateFrequencyConstraint.html"
---

# CreateFrequencyConstraint Method (ICWTopologyStudyManager)

Adds a frequency constraint to this topology study.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateFrequencyConstraint( _
   ByRef ErrorCode As System.Integer _
) As CWTopologyFrequencyConstraint
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyStudyManager
Dim ErrorCode As System.Integer
Dim value As CWTopologyFrequencyConstraint

value = instance.CreateFrequencyConstraint(ErrorCode)
```

### C#

```csharp
CWTopologyFrequencyConstraint CreateFrequencyConstraint(
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWTopologyFrequencyConstraint^ CreateFrequencyConstraint(
   [Out] System.int ErrorCode
)
```

### Parameters

- `ErrorCode`: Result code as defined in [swsTopologyStudyError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyError_e.html)

### Return Value

[ICWTopologyFrequencyConstraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFrequencyConstraint.html); null if failure

## VBA Syntax

See [CWTopologyStudyManager::CreateFrequencyConstraint](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyStudyManager~CreateFrequencyConstraint.html).

## Examples

See the [ICWTopologyStudyManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager.html) example.

## See Also

[ICWTopologyStudyManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager.html)
[ICWTopologyStudyManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0

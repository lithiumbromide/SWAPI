---
title: "GetFrequencyConstraint Method (ICWTopologyStudyManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyStudyManager"
member: "GetFrequencyConstraint"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager~GetFrequencyConstraint.html"
---

# GetFrequencyConstraint Method (ICWTopologyStudyManager)

Gets the specified frequency constraint for this topology study.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFrequencyConstraint( _
   ByVal SConstraintName As System.String, _
   ByRef ErrorCode As System.Integer _
) As CWTopologyFrequencyConstraint
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyStudyManager
Dim SConstraintName As System.String
Dim ErrorCode As System.Integer
Dim value As CWTopologyFrequencyConstraint

value = instance.GetFrequencyConstraint(SConstraintName, ErrorCode)
```

### C#

```csharp
CWTopologyFrequencyConstraint GetFrequencyConstraint(
   System.string SConstraintName,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWTopologyFrequencyConstraint^ GetFrequencyConstraint(
   System.String^ SConstraintName,
   [Out] System.int ErrorCode
)
```

### Parameters

- `SConstraintName`: Name of the frequency constraint to retrieve
- `ErrorCode`: Result code as defined in [swsTopologyStudyError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyError_e.html)

### Return Value

[ICWTopologyFrequencyConstraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFrequencyConstraint.html); null if failure

## VBA Syntax

See [CWTopologyStudyManager::GetFrequencyConstraint](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyStudyManager~GetFrequencyConstraint.html).

## Examples

See the [ICWTopologyStudyManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager.html) example.

## See Also

[ICWTopologyStudyManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager.html)
[ICWTopologyStudyManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0

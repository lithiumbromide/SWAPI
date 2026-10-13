---
title: "GetFactorOfSafetyConstraint Method (ICWTopologyStudyManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyStudyManager"
member: "GetFactorOfSafetyConstraint"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager~GetFactorOfSafetyConstraint.html"
---

# GetFactorOfSafetyConstraint Method (ICWTopologyStudyManager)

Gets the specified Factor Of Safety constraint for this topology study.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFactorOfSafetyConstraint( _
   ByVal SConstraintName As System.String, _
   ByRef ErrorCode As System.Integer _
) As CWTopologyFactorOfSafetyConstraint
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyStudyManager
Dim SConstraintName As System.String
Dim ErrorCode As System.Integer
Dim value As CWTopologyFactorOfSafetyConstraint

value = instance.GetFactorOfSafetyConstraint(SConstraintName, ErrorCode)
```

### C#

```csharp
CWTopologyFactorOfSafetyConstraint GetFactorOfSafetyConstraint(
   System.string SConstraintName,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWTopologyFactorOfSafetyConstraint^ GetFactorOfSafetyConstraint(
   System.String^ SConstraintName,
   [Out] System.int ErrorCode
)
```

### Parameters

- `SConstraintName`: Name of the Factory Of Safety constraint to retrieve
- `ErrorCode`: Result code as defined in [swsTopologyStudyError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyError_e.html)

### Return Value

[ICWTopologyFactorOfSafetyConstraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFactorOfSafetyConstraint.html); null if failure

## VBA Syntax

See [CWTopologyStudyManager::GetFactorOfSafetyConstraint](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyStudyManager~GetFactorOfSafetyConstraint.html).

## Examples

See the [ICWTopologyStudyManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager.html) example.

## See Also

[ICWTopologyStudyManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager.html)
[ICWTopologyStudyManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0

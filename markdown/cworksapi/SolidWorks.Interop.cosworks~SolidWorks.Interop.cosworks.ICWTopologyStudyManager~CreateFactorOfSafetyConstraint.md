---
title: "CreateFactorOfSafetyConstraint Method (ICWTopologyStudyManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyStudyManager"
member: "CreateFactorOfSafetyConstraint"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager~CreateFactorOfSafetyConstraint.html"
---

# CreateFactorOfSafetyConstraint Method (ICWTopologyStudyManager)

Adds a Factor Of Safety constraint to this topology study.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateFactorOfSafetyConstraint( _
   ByRef ErrorCode As System.Integer _
) As CWTopologyFactorOfSafetyConstraint
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyStudyManager
Dim ErrorCode As System.Integer
Dim value As CWTopologyFactorOfSafetyConstraint

value = instance.CreateFactorOfSafetyConstraint(ErrorCode)
```

### C#

```csharp
CWTopologyFactorOfSafetyConstraint CreateFactorOfSafetyConstraint(
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWTopologyFactorOfSafetyConstraint^ CreateFactorOfSafetyConstraint(
   [Out] System.int ErrorCode
)
```

### Parameters

- `ErrorCode`: Result code as defined in [swsTopologyStudyError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyError_e.html)

### Return Value

[ICWTopologyFactorOfSafetyConstraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFactorOfSafetyConstraint.html); null if failure

## VBA Syntax

See [CWTopologyStudyManager::CreateFactorOfSafetyConstraint](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyStudyManager~CreateFactorOfSafetyConstraint.html).

## Examples

See the [ICWTopologyStudyManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager.html) example.

## Remarks

If a topology stress constraint exists, this method will replace it with a Factor of Safety constraint.

## See Also

[ICWTopologyStudyManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager.html)
[ICWTopologyStudyManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0

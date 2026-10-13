---
title: "GetStressConstraint Method (ICWTopologyStudyManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyStudyManager"
member: "GetStressConstraint"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager~GetStressConstraint.html"
---

# GetStressConstraint Method (ICWTopologyStudyManager)

Gets the specified stress constraint for this topology study.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetStressConstraint( _
   ByVal SConstraintName As System.String, _
   ByRef ErrorCode As System.Integer _
) As CWTopologyStressConstraint
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyStudyManager
Dim SConstraintName As System.String
Dim ErrorCode As System.Integer
Dim value As CWTopologyStressConstraint

value = instance.GetStressConstraint(SConstraintName, ErrorCode)
```

### C#

```csharp
CWTopologyStressConstraint GetStressConstraint(
   System.string SConstraintName,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWTopologyStressConstraint^ GetStressConstraint(
   System.String^ SConstraintName,
   [Out] System.int ErrorCode
)
```

### Parameters

- `SConstraintName`: Name of the stress constraint to retrieve
- `ErrorCode`: Result code as defined in [swsTopologyStudyError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyError_e.html)

### Return Value

[ICWTopologyStressConstraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStressConstraint.html); null if failure

## VBA Syntax

See [CWTopologyStudyManager::GetStressConstraint](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyStudyManager~GetStressConstraint.html).

## Examples

See the [ICWTopologyStudyManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager.html) example.

## See Also

[ICWTopologyStudyManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager.html)
[ICWTopologyStudyManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0

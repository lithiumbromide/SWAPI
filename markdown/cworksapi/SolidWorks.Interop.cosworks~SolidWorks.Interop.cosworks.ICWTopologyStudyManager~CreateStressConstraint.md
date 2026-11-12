---
title: "CreateStressConstraint Method (ICWTopologyStudyManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyStudyManager"
member: "CreateStressConstraint"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager~CreateStressConstraint.html"
---

# CreateStressConstraint Method (ICWTopologyStudyManager)

Adds a stress constraint to this topology study.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateStressConstraint( _
   ByRef ErrorCode As System.Integer _
) As CWTopologyStressConstraint
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyStudyManager
Dim ErrorCode As System.Integer
Dim value As CWTopologyStressConstraint

value = instance.CreateStressConstraint(ErrorCode)
```

### C#

```csharp
CWTopologyStressConstraint CreateStressConstraint(
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWTopologyStressConstraint^ CreateStressConstraint(
   [Out] System.int ErrorCode
)
```

### Parameters

- `ErrorCode`: Result code as defined in [swsTopologyStudyError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyError_e.html)

### Return Value

[ICWTopologyStressConstraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStressConstraint.html); null if failure

## VBA Syntax

See [CWTopologyStudyManager::CreateStressConstraint](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyStudyManager~CreateStressConstraint.html).

## Examples

See the [ICWTopologyStudyManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager.html) example.

## Remarks

If a topology Factor Of Safety constraint exists, this method will replace it with a stress constraint.

## See Also

[ICWTopologyStudyManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager.html)
[ICWTopologyStudyManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0

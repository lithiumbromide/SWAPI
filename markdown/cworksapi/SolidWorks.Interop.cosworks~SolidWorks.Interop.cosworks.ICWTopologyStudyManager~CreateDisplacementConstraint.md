---
title: "CreateDisplacementConstraint Method (ICWTopologyStudyManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyStudyManager"
member: "CreateDisplacementConstraint"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager~CreateDisplacementConstraint.html"
---

# CreateDisplacementConstraint Method (ICWTopologyStudyManager)

Adds a displacement constraint to this topology study.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateDisplacementConstraint( _
   ByRef ErrorCode As System.Integer _
) As CWTopologyDisplacementConstraint
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyStudyManager
Dim ErrorCode As System.Integer
Dim value As CWTopologyDisplacementConstraint

value = instance.CreateDisplacementConstraint(ErrorCode)
```

### C#

```csharp
CWTopologyDisplacementConstraint CreateDisplacementConstraint(
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWTopologyDisplacementConstraint^ CreateDisplacementConstraint(
   [Out] System.int ErrorCode
)
```

### Parameters

- `ErrorCode`: Result code as defined in [swsTopologyStudyError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyError_e.html)

### Return Value

[ICWTopologyDisplacementConstraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint.html); null if failure

## VBA Syntax

See [CWTopologyStudyManager::CreateDisplacementConstraint](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyStudyManager~CreateDisplacementConstraint.html).

## Examples

See the [ICWTopologyStudyManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager.html) example.

## See Also

[ICWTopologyStudyManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager.html)
[ICWTopologyStudyManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager_members.html)
[ICWTopologyStudyManager::RemoveConstraint Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager~RemoveConstraint.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0

---
title: "GetDisplacementConstraint Method (ICWTopologyStudyManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyStudyManager"
member: "GetDisplacementConstraint"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager~GetDisplacementConstraint.html"
---

# GetDisplacementConstraint Method (ICWTopologyStudyManager)

Gets the specified displacement constraint for this topology study.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDisplacementConstraint( _
   ByVal SConstraintName As System.String, _
   ByRef ErrorCode As System.Integer _
) As CWTopologyDisplacementConstraint
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyStudyManager
Dim SConstraintName As System.String
Dim ErrorCode As System.Integer
Dim value As CWTopologyDisplacementConstraint

value = instance.GetDisplacementConstraint(SConstraintName, ErrorCode)
```

### C#

```csharp
CWTopologyDisplacementConstraint GetDisplacementConstraint(
   System.string SConstraintName,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWTopologyDisplacementConstraint^ GetDisplacementConstraint(
   System.String^ SConstraintName,
   [Out] System.int ErrorCode
)
```

### Parameters

- `SConstraintName`: Name of the displacement constraint to retrieve
- `ErrorCode`: Result code as defined in [swsTopologyStudyError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyError_e.html)

### Return Value

[ICWTopologyDisplacementConstraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint.html); null if failure

## VBA Syntax

See [CWTopologyStudyManager::GetDisplacementConstraint](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyStudyManager~GetDisplacementConstraint.html).

## Examples

See the [ICWTopologyStudyManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager.html) example.

## See Also

[ICWTopologyStudyManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager.html)
[ICWTopologyStudyManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager_members.html)
[ICWTopologyStudyManager::RemoveConstraint Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager~RemoveConstraint.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0

---
title: "GetMassConstraint Method (ICWTopologyStudyManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyStudyManager"
member: "GetMassConstraint"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager~GetMassConstraint.html"
---

# GetMassConstraint Method (ICWTopologyStudyManager)

Gets the specified mass constraint for this topology study.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMassConstraint( _
   ByVal SConstraintName As System.String, _
   ByRef ErrorCode As System.Integer _
) As CWTopologyMassConstraint
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyStudyManager
Dim SConstraintName As System.String
Dim ErrorCode As System.Integer
Dim value As CWTopologyMassConstraint

value = instance.GetMassConstraint(SConstraintName, ErrorCode)
```

### C#

```csharp
CWTopologyMassConstraint GetMassConstraint(
   System.string SConstraintName,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWTopologyMassConstraint^ GetMassConstraint(
   System.String^ SConstraintName,
   [Out] System.int ErrorCode
)
```

### Parameters

- `SConstraintName`: Name of the mass constraint to retrieve
- `ErrorCode`: Result code as defined in [swsTopologyStudyError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyError_e.html)

### Return Value

[ICWTopologyMassConstraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMassConstraint.html); null if failure

## VBA Syntax

See [CWTopologyStudyManager::GetMassConstraint](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyStudyManager~GetMassConstraint.html).

## Examples

See the [ICWTopologyStudyManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager.html) example.

## See Also

[ICWTopologyStudyManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager.html)
[ICWTopologyStudyManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager_members.html)
[ICWTopologyStudyManager::RemoveConstraint Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager~RemoveConstraint.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0

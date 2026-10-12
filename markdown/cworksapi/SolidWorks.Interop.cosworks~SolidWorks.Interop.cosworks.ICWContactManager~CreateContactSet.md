---
title: "CreateContactSet Method (ICWContactManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactManager"
member: "CreateContactSet"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~CreateContactSet.html"
---

# CreateContactSet Method (ICWContactManager)

Obsolete. Superseded by [ICWContactManager::CreateContactSet2](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWContactManager~CreateContactSet2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateContactSet( _
   ByVal NContactSetType As System.Integer, _
   ByVal ArraySourceEntities As System.Object, _
   ByVal ArrayTargetEntities As System.Object, _
   ByRef ErrorCode As System.Integer _
) As CWContactSet
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactManager
Dim NContactSetType As System.Integer
Dim ArraySourceEntities As System.Object
Dim ArrayTargetEntities As System.Object
Dim ErrorCode As System.Integer
Dim value As CWContactSet

value = instance.CreateContactSet(NContactSetType, ArraySourceEntities, ArrayTargetEntities, ErrorCode)
```

### C#

```csharp
CWContactSet CreateContactSet(
   System.int NContactSetType,
   System.object ArraySourceEntities,
   System.object ArrayTargetEntities,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWContactSet^ CreateContactSet(
   System.int NContactSetType,
   System.Object^ ArraySourceEntities,
   System.Object^ ArrayTargetEntities,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NContactSetType`: Type of contact set for

  - [static](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWStaticStudyOptions.html) and [nonlinear](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWNonLinearStudyOptions.html) studies as defined in [swsContactSetTypeStaticNonLinear_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsContactSetTypeStaticNonLinear_e.html)
  - [thermal](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWThermalStudyOptions.html) studies as defined in [swsContactSetTypeThermal_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsContactSetTypeThermal_e.html)
  - [buckling](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBucklingStudyOptions.html) and [frequency](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWFrequencyStudyOptions.html) studies as defined in [swsContactType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsContactType_e.html), excluding swsContactTypeStaticNoPenetration
- `ArraySourceEntities`: Array of source entities
- `ArrayTargetEntities`: Array of target faces
- `ErrorCode`: Error code as defined in [swsContactSetError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsContactSetError_e.html)

### Return Value

[Contact set](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWContactSet.html)

## VBA Syntax

See [CWContactManager::CreateContactSet](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactManager~CreateContactSet.html).

## Remarks

Contact set definitions override global and component contact definitions. Component contact definitions override global contact definitions.

## See Also

[ICWContactManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager.html)
[ICWContactManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager_members.html)
[ICWContactManager::DeleteContactSet Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~DeleteContactSet.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0

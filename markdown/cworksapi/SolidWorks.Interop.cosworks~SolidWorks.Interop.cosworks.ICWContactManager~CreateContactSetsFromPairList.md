---
title: "CreateContactSetsFromPairList Method (ICWContactManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactManager"
member: "CreateContactSetsFromPairList"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~CreateContactSetsFromPairList.html"
---

# CreateContactSetsFromPairList Method (ICWContactManager)

Creates contact sets from the specified contact pairs.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateContactSetsFromPairList( _
   ByVal NContactSetType As System.Integer, _
   ByVal VarPairs As System.Object, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactManager
Dim NContactSetType As System.Integer
Dim VarPairs As System.Object
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.CreateContactSetsFromPairList(NContactSetType, VarPairs, ErrorCode)
```

### C#

```csharp
System.object CreateContactSetsFromPairList(
   System.int NContactSetType,
   System.object VarPairs,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ CreateContactSetsFromPairList(
   System.int NContactSetType,
   System.Object^ VarPairs,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NContactSetType`: Type of contact set for:

  - [static](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWStaticStudyOptions.html) and [nonlinear](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWNonLinearStudyOptions.html) studies as defined in [swsContactSetTypeStaticNonLinear_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsContactSetTypeStaticNonLinear_e.html)
  - [thermal](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWThermalStudyOptions.html) studies as defined in [swsContactSetTypeThermal_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsContactSetTypeThermal_e.html)
  - [buckling](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBucklingStudyOptions.html) and [frequency](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWFrequencyStudyOptions.html) studies as defined in [swsContactType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsContactType_e.html), excluding swsContactTypeStaticNoPenetration
- `VarPairs`: Array of contact pairs (see **Remarks**)
- `ErrorCode`: Error code as defined in [swsContactSetError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsContactSetError_e.html)

### Return Value

Array of [contact sets](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet.html)

## VBA Syntax

See [CWContactManager::CreateContactSetsFromPairList](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactManager~CreateContactSetsFromPairList.html).

## Remarks

To populate varPairs, call one of the following:

- [ICWContactManager::FindNonTouchingPairs](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~FindNonTouchingPairs.html)
- [ICWContactManager::FindTouchingEdgeFacePairs](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~FindTouchingEdgeFacePairs.html)
- [ICWContactManager::FindTouchingFacePairs](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~FindTouchingFacePairs.html)

See the SOLIDWORKS Simulation Help for guidelines about studies with contact conditions.

## See Also

[ICWContactManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager.html)
[ICWContactManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager_members.html)
[ICWContactManager::CreateContactSet2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~CreateContactSet2.html)
[ICWContactManager::DeleteContactSet Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~DeleteContactSet.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0

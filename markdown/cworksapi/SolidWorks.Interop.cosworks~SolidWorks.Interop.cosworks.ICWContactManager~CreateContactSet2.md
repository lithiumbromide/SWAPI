---
title: "CreateContactSet2 Method (ICWContactManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactManager"
member: "CreateContactSet2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~CreateContactSet2.html"
---

# CreateContactSet2 Method (ICWContactManager)

Creates a contact set.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateContactSet2( _
   ByVal NContactSetType As System.Integer, _
   ByVal NSelectionType As System.Integer, _
   ByVal ArraySourceEntities As System.Object, _
   ByVal ArrayTargetEntities As System.Object, _
   ByRef ErrorCode As System.Integer _
) As CWContactSet
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactManager
Dim NContactSetType As System.Integer
Dim NSelectionType As System.Integer
Dim ArraySourceEntities As System.Object
Dim ArrayTargetEntities As System.Object
Dim ErrorCode As System.Integer
Dim value As CWContactSet

value = instance.CreateContactSet2(NContactSetType, NSelectionType, ArraySourceEntities, ArrayTargetEntities, ErrorCode)
```

### C#

```csharp
CWContactSet CreateContactSet2(
   System.int NContactSetType,
   System.int NSelectionType,
   System.object ArraySourceEntities,
   System.object ArrayTargetEntities,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWContactSet^ CreateContactSet2(
   System.int NContactSetType,
   System.int NSelectionType,
   System.Object^ ArraySourceEntities,
   System.Object^ ArrayTargetEntities,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NContactSetType`: Type of contact set for:

  - [static](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWStaticStudyOptions.html) and [nonlinear](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWNonLinearStudyOptions.html) studies as defined in [swsContactSetTypeStaticNonLinear_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsContactSetTypeStaticNonLinear_e.html)
  - [thermal](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWThermalStudyOptions.html) studies as defined in [swsContactSetTypeThermal_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsContactSetTypeThermal_e.html)
  - [buckling](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBucklingStudyOptions.html) and [frequency](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWFrequencyStudyOptions.html) studies as defined in [swsContactType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsContactType_e.html), excluding swsContactTypeStaticNoPenetration
- `NSelectionType`: Type of selection as defined in [swsSelectionType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsSelectionType_e.html)
- `ArraySourceEntities`: Array of source entities
- `ArrayTargetEntities`: Array of target faces
- `ErrorCode`: Error code as defined in [swsContactSetError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsContactSetError_e.html)

### Return Value

[Contact set](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWContactSet.html)

## VBA Syntax

See [CWContactManager::CreateContactSet2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactManager~CreateContactSet2.html).

## Examples

[Create Frequency Study with Mixed Mesh (C#)](Create_Frequency_Study_with_Mixed_Mesh_Example_CSharp.htm)
[Create Frequency Study with Mixed Mesh (VB.NET)](Create_Frequency_Study_with_Mixed_Mesh_Example_VBNET.htm)
[Create Frequency Study with Mixed Mesh (VBA)](Create_Frequency_Study_with_Mixed_Mesh_Example_VB.htm)

## Remarks

Contact set definitions override both global and component contact definitions. Component contact definitions override global contact definitions.

See the SOLIDWORKS Simulation Help for guidelines about studies with contact conditions.

## See Also

[ICWContactManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager.html)
[ICWContactManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager_members.html)
[ICWContactManager::DeleteContactSet Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~DeleteContactSet.html)
[ICWContactManager::CreateContactSetsFromPairList Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~CreateContactSetsFromPairList.html)

## Availability

SOLIDWORKS Simulation API 2010 SP0

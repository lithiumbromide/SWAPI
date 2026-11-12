---
title: "SetStudyAssociationData Method (ICWFatigueEvent)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFatigueEvent"
member: "SetStudyAssociationData"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent~SetStudyAssociationData.html"
---

# SetStudyAssociationData Method (ICWFatigueEvent)

Sets the study association data for this fatigue event.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetStudyAssociationData( _
   ByVal NCount As System.Integer, _
   ByVal VarStudyNames As System.Object, _
   ByVal VarScales As System.Object, _
   ByVal VarSteps As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFatigueEvent
Dim NCount As System.Integer
Dim VarStudyNames As System.Object
Dim VarScales As System.Object
Dim VarSteps As System.Object
Dim value As System.Integer

value = instance.SetStudyAssociationData(NCount, VarStudyNames, VarScales, VarSteps)
```

### C#

```csharp
System.int SetStudyAssociationData(
   System.int NCount,
   System.object VarStudyNames,
   System.object VarScales,
   System.object VarSteps
)
```

### C++/CLI

```cpp
System.int SetStudyAssociationData(
   System.int NCount,
   System.Object^ VarStudyNames,
   System.Object^ VarScales,
   System.Object^ VarSteps
)
```

### Parameters

- `NCount`: Number of study associations
- `VarStudyNames`: Array of reference study names
- `VarScales`: Array of scale factors to apply to the scaled loads of studies in VarStudyNames to calculate the alternating stresses; valid only if VarStudyNames contains the names of linear studies
- `VarSteps`: Array of solution steps whose stress results are used to calculate the alternating stresses; valid only if VarStudyNames contains the names of nonlinear or linear dynamic studies

### Return Value

Error code as defined in [swsFatigueEventEndEditError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFatigueEventEndEditError_e.html)

## VBA Syntax

See [CWFatigueEvent::SetStudyAssociationData](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFatigueEvent~SetStudyAssociationData.html).

## Examples

See the [ICWFatigueEvent](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent.html) examples.

## See Also

[ICWFatigueEvent Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent.html)
[ICWFatigueEvent Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent_members.html)
[ICWFatigueEvent::GetStudyAssociationData Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent~GetStudyAssociationData.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0

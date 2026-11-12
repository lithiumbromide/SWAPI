---
title: "GetStudyAssociationData Method (ICWFatigueEvent)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFatigueEvent"
member: "GetStudyAssociationData"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent~GetStudyAssociationData.html"
---

# GetStudyAssociationData Method (ICWFatigueEvent)

Gets the study association data for this fatigue event.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetStudyAssociationData( _
   ByRef VarStudyNames As System.Object, _
   ByRef VarScales As System.Object, _
   ByRef VarSteps As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFatigueEvent
Dim VarStudyNames As System.Object
Dim VarScales As System.Object
Dim VarSteps As System.Object
Dim value As System.Integer

value = instance.GetStudyAssociationData(VarStudyNames, VarScales, VarSteps)
```

### C#

```csharp
System.int GetStudyAssociationData(
   out System.object VarStudyNames,
   out System.object VarScales,
   out System.object VarSteps
)
```

### C++/CLI

```cpp
System.int GetStudyAssociationData(
   [Out] System.Object^ VarStudyNames,
   [Out] System.Object^ VarScales,
   [Out] System.Object^ VarSteps
)
```

### Parameters

- `VarStudyNames`: Array of reference study names
- `VarScales`: Array of scale factors to apply to the scaled loads of studies in VarStudyNames to calculate the alternating stresses; valid only if VarStudyNames contains the names of linear studies
- `VarSteps`: Array of solution steps whose stress results are used to calculate the alternating stresses; valid only if VarStudyNames contains the names of nonlinear or linear dynamic studies

### Return Value

Number of study associations

## VBA Syntax

See [CWFatigueEvent::GetStudyAssociationData](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFatigueEvent~GetStudyAssociationData.html).

## Examples

See the [ICWFatigueEvent](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent.html) examples.

## See Also

[ICWFatigueEvent Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent.html)
[ICWFatigueEvent Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent_members.html)
[ICWFatigueEvent::SetStudyAssociationData Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueEvent~SetStudyAssociationData.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0

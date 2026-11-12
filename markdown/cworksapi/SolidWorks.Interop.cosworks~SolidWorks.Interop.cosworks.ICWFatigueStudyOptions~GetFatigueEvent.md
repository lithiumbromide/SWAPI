---
title: "GetFatigueEvent Method (ICWFatigueStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFatigueStudyOptions"
member: "GetFatigueEvent"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~GetFatigueEvent.html"
---

# GetFatigueEvent Method (ICWFatigueStudyOptions)

Gets the specified fatigue event.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFatigueEvent( _
   ByVal NIndex As System.Integer, _
   ByRef ErrorCode As System.Integer _
) As CWFatigueEvent
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFatigueStudyOptions
Dim NIndex As System.Integer
Dim ErrorCode As System.Integer
Dim value As CWFatigueEvent

value = instance.GetFatigueEvent(NIndex, ErrorCode)
```

### C#

```csharp
CWFatigueEvent GetFatigueEvent(
   System.int NIndex,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWFatigueEvent^ GetFatigueEvent(
   System.int NIndex,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NIndex`: 0-based index of the fatigue event (see **Remarks**)
- `ErrorCode`: Error code as defined in [swsFatigueEventEndEditError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFatigueEventEndEditError_e.html)

### Return Value

[ICWFatigueEvent](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWFatigueEvent.html)

## VBA Syntax

See [CWFatigueStudyOptions::GetFatigueEvent](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFatigueStudyOptions~GetFatigueEvent.html).

## Examples

See the [ICWFatigueStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions.html) examples.

## Remarks

To populate NIndex, call [ICWFatigueStudyOptions::LoadingEventCount](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~LoadingEventCount.html).

## See Also

[ICWFatigueStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions.html)
[ICWFatigueStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0

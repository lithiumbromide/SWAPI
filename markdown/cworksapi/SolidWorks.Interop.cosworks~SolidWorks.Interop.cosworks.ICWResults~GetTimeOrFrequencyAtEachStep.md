---
title: "GetTimeOrFrequencyAtEachStep Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetTimeOrFrequencyAtEachStep"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetTimeOrFrequencyAtEachStep.html"
---

# GetTimeOrFrequencyAtEachStep Method (ICWResults)

Obsolete. Superseded by [ICWResults::GetTimeOrFrequencyAtEachStep2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetTimeOrFrequencyAtEachStep2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTimeOrFrequencyAtEachStep( _
   ByVal ForStressAndStrain As System.Integer, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim ForStressAndStrain As System.Integer
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetTimeOrFrequencyAtEachStep(ForStressAndStrain, ErrorCode)
```

### C#

```csharp
System.object GetTimeOrFrequencyAtEachStep(
   System.int ForStressAndStrain,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetTimeOrFrequencyAtEachStep(
   System.int ForStressAndStrain,
   [Out] System.int ErrorCode
)
```

### Parameters

- `ForStressAndStrain`: 1 for stress or strain results, 0 for other results
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

0-based array of:

- Times for time-domain studies

- or -

- Frequencies for frequency-domain studies

for all solution steps or mode shapes

## VBA Syntax

See [CWResults::GetTimeOrFrequencyAtEachStep](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetTimeOrFrequencyAtEachStep.html).

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0

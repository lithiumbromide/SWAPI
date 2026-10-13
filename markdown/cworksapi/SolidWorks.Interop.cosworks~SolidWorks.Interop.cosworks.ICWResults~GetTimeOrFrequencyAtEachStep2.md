---
title: "GetTimeOrFrequencyAtEachStep2 Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetTimeOrFrequencyAtEachStep2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetTimeOrFrequencyAtEachStep2.html"
---

# GetTimeOrFrequencyAtEachStep2 Method (ICWResults)

Gets the times or frequencies for all solution steps or mode shapes in these results.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTimeOrFrequencyAtEachStep2( _
   ByVal ForStressAndStrain As System.Boolean, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim ForStressAndStrain As System.Boolean
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetTimeOrFrequencyAtEachStep2(ForStressAndStrain, ErrorCode)
```

### C#

```csharp
System.object GetTimeOrFrequencyAtEachStep2(
   System.bool ForStressAndStrain,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetTimeOrFrequencyAtEachStep2(
   System.bool ForStressAndStrain,
   [Out] System.int ErrorCode
)
```

### Parameters

- `ForStressAndStrain`: -1 or true for stress or strain results, 0 or false for other results
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

0-based array of:

- Times for time-domain studies

- or -

- Frequencies for frequency-domain studies

for all solution steps or mode shapes

## Examples

[Get Frequencies in Mode Shape Plots (VBA)](Get_Frequencies_in_Mode_Shape_Plots_Example_VB.htm)
[Get Frequencies in Mode Shape Plots (VB.NET)](Get_Frequencies_in_Mode_Shape_Plots_Example_VBNET.htm)
[Get Frequencies in Mode Shape Plots (C#)](Get_Free_Body_Forces_and_Moments_Example_CSharp.htm)

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30

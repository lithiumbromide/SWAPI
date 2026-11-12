---
title: "GetResonantFrequencies Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetResonantFrequencies"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetResonantFrequencies.html"
---

# GetResonantFrequencies Method (ICWResults)

Gets the resonant frequency values.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetResonantFrequencies( _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetResonantFrequencies(ErrorCode)
```

### C#

```csharp
System.object GetResonantFrequencies(
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetResonantFrequencies(
   [Out] System.int ErrorCode
)
```

### Parameters

- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array of resonant frequencies containing groups of these results:

- Mode number
- Resonant frequency (rad/sec)
- Resonant frequency (Hertz)
- Resonant period (seconds)

## VBA Syntax

See [CWResults::GetResonantFrequencies](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetResonantFrequencies.html).

## Examples

[Create Frequency Study with Solid Mesh (C#)](Create_Frequency_Study_with_Solid_Mesh_Example_CSharp.htm)
[Create Frequency Study with Solid Mesh (VB.NET)](Create_Frequency_Study_with_Solid_Mesh_Example_VBNET.htm)
[Create Frequency Study with Solid Mesh (VBA)](Create_Frequency_Study_with_Solid_Mesh_Example_VB.htm)

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0

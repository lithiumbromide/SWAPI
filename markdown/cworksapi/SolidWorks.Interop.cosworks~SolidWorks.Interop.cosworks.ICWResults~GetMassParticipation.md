---
title: "GetMassParticipation Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetMassParticipation"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMassParticipation.html"
---

# GetMassParticipation Method (ICWResults)

Gets the mass participation factors in the X, Y, and Z directions for all modes.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMassParticipation( _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetMassParticipation(ErrorCode)
```

### C#

```csharp
System.object GetMassParticipation(
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetMassParticipation(
   [Out] System.int ErrorCode
)
```

### Parameters

- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array of mass participation factors (in X, Y, Z directions)

## VBA Syntax

See [CWResults::GetMassParticipation](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetMassParticipation.html).

## Examples

[Create Frequency Study with Solid Mesh (VBA)](Create_Frequency_Study_with_Solid_Mesh_Example_VB.htm)
[Create Frequency Study with Solid Mesh (VB.NET)](Create_Frequency_Study_with_Solid_Mesh_Example_VBNET.htm)
[Create Frequency Study with Solid Mesh (C#)](Create_Frequency_Study_with_Solid_Mesh_Example_CSharp.htm)

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0

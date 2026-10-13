---
title: "GetMinMaxFatigue Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetMinMaxFatigue"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxFatigue.html"
---

# GetMinMaxFatigue Method (ICWResults)

Gets the algebraic minimum and maximum for the specified fatigue component.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMinMaxFatigue( _
   ByVal NComponent As System.Integer, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim NComponent As System.Integer
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetMinMaxFatigue(NComponent, ErrorCode)
```

### C#

```csharp
System.object GetMinMaxFatigue(
   System.int NComponent,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetMinMaxFatigue(
   System.int NComponent,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NComponent`: Type of fatigue as defined in [swsFatigueComponent_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFatigueComponent_e.html)
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array (see **Remarks**)

## VBA Syntax

See [CWResults::GetMinMaxFatigue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetMinMaxFatigue.html).

## Examples

[Create Fatigue Study (C#)](Create_Fatigue_Study_Example_CSharp.htm)
[Create Fatigue Study (VB.NET)](Create_Fatigue_Study_Example_VBNET.htm)
[Create Fatigue Study (VBA)](Create_Fatigue_Study_Example_VB.htm)

## Remarks

This method returns the following array:

{`node_with_minimum_fatigue`, `minimum_fatigue`, `node_with_maximum_fatigue`, `maximum_fatigue`},

where the nodes are integers, and the fatigue values are floats.

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetFatigueForEntities Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetFatigueForEntities.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0

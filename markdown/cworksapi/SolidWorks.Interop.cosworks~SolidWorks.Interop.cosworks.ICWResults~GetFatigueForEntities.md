---
title: "GetFatigueForEntities Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetFatigueForEntities"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetFatigueForEntities.html"
---

# GetFatigueForEntities Method (ICWResults)

Gets the specified fatigue component for the specified entities.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFatigueForEntities( _
   ByVal NComponent As System.Integer, _
   ByVal ArraySelectedEntities As System.Object, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim NComponent As System.Integer
Dim ArraySelectedEntities As System.Object
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetFatigueForEntities(NComponent, ArraySelectedEntities, ErrorCode)
```

### C#

```csharp
System.object GetFatigueForEntities(
   System.int NComponent,
   System.object ArraySelectedEntities,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetFatigueForEntities(
   System.int NComponent,
   System.Object^ ArraySelectedEntities,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NComponent`: Fatigue component as defined in [swsFatigueComponent_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFatigueComponent_e.html)
- `ArraySelectedEntities`: Array of geometric entities
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array of fatigue component values

## VBA Syntax

See [CWResults::GetFatigueForEntities](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetFatigueForEntities.html).

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetMinMaxFatigue Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxFatigue.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0

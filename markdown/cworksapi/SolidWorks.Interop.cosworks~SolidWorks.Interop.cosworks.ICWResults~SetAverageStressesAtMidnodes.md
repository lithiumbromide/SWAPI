---
title: "SetAverageStressesAtMidnodes Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "SetAverageStressesAtMidnodes"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetAverageStressesAtMidnodes.html"
---

# SetAverageStressesAtMidnodes Method (ICWResults)

Sets whether to average stresses at mid-nodes for this study.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetAverageStressesAtMidnodes( _
   ByVal BValue As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim BValue As System.Boolean
Dim value As System.Boolean

value = instance.SetAverageStressesAtMidnodes(BValue)
```

### C#

```csharp
System.bool SetAverageStressesAtMidnodes(
   System.bool BValue
)
```

### C++/CLI

```cpp
System.bool SetAverageStressesAtMidnodes(
   System.bool BValue
)
```

### Parameters

- `BValue`: True to average stresses at mid-nodes, false to not

### Return Value

True if option successfully set, false if not

## VBA Syntax

See [CWResults::SetAverageStressesAtMidnodes](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~SetAverageStressesAtMidnodes.html).

## Remarks

This method is valid only for static, nonlinear, drop test, pressure vessel, and topology studies.

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetAverageStressesAtMidnodes Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetAverageStressesAtMidnodes.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0

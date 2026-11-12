---
title: "GetAverageStressesAtMidnodes Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetAverageStressesAtMidnodes"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetAverageStressesAtMidnodes.html"
---

# GetAverageStressesAtMidnodes Method (ICWResults)

Gets whether to average stress at mid-nodes in this study.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAverageStressesAtMidnodes() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim value As System.Boolean

value = instance.GetAverageStressesAtMidnodes()
```

### C#

```csharp
System.bool GetAverageStressesAtMidnodes()
```

### C++/CLI

```cpp
System.bool GetAverageStressesAtMidnodes();
```

### Return Value

True to average stresses at mid-nodes, false to not

## VBA Syntax

See [CWResults::GetAverageStressesAtMidnodes](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetAverageStressesAtMidnodes.html).

## Remarks

This method is valid only for static, nonlinear, drop test, pressure vessel, and topology studies.

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::SetAverageStressesAtMidnodes Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetAverageStressesAtMidnodes.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0

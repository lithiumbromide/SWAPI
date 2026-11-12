---
title: "SetBaseLine Method (ICWTrendTracker)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTrendTracker"
member: "SetBaseLine"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTrendTracker~SetBaseLine.html"
---

# SetBaseLine Method (ICWTrendTracker)

Sets the current results as the baseline for weight, displacement, stress, etc.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetBaseLine() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTrendTracker
Dim value As System.Integer

value = instance.SetBaseLine()
```

### C#

```csharp
System.int SetBaseLine()
```

### C++/CLI

```cpp
System.int SetBaseLine();
```

### Return Value

Error code as defined in [swsTrendTrackerErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTrendTrackerErrorCode_e.html)

## VBA Syntax

See [CWTrendTracker::SetBaseLine](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTrendTracker~SetBaseLine.html).

## Examples

See the [ICWTrendTracker](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTrendTracker.html) examples.

## See Also

[ICWTrendTracker Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTrendTracker.html)
[ICWTrendTracker Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTrendTracker_members.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0

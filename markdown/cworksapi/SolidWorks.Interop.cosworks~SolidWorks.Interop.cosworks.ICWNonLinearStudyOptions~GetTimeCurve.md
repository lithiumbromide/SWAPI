---
title: "GetTimeCurve Method (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "GetTimeCurve"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~GetTimeCurve.html"
---

# GetTimeCurve Method (ICWNonLinearStudyOptions)

Gets the time curve data.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTimeCurve() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
Dim value As System.Object

value = instance.GetTimeCurve()
```

### C#

```csharp
System.object GetTimeCurve()
```

### C++/CLI

```cpp
System.Object^ GetTimeCurve();
```

### Return Value

Array of curve data (see **Remarks**)

## VBA Syntax

See [CWNonLinearStudyOptions::GetTimeCurve](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~GetTimeCurve.html).

## Remarks

Array of time curve data:

**[** `n, x1, y1, x2, y2, x3, y3,...xn, yn` **]**

where:

- n = number of pairs of data points
- xi = time value at the `ith` data point
- yi = property value associated with time xi

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)
[ICWNonLinearStudyOptions::SetTimeCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~SetTimeCurve.html)

## Availability

SOLIDWORKS Simulation 2010 SP3.0

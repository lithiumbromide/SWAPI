---
title: "GetTimeCurve Method (ICWRestraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRestraint"
member: "GetTimeCurve"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~GetTimeCurve.html"
---

# GetTimeCurve Method (ICWRestraint)

Gets the time curve data for this restraint.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTimeCurve() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRestraint
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

Array of time curve data (see **Remarks**)

## VBA Syntax

See [CWRestraint::GetTimeCurve](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRestraint~GetTimeCurve.html).

## Remarks

This method is valid only for nonlinear studies and if [ICWRestraint::RestraintType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~RestraintType.html) is not set to:

- [swsRestraintType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRestraintType_e.html).swsRestraintTypeFixed,
- swsRestraintType_e.swsRestraintTypeImmovable, or
- swsRestraintType_e.swsRestraintTypeSymmetric.

Array of time curve data:

**[** `n, x1, y1, x2, y2, x3, y3,...xn, yn` **]**

where:

- n = number of pairs of data points
- xi = time value at the `ith` data point
- yi = property value associated with time xi

Time curves are used to specify feature variation with respect to time in transient studies.

## See Also

[ICWRestraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint.html)
[ICWRestraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint_members.html)
[ICWRestraint::SetTimeCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~SetTimeCurve.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0

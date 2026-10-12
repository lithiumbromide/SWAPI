---
title: "AllowShaftByBearingRatioGreaterThan2 Property (ICWBearingConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBearingConnector"
member: "AllowShaftByBearingRatioGreaterThan2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~AllowShaftByBearingRatioGreaterThan2.html"
---

# AllowShaftByBearingRatioGreaterThan2 Property (ICWBearingConnector)

Sets whether to allow (shaft length)/(bearing length) > 2.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property AllowShaftByBearingRatioGreaterThan2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBearingConnector

instance.AllowShaftByBearingRatioGreaterThan2 = value
```

### C#

```csharp
System.bool AllowShaftByBearingRatioGreaterThan2 {set;}
```

### C++/CLI

```cpp
property System.bool AllowShaftByBearingRatioGreaterThan2 {
   void set (    System.bool value);
}
```

### Property Value

True to allow (shaft length)/(bearing length) > 2, false to not

## VBA Syntax

See [CWBearingConnector::AllowShaftByBearingRatioGreaterThan2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBearingConnector~AllowShaftByBearingRatioGreaterThan2.html).

## Remarks

[ICWBearingConnector::PerformAdvanceValidations](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~PerformAdvanceValidations.html) calculates this ratio and returns an error code if it is greater than two and this property is set to false.

## See Also

[ICWBearingConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector.html)
[ICWBearingConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2024 SP0

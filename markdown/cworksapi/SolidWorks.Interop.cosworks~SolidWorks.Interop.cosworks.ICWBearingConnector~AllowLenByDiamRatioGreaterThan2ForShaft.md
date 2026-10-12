---
title: "AllowLenByDiamRatioGreaterThan2ForShaft Property (ICWBearingConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBearingConnector"
member: "AllowLenByDiamRatioGreaterThan2ForShaft"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~AllowLenByDiamRatioGreaterThan2ForShaft.html"
---

# AllowLenByDiamRatioGreaterThan2ForShaft Property (ICWBearingConnector)

Sets whether to allow (shaft length)/(shaft diameter) > 2.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property AllowLenByDiamRatioGreaterThan2ForShaft As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBearingConnector

instance.AllowLenByDiamRatioGreaterThan2ForShaft = value
```

### C#

```csharp
System.bool AllowLenByDiamRatioGreaterThan2ForShaft {set;}
```

### C++/CLI

```cpp
property System.bool AllowLenByDiamRatioGreaterThan2ForShaft {
   void set (    System.bool value);
}
```

### Property Value

True to allow (shaft length)/(diameter) greater than > 2, false to not

## VBA Syntax

See [CWBearingConnector::AllowLenByDiamRatioGreaterThan2ForShaft](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBearingConnector~AllowLenByDiamRatioGreaterThan2ForShaft.html).

## Remarks

[ICWBearingConnector::PerformAdvanceValidations](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~PerformAdvanceValidations.html) calculates this ratio and returns an error code if it cannot be greater than two and this property is set to false.

## See Also

[ICWBearingConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector.html)
[ICWBearingConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2024 SP0

---
title: "IncludeKnownTensileStressArea Property (ICWBoltConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBoltConnector"
member: "IncludeKnownTensileStressArea"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~IncludeKnownTensileStressArea.html"
---

# IncludeKnownTensileStressArea Property (ICWBoltConnector)

Gets or sets whether to include known tensile stress area.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeKnownTensileStressArea As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBoltConnector
Dim value As System.Boolean

instance.IncludeKnownTensileStressArea = value

value = instance.IncludeKnownTensileStressArea
```

### C#

```csharp
System.bool IncludeKnownTensileStressArea {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeKnownTensileStressArea {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to include known tensile stress area, false to include calculated tensile stress area

## VBA Syntax

See [CWBoltConnector::IncludeKnownTensileStressArea](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBoltConnector~IncludeKnownTensileStressArea.html).

## See Also

[ICWBoltConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector.html)
[ICWBoltConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector_members.html)
[ICWBoltConnector::GetStrengthData Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~GetStrengthData.html)
[ICWBoltConnector::SetStrengthData Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~SetStrengthData.html)
[ICWBoltConnector::IncludeStrengthData Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~IncludeStrengthData.html)
[ICWBoltConnector::PinBoltStrengthUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~PinBoltStrengthUnit.html)
[ICWBoltConnector::TensileStressAreaUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~TensileStressAreaUnit.html)
[ICWBoltConnector::BoltUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~BoltUnit.html)
[ICWBoltConnector::ThreadsPerLengthUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~ThreadsPerLengthUnit.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0

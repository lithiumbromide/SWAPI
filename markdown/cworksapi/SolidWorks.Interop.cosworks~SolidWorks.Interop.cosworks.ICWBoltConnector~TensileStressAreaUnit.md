---
title: "TensileStressAreaUnit Property (ICWBoltConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBoltConnector"
member: "TensileStressAreaUnit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~TensileStressAreaUnit.html"
---

# TensileStressAreaUnit Property (ICWBoltConnector)

Gets or sets the unit of the tensile stress area.

## Syntax

### Visual Basic (Declaration)

```vb
Property TensileStressAreaUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBoltConnector
Dim value As System.Integer

instance.TensileStressAreaUnit = value

value = instance.TensileStressAreaUnit
```

### C#

```csharp
System.int TensileStressAreaUnit {get; set;}
```

### C++/CLI

```cpp
property System.int TensileStressAreaUnit {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Tensile stress area unit as defined in [swsTensileStressAreaUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsTensileStressAreaUnit_e.html)

## VBA Syntax

See [CWBoltConnector::TensileStressAreaUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBoltConnector~TensileStressAreaUnit.html).

## See Also

[ICWBoltConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector.html)
[ICWBoltConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector_members.html)
[ICWBoltConnector::GetStrengthData Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~GetStrengthData.html)
[ICWBoltConnector::SetStrengthData Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~SetStrengthData.html)
[ICWBoltConnector::BoltUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~BoltUnit.html)
[ICWBoltConnector::IncludeKnownTensileStressArea Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~IncludeKnownTensileStressArea.html)
[ICWBoltConnector::IncludeStrengthData Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~IncludeStrengthData.html)
[ICWBoltConnector::ThreadsPerLengthUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~ThreadsPerLengthUnit.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0

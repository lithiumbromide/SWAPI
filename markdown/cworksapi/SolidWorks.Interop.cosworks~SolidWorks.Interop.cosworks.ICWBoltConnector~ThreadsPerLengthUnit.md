---
title: "ThreadsPerLengthUnit Property (ICWBoltConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBoltConnector"
member: "ThreadsPerLengthUnit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~ThreadsPerLengthUnit.html"
---

# ThreadsPerLengthUnit Property (ICWBoltConnector)

Gets or sets the threads/length unit.

## Syntax

### Visual Basic (Declaration)

```vb
Property ThreadsPerLengthUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBoltConnector
Dim value As System.Integer

instance.ThreadsPerLengthUnit = value

value = instance.ThreadsPerLengthUnit
```

### C#

```csharp
System.int ThreadsPerLengthUnit {get; set;}
```

### C++/CLI

```cpp
property System.int ThreadsPerLengthUnit {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Threads/length unit as defined in [swsThreadsPerLengthUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsThreadsPerLengthUnit_e.html)

## VBA Syntax

See [CWBoltConnector::ThreadsPerLengthUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBoltConnector~ThreadsPerLengthUnit.html).

## See Also

[ICWBoltConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector.html)
[ICWBoltConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector_members.html)
[ICWBoltConnector::GetStrengthData Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~GetStrengthData.html)
[ICWBoltConnector::SetStrengthData Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~SetStrengthData.html)
[ICWBoltConnector::BoltUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~BoltUnit.html)
[ICWBoltConnector::IncludeKnownTensileStressArea Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~IncludeKnownTensileStressArea.html)
[ICWBoltConnector::IncludeStrengthData Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~IncludeStrengthData.html)
[ICWBoltConnector::TensileStressAreaUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~TensileStressAreaUnit.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0

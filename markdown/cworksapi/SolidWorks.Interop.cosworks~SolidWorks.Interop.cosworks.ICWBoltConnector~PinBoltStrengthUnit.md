---
title: "PinBoltStrengthUnit Property (ICWBoltConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBoltConnector"
member: "PinBoltStrengthUnit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~PinBoltStrengthUnit.html"
---

# PinBoltStrengthUnit Property (ICWBoltConnector)

Gets or sets the strength of the bolt.

## Syntax

### Visual Basic (Declaration)

```vb
Property PinBoltStrengthUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBoltConnector
Dim value As System.Integer

instance.PinBoltStrengthUnit = value

value = instance.PinBoltStrengthUnit
```

### C#

```csharp
System.int PinBoltStrengthUnit {get; set;}
```

### C++/CLI

```cpp
property System.int PinBoltStrengthUnit {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Strength of bolt

## VBA Syntax

See [CWBoltConnector::PinBoltStrengthUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBoltConnector~PinBoltStrengthUnit.html).

## See Also

[ICWBoltConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector.html)
[ICWBoltConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector_members.html)
[ICWBoltConnector::ICWBoltConnector::GetStrengthData Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~GetStrengthData.html)
[ICWBoltConnector::SetStrengthData Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~SetStrengthData.html)
[ICWBoltConnector::BoltUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~BoltUnit.html)
[ICWBoltConnector::IncludeKnownTensileStressArea Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~IncludeKnownTensileStressArea.html)
[ICWBoltConnector::IncludeStrengthData Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~IncludeStrengthData.html)
[ICWBoltConnector::TensileStressAreaUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~TensileStressAreaUnit.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0

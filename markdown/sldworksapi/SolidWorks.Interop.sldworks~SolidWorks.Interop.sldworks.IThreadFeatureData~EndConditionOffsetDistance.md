---
title: "EndConditionOffsetDistance Property (IThreadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IThreadFeatureData"
member: "EndConditionOffsetDistance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~EndConditionOffsetDistance.html"
---

# EndConditionOffsetDistance Property (IThreadFeatureData)

Gets or sets the end condition offset distance of this thread feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property EndConditionOffsetDistance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IThreadFeatureData
Dim value As System.Double

instance.EndConditionOffsetDistance = value

value = instance.EndConditionOffsetDistance
```

### C#

```csharp
System.double EndConditionOffsetDistance {get; set;}
```

### C++/CLI

```cpp
property System.double EndConditionOffsetDistance {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0.0 (default) < End condition offset distance

## VBA Syntax

See [ThreadFeatureData::EndConditionOffsetDistance](ms-its:sldworksapivb6.chm::/sldworks~ThreadFeatureData~EndConditionOffsetDistance.html).

## Examples

See the [IThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html) examples.

## Remarks

This property is valid only if:

- [IThreadFeatureData::EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~EndCondition.html) is set to [swThreadEndCondition_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swThreadEndCondition_e.html).swThreadEndCondition_UpToSelection.

- and -

- [IThreadFeatureData::EndConditionOffset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~EndConditionOffset.html) is set to true.

## See Also

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html)
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0

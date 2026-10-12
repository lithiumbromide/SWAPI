---
title: "EngageBelt Property (IBeltChainFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBeltChainFeatureData"
member: "EngageBelt"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~EngageBelt.html"
---

# EngageBelt Property (IBeltChainFeatureData)

Gets and sets whether to engage the belt with the pulleys.

## Syntax

### Visual Basic (Declaration)

```vb
Property EngageBelt As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBeltChainFeatureData
Dim value As System.Boolean

instance.EngageBelt = value

value = instance.EngageBelt
```

### C#

```csharp
System.bool EngageBelt {get; set;}
```

### C++/CLI

```cpp
property System.bool EngageBelt {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to engage the belt with the pulleys, false to suppress belt mates

## VBA Syntax

See [BeltChainFeatureData::EngageBelt](ms-its:sldworksapivb6.chm::/sldworks~BeltChainFeatureData~EngageBelt.html).

## Examples

See the [IBeltChainFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.html) examples.

## See Also

[IBeltChainFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.html)
[IBeltChainFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30

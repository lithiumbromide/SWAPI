---
title: "SingleDirection Property (ISplitLineFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISplitLineFeatureData"
member: "SingleDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~SingleDirection.html"
---

# SingleDirection Property (ISplitLineFeatureData)

Gets or sets whether the projection split line is in a single direction.

## Syntax

### Visual Basic (Declaration)

```vb
Property SingleDirection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISplitLineFeatureData
Dim value As System.Boolean

instance.SingleDirection = value

value = instance.SingleDirection
```

### C#

```csharp
System.bool SingleDirection {get; set;}
```

### C++/CLI

```cpp
property System.bool SingleDirection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if single direction, false if not

## VBA Syntax

See [SplitLineFeatureData::SingleDirection](ms-its:sldworksapivb6.chm::/sldworks~SplitLineFeatureData~SingleDirection.html).

## Examples

See the [ISplitLineFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData.html) examples.

## Remarks

This property is valid only if [ISplitLineFeatureData::GetType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplitLineFeatureData~GetType.html) is set to [swSplitLineFeatureType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSplitLineFeatureType_e.html).swSplitLineFeatureType_Projection.

## See Also

[ISplitLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData.html)
[ISplitLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData_members.html)
[ISplitLineFeatureData::PullDirectionBase Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~PullDirectionBase.html)
[ISplitLineFeatureData::PullDirectionType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~PullDirectionType.html)
[ISplitLineFeatureData::ReverseDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~ReverseDirection.html)
[ISplitLineFeatureData::SplitType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~SplitType.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0

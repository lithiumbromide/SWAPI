---
title: "PullDirectionBase Property (ISplitLineFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISplitLineFeatureData"
member: "PullDirectionBase"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~PullDirectionBase.html"
---

# PullDirectionBase Property (ISplitLineFeatureData)

Gets or sets the entity indicating the direction of pull of this split line feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PullDirectionBase As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISplitLineFeatureData
Dim value As System.Object

instance.PullDirectionBase = value

value = instance.PullDirectionBase
```

### C#

```csharp
System.object PullDirectionBase {get; set;}
```

### C++/CLI

```cpp
property System.Object^ PullDirectionBase {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Entity indicating the direction of pull: [axis](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefAxis.html), [edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html), [face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html), or [plane](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlane.html)

## VBA Syntax

See [SplitLineFeatureData::PullDirectionBase](ms-its:sldworksapivb6.chm::/sldworks~SplitLineFeatureData~PullDirectionBase.html).

## Remarks

This property is only valid when [ISplitLineFeatureData::GetType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplitLineFeatureData~GetType.html) is set to [swSplitLineFeatureType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSplitLineFeatureType_e.html).swSplitLineFeatureType_Draft.

After calling this property, call [ISplitLineFeatureData::PullDirectionType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplitLineFeatureData~PullDirectionType.html) to determine the type of entity.

## See Also

[ISplitLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData.html)
[ISplitLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData_members.html)
[ISplitLineFeatureData::ReverseDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~ReverseDirection.html)
[ISplitLineFeatureData::SingleDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~SingleDirection.html)
[ISplitLineFeatureData::SplitType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~SplitType.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0

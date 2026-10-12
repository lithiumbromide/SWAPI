---
title: "PullDirectionType Property (ISplitLineFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISplitLineFeatureData"
member: "PullDirectionType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~PullDirectionType.html"
---

# PullDirectionType Property (ISplitLineFeatureData)

Gets the type of entity indicating the direction of pull for this split line feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property PullDirectionType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISplitLineFeatureData
Dim value As System.Integer

value = instance.PullDirectionType
```

### C#

```csharp
System.int PullDirectionType {get;}
```

### C++/CLI

```cpp
property System.int PullDirectionType {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of entity as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html):

- swSelDATUMAXES
- swSelEDGES
- swSelFACES
- swSelDATUMPLANES
- swSelDATUMPOINT
- swSelVERTICES

## VBA Syntax

See [SplitLineFeatureData::PullDirectionType](ms-its:sldworksapivb6.chm::/sldworks~SplitLineFeatureData~PullDirectionType.html).

## Remarks

Before calling this property, call [ISplitLineFeatureData::PullDirectionBase](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplitLineFeatureData~PullDirectionBase.html) to get the entity that indicates the pull direction.

## See Also

[ISplitLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData.html)
[ISplitLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData_members.html)
[ISplitLineFeatureData::ReverseDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~ReverseDirection.html)
[ISplitLineFeatureData::SingleDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~SingleDirection.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0

---
title: "PullDirectionType Property (IPartingSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPartingSurfaceFeatureData"
member: "PullDirectionType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData~PullDirectionType.html"
---

# PullDirectionType Property (IPartingSurfaceFeatureData)

Gets the type of entity that specifies the direction of pull for this parting surface feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property PullDirectionType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPartingSurfaceFeatureData
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

Type of entity that represents the direction of pull as defined by [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html):

- swSelEDGES
- swSelDATUMAXES
- swSelDATUMPLANES
- swSelFaCES

## VBA Syntax

See [PartingSurfaceFeatureData::PullDirectionType](ms-its:sldworksapivb6.chm::/sldworks~PartingSurfaceFeatureData~PullDirectionType.html).

## See Also

[IPartingSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData.html)
[IPartingSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData_members.html)
[IPartingSurfaceFeatureData::PullDirectionBase Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData~PullDirectionBase.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0

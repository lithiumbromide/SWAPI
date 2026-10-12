---
title: "SweepType Property (ISweepFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweepFeatureData"
member: "SweepType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~SweepType.html"
---

# SweepType Property (ISweepFeatureData)

Gets the type of this sweep feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property SweepType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISweepFeatureData
Dim value As System.Integer

value = instance.SweepType
```

### C#

```csharp
System.int SweepType {get;}
```

### C++/CLI

```cpp
property System.int SweepType {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Sweep type as defined in [swFeatureNameID_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFeatureNameID_e.html):

- swFmSweep (swept boss)
- swFmSweepCut (swept cut)
- swRefSurface (swept surface)

## VBA Syntax

See [SweepFeatureData::SweepType](ms-its:sldworksapivb6.chm::/sldworks~SweepFeatureData~SweepType.html).

## See Also

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html)
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0

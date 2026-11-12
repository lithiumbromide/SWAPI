---
title: "MergeFace Property (IFlatPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFlatPatternFeatureData"
member: "MergeFace"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~MergeFace.html"
---

# MergeFace Property (IFlatPatternFeatureData)

Gets or sets whether to merge the faces that are planar and coincident in the Flat-Pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property MergeFace As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFlatPatternFeatureData
Dim value As System.Boolean

instance.MergeFace = value

value = instance.MergeFace
```

### C#

```csharp
System.bool MergeFace {get; set;}
```

### C++/CLI

```cpp
property System.bool MergeFace {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True merges the faces, false does not

## VBA Syntax

See [FlatPatternFeatureData::MergeFace](ms-its:sldworksapivb6.chm::/sldworks~FlatPatternFeatureData~MergeFace.html).

## See Also

[IFlatPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData.html)
[IFlatPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2

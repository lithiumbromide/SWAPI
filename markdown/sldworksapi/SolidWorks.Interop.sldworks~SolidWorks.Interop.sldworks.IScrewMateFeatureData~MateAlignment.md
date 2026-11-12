---
title: "MateAlignment Property (IScrewMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IScrewMateFeatureData"
member: "MateAlignment"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScrewMateFeatureData~MateAlignment.html"
---

# MateAlignment Property (IScrewMateFeatureData)

Gets or sets the alignment of this screw mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property MateAlignment As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IScrewMateFeatureData
Dim value As System.Integer

instance.MateAlignment = value

value = instance.MateAlignment
```

### C#

```csharp
System.int MateAlignment {get; set;}
```

### C++/CLI

```cpp
property System.int MateAlignment {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Mate alignment as defined in [swMateAlign_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMateAlign_e.html)

## VBA Syntax

See [ScrewMateFeatureData::MateAlignment](ms-its:sldworksapivb6.chm::/sldworks~ScrewMateFeatureData~MateAlignment.html).

## See Also

[IScrewMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScrewMateFeatureData.html)
[IScrewMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScrewMateFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0

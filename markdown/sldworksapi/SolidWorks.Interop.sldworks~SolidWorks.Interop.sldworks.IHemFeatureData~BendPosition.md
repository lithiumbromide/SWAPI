---
title: "BendPosition Property (IHemFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHemFeatureData"
member: "BendPosition"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData~BendPosition.html"
---

# BendPosition Property (IHemFeatureData)

Gets or sets the bend position.

## Syntax

### Visual Basic (Declaration)

```vb
Property BendPosition As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IHemFeatureData
Dim value As System.Integer

instance.BendPosition = value

value = instance.BendPosition
```

### C#

```csharp
System.int BendPosition {get; set;}
```

### C++/CLI

```cpp
property System.int BendPosition {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Position as defined in [swHemPositionTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swHemPositionTypes_e.html)

## VBA Syntax

See [HemFeatureData::BendPosition](ms-its:sldworksapivb6.chm::/sldworks~HemFeatureData~BendPosition.html).

## See Also

[IHemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData.html)
[IHemFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1

---
title: "SimplifyBends Property (IFlatPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFlatPatternFeatureData"
member: "SimplifyBends"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~SimplifyBends.html"
---

# SimplifyBends Property (IFlatPatternFeatureData)

Gets or sets whether to simplify bends in this Flat-Pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property SimplifyBends As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFlatPatternFeatureData
Dim value As System.Boolean

instance.SimplifyBends = value

value = instance.SimplifyBends
```

### C#

```csharp
System.bool SimplifyBends {get; set;}
```

### C++/CLI

```cpp
property System.bool SimplifyBends {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to simplify edges to lines, false to leave edges complex

## VBA Syntax

See [FlatPatternFeatureData::SimplifyBends](ms-its:sldworksapivb6.chm::/sldworks~FlatPatternFeatureData~SimplifyBends.html).

## Remarks

This property corresponds to the Simplify bends check box on the Parameters group box on the Flat Pattern PropertyManager, which is displayed when you edit the definition of a flat-pattern feature with complex bends in SOLIDWORKS.

## See Also

[IFlatPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData.html)
[IFlatPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0

---
title: "SymmetricThickness Property (ILoftedBendsFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILoftedBendsFeatureData"
member: "SymmetricThickness"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~SymmetricThickness.html"
---

# SymmetricThickness Property (ILoftedBendsFeatureData)

Gets or sets whether to symmetrically thicken this bi-directional lofted bends feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property SymmetricThickness As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILoftedBendsFeatureData
Dim value As System.Boolean

instance.SymmetricThickness = value

value = instance.SymmetricThickness
```

### C#

```csharp
System.bool SymmetricThickness {get; set;}
```

### C++/CLI

```cpp
property System.bool SymmetricThickness {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to thicken symmetrically, false to not

## VBA Syntax

See [LoftedBendsFeatureData::SymmetricThickness](ms-its:sldworksapivb6.chm::/sldworks~LoftedBendsFeatureData~SymmetricThickness.html).

## See Also

[ILoftedBendsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData.html)
[ILoftedBendsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31

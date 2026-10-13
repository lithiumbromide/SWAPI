---
title: "Diameter Property (ISimpleHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleHoleFeatureData2"
member: "Diameter"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~Diameter.html"
---

# Diameter Property (ISimpleHoleFeatureData2)

Gets or sets the diameter of this simple hole feature

## Syntax

### Visual Basic (Declaration)

```vb
Property Diameter As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleHoleFeatureData2
Dim value As System.Double

instance.Diameter = value

value = instance.Diameter
```

### C#

```csharp
System.double Diameter {get; set;}
```

### C++/CLI

```cpp
property System.double Diameter {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Hole diameter

## VBA Syntax

See [SimpleHoleFeatureData2::Diameter](ms-its:sldworksapivb6.chm::/sldworks~SimpleHoleFeatureData2~Diameter.html).

## See Also

[ISimpleHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2.html)
[ISimpleHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

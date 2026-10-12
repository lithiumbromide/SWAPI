---
title: "Diameter Property (IThreadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IThreadFeatureData"
member: "Diameter"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~Diameter.html"
---

# Diameter Property (IThreadFeatureData)

Gets or sets the diameter of the cylindrical face or helix of this thread feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Diameter As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IThreadFeatureData
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

0.0 < Diameter of the helix; default is the diameter of the circular edge specified by [IThreadFeatureData::Edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~Edge.html)

## VBA Syntax

See [ThreadFeatureData::Diameter](ms-its:sldworksapivb6.chm::/sldworks~ThreadFeatureData~Diameter.html).

## Examples

See the [IThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html) examples.

## Remarks

Specify either a value or an equation that starts with an equal sign (=).

This property is valid only if [IThreadFeatureData::DiameterOverride](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~DiameterOverride.html) is set to true.

## See Also

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html)
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0

---
title: "Diameter Property (ICosmeticThreadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICosmeticThreadFeatureData"
member: "Diameter"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData~Diameter.html"
---

# Diameter Property (ICosmeticThreadFeatureData)

Gets or sets the value of the diameter of the cosmetic thread.

## Syntax

### Visual Basic (Declaration)

```vb
Property Diameter As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmeticThreadFeatureData
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

Depth of the diameter (see **Remarks**)

## VBA Syntax

See [CosmeticThreadFeatureData::Diameter](ms-its:sldworksapivb6.chm::/sldworks~CosmeticThreadFeatureData~Diameter.html).

## Examples

See the [ICosmeticThreadFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticThreadFeatureData.html) examples.

## Remarks

| If ICosmeticThreadFeatureData::DiameterType ... | Then the value of Diameter is the... |
| --- | --- |
| swCosmeticThread_MajorDiameter - or - swCosmeticThread_MinorDiameter | Diameter of the cosmetic thread |
| swCosmeticThread_ConicalOffset | Offset of the cosmetic thread from the edge of the conical hole |

## See Also

[ICosmeticThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData.html)
[ICosmeticThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData_members.html)
[ICosmeticThreadFeatureData::DiameterType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData~DiameterType.html)

## Availability

SOLIDWORKS 2003 SP1, Revision Number 11.1

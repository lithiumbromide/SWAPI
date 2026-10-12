---
title: "DepthDistance Property (IEndCapFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IEndCapFeatureData"
member: "DepthDistance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData~DepthDistance.html"
---

# DepthDistance Property (IEndCapFeatureData)

Gets or sets the depth distance for this end cap feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property DepthDistance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IEndCapFeatureData
Dim value As System.Double

instance.DepthDistance = value

value = instance.DepthDistance
```

### C#

```csharp
System.double DepthDistance {get; set;}
```

### C++/CLI

```cpp
property System.double DepthDistance {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Depth distance

## VBA Syntax

See [EndCapFeatureData::DepthDistance](ms-its:sldworksapivb6.chm::/sldworks~EndCapFeatureData~DepthDistance.html).

## Examples

See the [IEndCapFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEndCapFeatureData.html) examples.

## See Also

[IEndCapFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData.html)
[IEndCapFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0

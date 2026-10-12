---
title: "DefaultDistance Property (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "DefaultDistance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~DefaultDistance.html"
---

# DefaultDistance Property (ISimpleFilletFeatureData2)

Gets or sets the default Distance 2 radius of this asymmetric fillet.

## Syntax

### Visual Basic (Declaration)

```vb
Property DefaultDistance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
Dim value As System.Double

instance.DefaultDistance = value

value = instance.DefaultDistance
```

### C#

```csharp
System.double DefaultDistance {get; set;}
```

### C++/CLI

```cpp
property System.double DefaultDistance {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Default Distance 2 radius of this asymmetric fillet

## VBA Syntax

See [SimpleFilletFeatureData2::DefaultDistance](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData2~DefaultDistance.html).

## Examples

See the [ISimpleFilletFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html) introductory example.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)
[ISimpleFilletFeatureData2::AsymmetricFillet Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~AsymmetricFillet.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0

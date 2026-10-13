---
title: "AsymmetricFillet Property (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "AsymmetricFillet"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~AsymmetricFillet.html"
---

# AsymmetricFillet Property (ISimpleFilletFeatureData2)

Gets or sets whether this simple fillet/chamfer is asymmetric.

## Syntax

### Visual Basic (Declaration)

```vb
Property AsymmetricFillet As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
Dim value As System.Boolean

instance.AsymmetricFillet = value

value = instance.AsymmetricFillet
```

### C#

```csharp
System.bool AsymmetricFillet {get; set;}
```

### C++/CLI

```cpp
property System.bool AsymmetricFillet {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if an asymmetric fillet/chamfer, false if a symmetric fillet/chamfer

## VBA Syntax

See [SimpleFilletFeatureData2::AsymmetricFillet](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData2~AsymmetricFillet.html).

## Examples

See the [ISimpleFilletFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html) introductory example.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0

---
title: "AsymmetricFillet Property (IVariableFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IVariableFilletFeatureData2"
member: "AsymmetricFillet"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~AsymmetricFillet.html"
---

# AsymmetricFillet Property (IVariableFilletFeatureData2)

Gets or sets whether this variable radius fillet is asymmetric.

## Syntax

### Visual Basic (Declaration)

```vb
Property AsymmetricFillet As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IVariableFilletFeatureData2
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

True if an asymmetric fillet, false if a symmetric fillet

## VBA Syntax

See [VariableFilletFeatureData2::AsymmetricFillet](ms-its:sldworksapivb6.chm::/sldworks~VariableFilletFeatureData2~AsymmetricFillet.html).

## Examples

See the [IVariableFilletFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVariableFilletFeatureData2.html) examples.

## Remarks

See [Accessing Selections that Define Features](sldworksapiprogguide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html)
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0

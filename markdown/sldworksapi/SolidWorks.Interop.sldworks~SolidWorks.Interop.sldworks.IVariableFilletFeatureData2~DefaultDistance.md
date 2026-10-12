---
title: "DefaultDistance Property (IVariableFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IVariableFilletFeatureData2"
member: "DefaultDistance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~DefaultDistance.html"
---

# DefaultDistance Property (IVariableFilletFeatureData2)

Gets or sets the default Distance 2 radius of this asymmetric fillet.

## Syntax

### Visual Basic (Declaration)

```vb
Property DefaultDistance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IVariableFilletFeatureData2
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

Default distance 2 radius of this asymmetric fillet

## VBA Syntax

See [VariableFilletFeatureData2::DefaultDistance](ms-its:sldworksapivb6.chm::/sldworks~VariableFilletFeatureData2~DefaultDistance.html).

## Remarks

See [Accessing Selections that Define Features](sldworksapiprogguide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html)
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.html)
[IVariableFilletFeatureData2::DefaultRadius Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~DefaultRadius.html)
[IVariableFilletFeatureData2::DefaultConicRhoOrRadius Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~DefaultConicRhoOrRadius.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0

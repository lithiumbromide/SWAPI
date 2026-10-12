---
title: "DefaultRadius Property (IVariableFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IVariableFilletFeatureData2"
member: "DefaultRadius"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~DefaultRadius.html"
---

# DefaultRadius Property (IVariableFilletFeatureData2)

Gets or sets the default radius for this symmetric fillet or the default Distance 1 radius for this asymmetric fillet.

## Syntax

### Visual Basic (Declaration)

```vb
Property DefaultRadius As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IVariableFilletFeatureData2
Dim value As System.Double

instance.DefaultRadius = value

value = instance.DefaultRadius
```

### C#

```csharp
System.double DefaultRadius {get; set;}
```

### C++/CLI

```cpp
property System.double DefaultRadius {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Default radius if a symmetric fillet; default Distance 1 radius if an asymmetric fillet

## VBA Syntax

See [VariableFilletFeatureData2::DefaultRadius](ms-its:sldworksapivb6.chm::/sldworks~VariableFilletFeatureData2~DefaultRadius.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html)
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.html)
[IVariableFilletFeatureData2::GetRadius2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetRadius2.html)
[IVariableFilletFeatureData2::ISetRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ISetRadius.html)
[IVariableFilletFeatureData2::SetRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetRadius.html)
[IVariableFilletFeatureData2::DefaultConicRhoOrRadius Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~DefaultConicRhoOrRadius.html)
[IVariableFilletFeatureData2::DefaultDistance Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~DefaultDistance.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

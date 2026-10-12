---
title: "ISetConicRhoOrRadius Method (IVariableFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IVariableFilletFeatureData2"
member: "ISetConicRhoOrRadius"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ISetConicRhoOrRadius.html"
---

# ISetConicRhoOrRadius Method (IVariableFilletFeatureData2)

Sets the conic rho, conic radius, or circular radius of this fillet.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetConicRhoOrRadius( _
   ByVal PFilletItem As Vertex, _
   ByVal ConicRhoVal As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IVariableFilletFeatureData2
Dim PFilletItem As Vertex
Dim ConicRhoVal As System.Double

instance.ISetConicRhoOrRadius(PFilletItem, ConicRhoVal)
```

### C#

```csharp
void ISetConicRhoOrRadius(
   Vertex PFilletItem,
   System.double ConicRhoVal
)
```

### C++/CLI

```cpp
void ISetConicRhoOrRadius(
   Vertex^ PFilletItem,
   System.double ConicRhoVal
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PFilletItem`: Fillet edge for which to set ConicRhoVal (see **Remarks**)
- `ConicRhoVal`: Conic rho, conic radius, or circular radius (see **Remarks**)

## Remarks

Before calling this method, call [IVariableFilletFeatureData2::IGetFilletEdgeAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVariableFilletFeatureData2~IGetFilletEdgeAtIndex.html) to specify PFilletItem.

The type of ConicRhoVal must match the [IVariableFilletFeatureData2::ConicTypeForCrossSectionProfile](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVariableFilletFeatureData2~ConicTypeForCrossSectionProfile.html) setting.

If setting the conic rho value, it must be in the range [0.05, 0.95].

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html)
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.html)
[IVariableFilletFeatureData2::IGetConicRhoOrRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~IGetConicRhoOrRadius.html)
[IVariableFilletFeatureData2::SetConicRhoOrRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetConicRhoOrRadius.html)
[IVariableFilletFeatureData2::ISetRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ISetRadius.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0

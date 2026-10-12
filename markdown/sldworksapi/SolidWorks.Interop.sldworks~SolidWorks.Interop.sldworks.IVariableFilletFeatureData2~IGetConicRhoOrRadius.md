---
title: "IGetConicRhoOrRadius Method (IVariableFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IVariableFilletFeatureData2"
member: "IGetConicRhoOrRadius"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~IGetConicRhoOrRadius.html"
---

# IGetConicRhoOrRadius Method (IVariableFilletFeatureData2)

Gets the conic rho, conic radius, or circular radius of this fillet.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetConicRhoOrRadius( _
   ByVal PFilletItem As Vertex _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IVariableFilletFeatureData2
Dim PFilletItem As Vertex
Dim value As System.Double

value = instance.IGetConicRhoOrRadius(PFilletItem)
```

### C#

```csharp
System.double IGetConicRhoOrRadius(
   Vertex PFilletItem
)
```

### C++/CLI

```cpp
System.double IGetConicRhoOrRadius(
   Vertex^ PFilletItem
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PFilletItem`: Fillet edge for which to get a value (see **Remarks**)

### Return Value

Conic rho, conic radius, or circular radius

## Remarks

Before calling this method, call [IVariableFilletFeatureData2::IGetFilletEdgeAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVariableFilletFeatureData2~IGetFilletEdgeAtIndex.html) to specify PFilletItem.

The type of value returned by this method corresponds to the [IVariableFilletFeatureData2::ConicTypeForCrossSectionProfile](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVariableFilletFeatureData2~ConicTypeForCrossSectionProfile.html) setting.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html)
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.html)
[IVariableFilletFeatureData2::GetConicRhoOrRadius2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetConicRhoOrRadius2.html)
[IVariableFilletFeatureData2::ISetConicRhoOrRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ISetConicRhoOrRadius.html)
[IVariableFilletFeatureData2::IGetRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~IGetRadius.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0

---
title: "GetConicRhoOrRadius Method (IVariableFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IVariableFilletFeatureData2"
member: "GetConicRhoOrRadius"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetConicRhoOrRadius.html"
---

# GetConicRhoOrRadius Method (IVariableFilletFeatureData2)

Gets the conic rho, conic radius, or circular radius of this fillet.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetConicRhoOrRadius( _
   ByVal PFilletItem As System.Object _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IVariableFilletFeatureData2
Dim PFilletItem As System.Object
Dim value As System.Double

value = instance.GetConicRhoOrRadius(PFilletItem)
```

### C#

```csharp
System.double GetConicRhoOrRadius(
   System.object PFilletItem
)
```

### C++/CLI

```cpp
System.double GetConicRhoOrRadius(
   System.Object^ PFilletItem
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PFilletItem`: Fillet edge for which to get a value (see **Remarks**)

### Return Value

Conic rho or radius of this fillet

## VBA Syntax

See [VariableFilletFeatureData2::GetConicRhoOrRadius](ms-its:sldworksapivb6.chm::/sldworks~VariableFilletFeatureData2~GetConicRhoOrRadius.html).

## Remarks

Before calling this method, call [IVariableFilletFeatureData2::GetFilletEdgeAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVariableFilletFeatureData2~GetFilletEdgeAtIndex.html) to specify PFilletItem.

The type of value returned by this method corresponds to the [IVariableFilletFeatureData2::ConicTypeForCrossSectionProfile](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVariableFilletFeatureData2~ConicTypeForCrossSectionProfile.html) setting.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html)
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.html)
[IVariableFilletFeatureData2::SetConicRhoOrRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetConicRhoOrRadius.html)
[IVariableFilletFeatureData2::IGetConicRhoOrRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~IGetConicRhoOrRadius.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0

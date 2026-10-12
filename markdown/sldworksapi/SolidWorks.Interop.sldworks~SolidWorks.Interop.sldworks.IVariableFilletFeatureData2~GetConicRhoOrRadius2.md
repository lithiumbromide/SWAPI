---
title: "GetConicRhoOrRadius2 Method (IVariableFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IVariableFilletFeatureData2"
member: "GetConicRhoOrRadius2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetConicRhoOrRadius2.html"
---

# GetConicRhoOrRadius2 Method (IVariableFilletFeatureData2)

Gets the conic rho or radius at the specified vertex.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetConicRhoOrRadius2( _
   ByVal PFilletItem As Vertex, _
   ByRef IsAssigned As System.Boolean _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IVariableFilletFeatureData2
Dim PFilletItem As Vertex
Dim IsAssigned As System.Boolean
Dim value As System.Double

value = instance.GetConicRhoOrRadius2(PFilletItem, IsAssigned)
```

### C#

```csharp
System.double GetConicRhoOrRadius2(
   Vertex PFilletItem,
   out System.bool IsAssigned
)
```

### C++/CLI

```cpp
System.double GetConicRhoOrRadius2(
   Vertex^ PFilletItem,
   [Out] System.bool IsAssigned
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PFilletItem`: Vertex for which to get a value (see **Remarks**)
- `IsAssigned`: True if the conic value is assigned to each control point, false if not

### Return Value

Conic rho or radius

## VBA Syntax

See [VariableFilletFeatureData2::GetConicRhoOrRadius2](ms-its:sldworksapivb6.chm::/sldworks~VariableFilletFeatureData2~GetConicRhoOrRadius2.html).

## Remarks

Before calling this method, call [IVariableFilletFeatureData2::GetFilletEdgeAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVariableFilletFeatureData2~GetFilletEdgeAtIndex.html) to specify PFilletItem.

If [IVariableFilletFeatureData2::ConicTypeForCrossSectionProfile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ConicTypeForCrossSectionProfile.html) is set to [swFeatureFilletProfileType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletProfileType_e.html).:

- swFeatureFilletConicRadius (symmetric fillet only), then this method returns a radius.
- swFeatureFilletConicRho (symmetric or asymmetric fillet), then this method returns a conic rho value in the range [0.05, 0.95].

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html)
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.html)
[IVariableFilletFeatureData2::IGetConicRhoOrRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~IGetConicRhoOrRadius.html)
[IVariableFilletFeatureData2::SetConicRhoOrRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetConicRhoOrRadius.html)
[IVariableFilletFeatureData2::GetRadius2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetRadius2.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0

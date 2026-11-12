---
title: "SetRadius Method (IVariableFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IVariableFilletFeatureData2"
member: "SetRadius"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetRadius.html"
---

# SetRadius Method (IVariableFilletFeatureData2)

Sets the value of the Distance 1 radius at the specified vertex.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetRadius( _
   ByVal PFilletItem As System.Object, _
   ByVal Radius As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IVariableFilletFeatureData2
Dim PFilletItem As System.Object
Dim Radius As System.Double

instance.SetRadius(PFilletItem, Radius)
```

### C#

```csharp
void SetRadius(
   System.object PFilletItem,
   System.double Radius
)
```

### C++/CLI

```cpp
void SetRadius(
   System.Object^ PFilletItem,
   System.double Radius
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PFilletItem`: [Vertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html) at which to set the radius
- `Radius`: Radius of the symmetric fillet at the vertex specified by PFilletItem; Distance 1 radius of the asymmetric fillet at the vertex

## VBA Syntax

See [VariableFilletFeatureData2::SetRadius](ms-its:sldworksapivb6.chm::/sldworks~VariableFilletFeatureData2~SetRadius.html).

## Remarks

Call [IVariableFilletFeatureData2::SetDistance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVariableFilletFeatureData2~SetDistance.html) to set the Distance 2 radius at the vertex for the asymmetric fillet.

See [Accessing Selections that Define Features](sldworksapiprogguide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html)
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.html)
[IVariableFilletFeatureData2::DefaultRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~DefaultRadius.html)
[IVariableFilletFeatureData2::GetRadius2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetRadius2.html)
[IVariableFilletFeatureData2::SetConicRhoOrRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetConicRhoOrRadius.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

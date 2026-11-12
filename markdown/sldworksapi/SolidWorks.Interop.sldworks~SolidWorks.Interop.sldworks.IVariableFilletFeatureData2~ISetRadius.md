---
title: "ISetRadius Method (IVariableFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IVariableFilletFeatureData2"
member: "ISetRadius"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ISetRadius.html"
---

# ISetRadius Method (IVariableFilletFeatureData2)

Sets the radius value for specified fillet item.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetRadius( _
   ByVal PFilletItem As Vertex, _
   ByVal Radius As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IVariableFilletFeatureData2
Dim PFilletItem As Vertex
Dim Radius As System.Double

instance.ISetRadius(PFilletItem, Radius)
```

### C#

```csharp
void ISetRadius(
   Vertex PFilletItem,
   System.double Radius
)
```

### C++/CLI

```cpp
void ISetRadius(
   Vertex^ PFilletItem,
   System.double Radius
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PFilletItem`: [Vertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html) whose radius to set
- `Radius`: Radius

## VBA Syntax

See [VariableFilletFeatureData2::ISetRadius](ms-its:sldworksapivb6.chm::/sldworks~VariableFilletFeatureData2~ISetRadius.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html)
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.html)
[IVariableFilletFeatureData2::SetRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetRadius.html)
[IVariableFilletFeatureData2::DefaultRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~DefaultRadius.html)
[IVariableFilletFeatureData2::GetRadius2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetRadius2.html)
[IVariableFilletFeatureData2::ISetConicRhoOrRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ISetConicRhoOrRadius.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

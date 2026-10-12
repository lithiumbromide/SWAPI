---
title: "GetRadius2 Method (IVariableFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IVariableFilletFeatureData2"
member: "GetRadius2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetRadius2.html"
---

# GetRadius2 Method (IVariableFilletFeatureData2)

Gets the value of the Distance 1 radius at the specified vertex.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRadius2( _
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

value = instance.GetRadius2(PFilletItem, IsAssigned)
```

### C#

```csharp
System.double GetRadius2(
   Vertex PFilletItem,
   out System.bool IsAssigned
)
```

### C++/CLI

```cpp
System.double GetRadius2(
   Vertex^ PFilletItem,
   [Out] System.bool IsAssigned
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PFilletItem`: [Vertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html) at which to get the radius
- `IsAssigned`: True if the radius is assigned to a control point, false if not

### Return Value

Fillet radius at the vertex specified by PFilletItem for the symmetric fillet; Distance 1 radius at the vertex for the asymmetric fillet (see **Remarks**)

## VBA Syntax

See [VariableFilletFeatureData2::GetRadius2](ms-its:sldworksapivb6.chm::/sldworks~VariableFilletFeatureData2~GetRadius2.html).

## Examples

See the [IVariableFilletFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVariableFilletFeatureData2.html) examples.

## Remarks

Call [IVariableFilletFeatureData2::GetDistance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVariableFilletFeatureData2~GetDistance.html) to get the Distance 2 radius at the vertex for the asymmetric fillet.

## See Also

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html)
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.html)
[IVariableFilletFeatureData2::ISetRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ISetRadius.html)
[IVariableFilletFeatureData2::SetRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetRadius.html)
[IVariableFilletFeatureData2::DefaultRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~DefaultRadius.html)
[IVariableFilletFeatureData2::GetConicRhoOrRadius2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetConicRhoOrRadius2.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0

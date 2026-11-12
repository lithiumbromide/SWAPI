---
title: "GetDistance Method (IVariableFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IVariableFilletFeatureData2"
member: "GetDistance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetDistance.html"
---

# GetDistance Method (IVariableFilletFeatureData2)

Gets the Distance 2 radius for this asymmetric fillet.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDistance( _
   ByVal PFilletItem As System.Object _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IVariableFilletFeatureData2
Dim PFilletItem As System.Object
Dim value As System.Double

value = instance.GetDistance(PFilletItem)
```

### C#

```csharp
System.double GetDistance(
   System.object PFilletItem
)
```

### C++/CLI

```cpp
System.double GetDistance(
   System.Object^ PFilletItem
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PFilletItem`: [Vertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html) at which to get the radius

### Return Value

Distance 2 radius at the vertex for the asymmetric fillet

## VBA Syntax

See [VariableFilletFeatureData2::GetDistance](ms-its:sldworksapivb6.chm::/sldworks~VariableFilletFeatureData2~GetDistance.html).

## Examples

See the [IVariableFilletFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVariableFilletFeatureData2.html) examples.

## Remarks

Call [IVariableFilletFeatureData2::GetRadius2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVariableFilletFeatureData2~GetRadius2.html) to get the Distance 1 radius at the vertex for this asymmetric fillet.

## See Also

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html)
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.html)
[IVariableFilletFeatureData2::SetDistance Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetDistance.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0

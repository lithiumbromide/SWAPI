---
title: "GetIsFlipped Method (IChamferFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IChamferFeatureData2"
member: "GetIsFlipped"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~GetIsFlipped.html"
---

# GetIsFlipped Method (IChamferFeatureData2)

Gets whether the chamfer feature is flipped.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetIsFlipped( _
   ByVal Entity As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IChamferFeatureData2
Dim Entity As System.Object
Dim value As System.Boolean

value = instance.GetIsFlipped(Entity)
```

### C#

```csharp
System.bool GetIsFlipped(
   System.object Entity
)
```

### C++/CLI

```cpp
System.bool GetIsFlipped(
   System.Object^ Entity
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Entity`: Edge, face, or loop

### Return Value

True if the chamfer feature is flipped, false if not

## VBA Syntax

See [ChamferFeatureData2::GetIsFlipped](ms-its:sldworksapivb6.chm::/sldworks~ChamferFeatureData2~GetIsFlipped.html).

## Examples

[Get Edge Chamfer Distances (C#)](Get_Edge_Chamfer_Distances_Example_CSharp.htm)
[Get Edge Chamfer Distances (VB.NET)](Get_Edge_Chamfer_Distances_Example_VBNET.htm)
[Get Edge Chamfer Distances (VBA)](Get_Edge_Chamfer_Distances_Example_VB.htm)

## See Also

[IChamferFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.html)
[IChamferFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2_members.html)
[IChamferFeatureData2::SetIsFlipped Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~SetIsFlipped.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

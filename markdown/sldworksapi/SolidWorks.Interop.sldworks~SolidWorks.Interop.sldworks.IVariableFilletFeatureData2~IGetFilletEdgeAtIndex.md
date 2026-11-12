---
title: "IGetFilletEdgeAtIndex Method (IVariableFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IVariableFilletFeatureData2"
member: "IGetFilletEdgeAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~IGetFilletEdgeAtIndex.html"
---

# IGetFilletEdgeAtIndex Method (IVariableFilletFeatureData2)

Gets the fillet edge at the specified index.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFilletEdgeAtIndex( _
   ByVal Index As System.Integer _
) As Edge
```

### Visual Basic (Usage)

```vb
Dim instance As IVariableFilletFeatureData2
Dim Index As System.Integer
Dim value As Edge

value = instance.IGetFilletEdgeAtIndex(Index)
```

### C#

```csharp
Edge IGetFilletEdgeAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
Edge^ IGetFilletEdgeAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index at which fillet edge is required

### Return Value

Fillet [edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)

## VBA Syntax

See [VariableFilletFeatureData2::IGetFilletEdgeAtIndex](ms-its:sldworksapivb6.chm::/sldworks~VariableFilletFeatureData2~IGetFilletEdgeAtIndex.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html)
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.html)
[IVariableFilletFeatureData2::GetFilletEdgeAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetFilletEdgeAtIndex.html)
[IVariableFilletFeatureData2::FilletEdgeCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~FilletEdgeCount.html)
[IVariableFilletFeatureData2::IGetConicRhoOrRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~IGetConicRhoOrRadius.html)
[IVariableFilletFeatureData2::ISetConicRhoOrRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ISetConicRhoOrRadius.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0

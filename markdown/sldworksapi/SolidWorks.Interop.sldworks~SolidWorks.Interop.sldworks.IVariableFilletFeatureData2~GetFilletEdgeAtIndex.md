---
title: "GetFilletEdgeAtIndex Method (IVariableFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IVariableFilletFeatureData2"
member: "GetFilletEdgeAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetFilletEdgeAtIndex.html"
---

# GetFilletEdgeAtIndex Method (IVariableFilletFeatureData2)

Gets the fillet edge at the specified index.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFilletEdgeAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IVariableFilletFeatureData2
Dim Index As System.Integer
Dim value As System.Object

value = instance.GetFilletEdgeAtIndex(Index)
```

### C#

```csharp
System.object GetFilletEdgeAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.Object^ GetFilletEdgeAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Zero-based index of the fillet edge

### Return Value

Fillet [edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)

## VBA Syntax

See [VariableFilletFeatureData2::GetFilletEdgeAtIndex](ms-its:sldworksapivb6.chm::/sldworks~VariableFilletFeatureData2~GetFilletEdgeAtIndex.html).

## Examples

See the [IVariableFilletFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVariableFilletFeatureData2.html) examples.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html)
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.html)
[IVariableFilletFeatureData2::IGetFilletEdgeAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~IGetFilletEdgeAtIndex.html)
[IVariableFilletFeatureData2::FilletEdgeCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~FilletEdgeCount.html)
[IVariableFilletFeatureData2::GetConicRhoOrRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetConicRhoOrRadius.html)
[IVariableFilletFeatureData2::GetConicRhoOrRadius2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetConicRhoOrRadius2.html)
[IVariableFilletFeatureData2::SetConicRhoOrRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetConicRhoOrRadius.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0

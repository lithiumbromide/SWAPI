---
title: "GetCornerAtIndex Method (ICornerReliefFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICornerReliefFeatureData"
member: "GetCornerAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData~GetCornerAtIndex.html"
---

# GetCornerAtIndex Method (ICornerReliefFeatureData)

Gets the corner at the specified index of this corner relief feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCornerAtIndex( _
   ByVal CornerIndex As System.Integer, _
   ByRef Corner As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICornerReliefFeatureData
Dim CornerIndex As System.Integer
Dim Corner As System.Object
Dim value As System.Integer

value = instance.GetCornerAtIndex(CornerIndex, Corner)
```

### C#

```csharp
System.int GetCornerAtIndex(
   System.int CornerIndex,
   out System.object Corner
)
```

### C++/CLI

```cpp
System.int GetCornerAtIndex(
   System.int CornerIndex,
   [Out] System.Object^ Corner
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CornerIndex`: One-based index of corner to retrieve
- `Corner`: [ISMCornerReliefData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData.html)

### Return Value

Error code as defined by [swCornerReliefError_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerReliefError_e.html)

## VBA Syntax

See [CornerReliefFeatureData::GetCornerAtIndex](ms-its:sldworksapivb6.chm::/sldworks~CornerReliefFeatureData~GetCornerAtIndex.html).

## Examples

See the [ICornerReliefFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.html) examples.

## See Also

[ICornerReliefFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.html)
[ICornerReliefFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30

---
title: "RemoveCorner Method (ICornerReliefFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICornerReliefFeatureData"
member: "RemoveCorner"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData~RemoveCorner.html"
---

# RemoveCorner Method (ICornerReliefFeatureData)

Removes the specified corner from this corner relief feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveCorner( _
   ByVal CornerIndex As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICornerReliefFeatureData
Dim CornerIndex As System.Integer
Dim value As System.Boolean

value = instance.RemoveCorner(CornerIndex)
```

### C#

```csharp
System.bool RemoveCorner(
   System.int CornerIndex
)
```

### C++/CLI

```cpp
System.bool RemoveCorner(
   System.int CornerIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CornerIndex`: One-based index of corner to remove

### Return Value

True if specified corner successfully removed, false if not

## VBA Syntax

See [CornerReliefFeatureData::RemoveCorner](ms-its:sldworksapivb6.chm::/sldworks~CornerReliefFeatureData~RemoveCorner.html).

## See Also

[ICornerReliefFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.html)
[ICornerReliefFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30

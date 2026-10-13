---
title: "GetCorners Method (ICornerReliefFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICornerReliefFeatureData"
member: "GetCorners"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData~GetCorners.html"
---

# GetCorners Method (ICornerReliefFeatureData)

Gets all corners of the specified type in this corner relief feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCorners( _
   ByVal CornerReliefType As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICornerReliefFeatureData
Dim CornerReliefType As System.Integer
Dim value As System.Object

value = instance.GetCorners(CornerReliefType)
```

### C#

```csharp
System.object GetCorners(
   System.int CornerReliefType
)
```

### C++/CLI

```cpp
System.Object^ GetCorners(
   System.int CornerReliefType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CornerReliefType`: Corner relief type as defined by [swCornerReliefType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerReliefType_e.html)

### Return Value

Array of [ISMCornerReliefData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData.html)s

## VBA Syntax

See [CornerReliefFeatureData::GetCorners](ms-its:sldworksapivb6.chm::/sldworks~CornerReliefFeatureData~GetCorners.html).

## Examples

See the [ICornerReliefFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.html) examples.

## Remarks

If CornerReliefType is specified with -1, then this method retrieves corners of all types.

## See Also

[ICornerReliefFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.html)
[ICornerReliefFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30

---
title: "GetOffsetReferenceType Method (IJogFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IJogFeatureData"
member: "GetOffsetReferenceType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~GetOffsetReferenceType.html"
---

# GetOffsetReferenceType Method (IJogFeatureData)

Gets the offset reference geometry type for this jog feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetOffsetReferenceType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IJogFeatureData
Dim value As System.Integer

value = instance.GetOffsetReferenceType()
```

### C#

```csharp
System.int GetOffsetReferenceType()
```

### C++/CLI

```cpp
System.int GetOffsetReferenceType();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Offset reference geometry type as defined in [swJogOffsetTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swJogOffsetTypes_e.html)

## VBA Syntax

See [JogFeatureData::GetOffsetReferenceType](ms-its:sldworksapivb6.chm::/sldworks~JogFeatureData~GetOffsetReferenceType.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IJogFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData.html)
[IJogFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData_members.html)
[IJogFeatureData::OffsetDistance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~OffsetDistance.html)
[IJogFeatureData::OffsetReference Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~OffsetReference.html)
[IJogFeatureData::OffsetType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~OffsetType.html)
[IJogFeatureData::ReverseOffset Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~ReverseOffset.html)

## Availability

SOLIDWORKS 2001Plus SP3, Revision Number 10.3

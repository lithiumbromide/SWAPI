---
title: "GetMemberIndex Method (IBeltChainFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBeltChainFeatureData"
member: "GetMemberIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~GetMemberIndex.html"
---

# GetMemberIndex Method (IBeltChainFeatureData)

Gets the index of the specified pulley member.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMemberIndex( _
   ByVal PulleyCompObject As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBeltChainFeatureData
Dim PulleyCompObject As System.Object
Dim value As System.Integer

value = instance.GetMemberIndex(PulleyCompObject)
```

### C#

```csharp
System.int GetMemberIndex(
   System.object PulleyCompObject
)
```

### C++/CLI

```cpp
System.int GetMemberIndex(
   System.Object^ PulleyCompObject
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PulleyCompObject`: Pulley component

### Return Value

Zero-based index value

## VBA Syntax

See [BeltChainFeatureData::GetMemberIndex](ms-its:sldworksapivb6.chm::/sldworks~BeltChainFeatureData~GetMemberIndex.html).

## Remarks

To specify PulleyCompObject, use [IBeltChainFeatureData::PulleyComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~PulleyComponents.html).

## See Also

[IBeltChainFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.html)
[IBeltChainFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30

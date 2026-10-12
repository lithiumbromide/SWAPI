---
title: "AccessBeltPart Method (IBeltChainFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBeltChainFeatureData"
member: "AccessBeltPart"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~AccessBeltPart.html"
---

# AccessBeltPart Method (IBeltChainFeatureData)

Gets the belt part.

## Syntax

### Visual Basic (Declaration)

```vb
Function AccessBeltPart() As PartDoc
```

### Visual Basic (Usage)

```vb
Dim instance As IBeltChainFeatureData
Dim value As PartDoc

value = instance.AccessBeltPart()
```

### C#

```csharp
PartDoc AccessBeltPart()
```

### C++/CLI

```cpp
PartDoc^ AccessBeltPart();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IPartDoc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)

## VBA Syntax

See [BeltChainFeatureData::AccessBeltPart](ms-its:sldworksapivb6.chm::/sldworks~BeltChainFeatureData~AccessBeltPart.html).

## Remarks

This method is valid only if [IBeltChainFeatureData::CreateBeltPart](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~CreateBeltPart.html) is true.

## See Also

[IBeltChainFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.html)
[IBeltChainFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30

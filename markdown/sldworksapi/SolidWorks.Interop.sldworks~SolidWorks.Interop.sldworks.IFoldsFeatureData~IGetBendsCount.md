---
title: "IGetBendsCount Method (IFoldsFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFoldsFeatureData"
member: "IGetBendsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFoldsFeatureData~IGetBendsCount.html"
---

# IGetBendsCount Method (IFoldsFeatureData)

Gets the number of bend features in this fold feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetBendsCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFoldsFeatureData
Dim value As System.Integer

value = instance.IGetBendsCount()
```

### C#

```csharp
System.int IGetBendsCount()
```

### C++/CLI

```cpp
System.int IGetBendsCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of bend features in this fold feature

## VBA Syntax

See [FoldsFeatureData::IGetBendsCount](ms-its:sldworksapivb6.chm::/sldworks~FoldsFeatureData~IGetBendsCount.html).

## See Also

[IFoldsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFoldsFeatureData.html)
[IFoldsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFoldsFeatureData_members.html)
[IFoldsFeatureData::IGetBends Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFoldsFeatureData~IGetBends.html)
[IFoldsFeatureData::ISetBends Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFoldsFeatureData~ISetBends.html)
[IFoldsFeatureData::Bends Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFoldsFeatureData~Bends.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2

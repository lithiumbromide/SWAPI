---
title: "GetEntitiesCount Method (IBreakCornerFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBreakCornerFeatureData"
member: "GetEntitiesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData~GetEntitiesCount.html"
---

# GetEntitiesCount Method (IBreakCornerFeatureData)

Gets the number of faces or edges associated with this break corner feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEntitiesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBreakCornerFeatureData
Dim value As System.Integer

value = instance.GetEntitiesCount()
```

### C#

```csharp
System.int GetEntitiesCount()
```

### C++/CLI

```cpp
System.int GetEntitiesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of faces or edges

## VBA Syntax

See [BreakCornerFeatureData::GetEntitiesCount](ms-its:sldworksapivb6.chm::/sldworks~BreakCornerFeatureData~GetEntitiesCount.html).

## Remarks

Call this method before calling [IBreakCornerFeatureData::IGetEntities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBreakCornerFeatureData~IGetEntities.html).

## See Also

[IBreakCornerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData.html)
[IBreakCornerFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision NUmber 10.1

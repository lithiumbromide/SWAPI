---
title: "GetPartingLinesCount Method (IPartingLineFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPartingLineFeatureData"
member: "GetPartingLinesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~GetPartingLinesCount.html"
---

# GetPartingLinesCount Method (IPartingLineFeatureData)

Gets the number of edges used as parting lines.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPartingLinesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPartingLineFeatureData
Dim value As System.Integer

value = instance.GetPartingLinesCount()
```

### C#

```csharp
System.int GetPartingLinesCount()
```

### C++/CLI

```cpp
System.int GetPartingLinesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of edges

## VBA Syntax

See [PartingLineFeatureData::GetPartingLinesCount](ms-its:sldworksapivb6.chm::/sldworks~PartingLineFeatureData~GetPartingLinesCount.html).

## Remarks

Call this method before calling [IPartingLineFeatureData::IGetPartingLines](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartingLineFeatureData~IGetPartingLines.html).

## See Also

[IPartingLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData.html)
[IPartingLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData_members.html)
[IPartingLineFeatureData::ISetPartingLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~ISetPartingLines.html)
[IPartingLineFeatureData::PartingLines Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~PartingLines.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0

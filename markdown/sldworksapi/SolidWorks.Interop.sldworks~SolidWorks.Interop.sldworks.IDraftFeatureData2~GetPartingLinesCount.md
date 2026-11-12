---
title: "GetPartingLinesCount Method (IDraftFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IDraftFeatureData2"
member: "GetPartingLinesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~GetPartingLinesCount.html"
---

# GetPartingLinesCount Method (IDraftFeatureData2)

Gets the number of parting lines for this draft feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPartingLinesCount() As System.Short
```

### Visual Basic (Usage)

```vb
Dim instance As IDraftFeatureData2
Dim value As System.Short

value = instance.GetPartingLinesCount()
```

### C#

```csharp
System.short GetPartingLinesCount()
```

### C++/CLI

```cpp
System.short GetPartingLinesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of parting lines

## VBA Syntax

See [DraftFeatureData2::GetPartingLinesCount](ms-its:sldworksapivb6.chm::/sldworks~DraftFeatureData2~GetPartingLinesCount.html).

## Remarks

Call this method before calling [IDraftFeatureData2::IGetPartingLines](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDraftFeatureData2~IGetPartingLines.html) to determine the size of the array for that method.

## See Also

[IDraftFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2.html)
[IDraftFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2_members.html)
[IDraftFeatureData2::ISetPartingLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~ISetPartingLines.html)
[IDraftFeatureData2::PartingLines Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~PartingLines.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

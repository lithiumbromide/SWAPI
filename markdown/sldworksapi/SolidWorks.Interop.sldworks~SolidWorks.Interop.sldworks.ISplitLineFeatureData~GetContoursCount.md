---
title: "GetContoursCount Method (ISplitLineFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISplitLineFeatureData"
member: "GetContoursCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~GetContoursCount.html"
---

# GetContoursCount Method (ISplitLineFeatureData)

Gets the number of selected contours for this split line feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetContoursCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISplitLineFeatureData
Dim value As System.Integer

value = instance.GetContoursCount()
```

### C#

```csharp
System.int GetContoursCount()
```

### C++/CLI

```cpp
System.int GetContoursCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of selected contours

## VBA Syntax

See [SplitLineFeatureData::GetContoursCount](ms-its:sldworksapivb6.chm::/sldworks~SplitLineFeatureData~GetContoursCount.html).

## Remarks

Call this method before calling [ISplitLineFeatureData::IGetContours](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplitLineFeatureData~IGetContours.html) to determine the size of the array for that method.

## See Also

[ISplitLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData.html)
[ISplitLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData_members.html)
[ISplitLineFeatureData:ISetContours Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~ISetContours.html)
[ISplitLineFeatureData::Contours Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~Contours.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0

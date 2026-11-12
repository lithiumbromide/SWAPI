---
title: "IGetPatternBodyArray Method (ITablePatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ITablePatternFeatureData"
member: "IGetPatternBodyArray"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~IGetPatternBodyArray.html"
---

# IGetPatternBodyArray Method (ITablePatternFeatureData)

Gets the seed bodies for this table-driven pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetPatternBodyArray() As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As ITablePatternFeatureData
Dim value As Body2

value = instance.IGetPatternBodyArray()
```

### C#

```csharp
Body2 IGetPatternBodyArray()
```

### C++/CLI

```cpp
Body2^ IGetPatternBodyArray();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of seed [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ITablePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.html)
[ITablePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData_members.html)
[ITablePatternFeatureData::PatternBodyArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~PatternBodyArray.html)
[ITablePatternFeatureData::GetPatternBodyCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~GetPatternBodyCount.html)
[ITablePatternFeatureData::ISetPatternBodyArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~ISetPatternBodyArray.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0

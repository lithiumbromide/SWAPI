---
title: "IGetPatternBodyArray Method (ILinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILinearPatternFeatureData"
member: "IGetPatternBodyArray"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~IGetPatternBodyArray.html"
---

# IGetPatternBodyArray Method (ILinearPatternFeatureData)

Gets the seed bodies for this linear pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetPatternBodyArray() As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As ILinearPatternFeatureData
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

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html)
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.html)
[ILinearPatternFeatureData::GetPatternBodyCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~GetPatternBodyCount.html)
[ILinearPatternFeatureData::ISetPatternBodyArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~ISetPatternBodyArray.html)
[ILinearPatternFeatureData::PatternBodyArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~PatternBodyArray.html)
[ILinearPatternFeatureData::BodyPattern Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~BodyPattern.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0

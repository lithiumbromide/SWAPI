---
title: "ISetPatternBodyArray Method (ILinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILinearPatternFeatureData"
member: "ISetPatternBodyArray"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~ISetPatternBodyArray.html"
---

# ISetPatternBodyArray Method (ILinearPatternFeatureData)

Sets the seed bodies for this linear pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetPatternBodyArray( _
   ByVal BodyCount As System.Integer, _
   ByRef ArrayDataIn As Body2 _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ILinearPatternFeatureData
Dim BodyCount As System.Integer
Dim ArrayDataIn As Body2

instance.ISetPatternBodyArray(BodyCount, ArrayDataIn)
```

### C#

```csharp
void ISetPatternBodyArray(
   System.int BodyCount,
   ref Body2 ArrayDataIn
)
```

### C++/CLI

```cpp
void ISetPatternBodyArray(
   System.int BodyCount,
   Body2^% ArrayDataIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BodyCount`: Number of seed bodies
- `ArrayDataIn`: - in-process, unmanaged C++: Pointer to an array of seed [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) of size BodyCount

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html)
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.html)
[ILinearPatternFeatureData::GetPatternBodyCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~GetPatternBodyCount.html)
[ILinearPatternFeatureData::IGetPatternBodyArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~IGetPatternBodyArray.html)
[ILinearPatternFeatureData::PatternBodyArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~PatternBodyArray.html)
[ILinearPatternFeatureData::BodyPattern Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~BodyPattern.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0

---
title: "ISetPatternFeatureArray Method (ICircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICircularPatternFeatureData"
member: "ISetPatternFeatureArray"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~ISetPatternFeatureArray.html"
---

# ISetPatternFeatureArray Method (ICircularPatternFeatureData)

Sets the seed features to use to create the circular pattern.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetPatternFeatureArray( _
   ByVal FeatCount As System.Integer, _
   ByRef ArrayDataIn As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICircularPatternFeatureData
Dim FeatCount As System.Integer
Dim ArrayDataIn As System.Object

instance.ISetPatternFeatureArray(FeatCount, ArrayDataIn)
```

### C#

```csharp
void ISetPatternFeatureArray(
   System.int FeatCount,
   ref System.object ArrayDataIn
)
```

### C++/CLI

```cpp
void ISetPatternFeatureArray(
   System.int FeatCount,
   System.Object^% ArrayDataIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FeatCount`: Number of seed features to use to create this circular pattern
- `ArrayDataIn`: - in-process, unmanaged C++: Pointer to an array of seed [features](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) to use to create the circular pattern

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.html)
[ICircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData_members.html)
[ICircularPatternFeatureData::GetPatternFeatureCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~GetPatternFeatureCount.html)
[ICircularPatternFeatureData::IGetPatternFeatureArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~IGetPatternFeatureArray.html)
[ICircularPatternFeatureData::PatternFeatureArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~PatternFeatureArray.html)
[ICircularPatternFeatureData::BodyPattern Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~BodyPattern.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0

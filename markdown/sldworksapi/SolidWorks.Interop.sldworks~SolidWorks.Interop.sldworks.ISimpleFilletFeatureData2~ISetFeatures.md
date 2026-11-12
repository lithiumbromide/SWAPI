---
title: "ISetFeatures Method (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "ISetFeatures"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetFeatures.html"
---

# ISetFeatures Method (ISimpleFilletFeatureData2)

Sets the features on which to create a simple radius fillet.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetFeatures( _
   ByVal Count As System.Integer, _
   ByRef FeatList As Feature _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
Dim Count As System.Integer
Dim FeatList As Feature

instance.ISetFeatures(Count, FeatList)
```

### C#

```csharp
void ISetFeatures(
   System.int Count,
   ref Feature FeatList
)
```

### C++/CLI

```cpp
void ISetFeatures(
   System.int Count,
   Feature^% FeatList
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of features
- `FeatList`: - in-process, unmanaged C++: Pointer to an array of [features](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) of size Count

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)
[ISimpleFilletFeatureData2::GetFeatureCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetFeatureCount.html)
[ISimpleFilletFeatureData2::IGetFeatures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetFeatures.html)
[ISimpleFilletFeatureData2::Features Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~Features.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0

---
title: "IGetPatternFeatureArray Method (ISketchPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISketchPatternFeatureData"
member: "IGetPatternFeatureArray"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~IGetPatternFeatureArray.html"
---

# IGetPatternFeatureArray Method (ISketchPatternFeatureData)

Gets the seed features for the sketch pattern.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetPatternFeatureArray() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPatternFeatureData
Dim value As System.Object

value = instance.IGetPatternFeatureArray()
```

### C#

```csharp
System.object IGetPatternFeatureArray()
```

### C++/CLI

```cpp
System.Object^ IGetPatternFeatureArray();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of [seed features](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISketchPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData.html)
[ISketchPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData_members.html)
[ISketchPatternFeatureData::GetPatternFeatureCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~GetPatternFeatureCount.html)
[ISketchPatternFeatureData::ISetPatternFaceArray Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~ISetPatternFaceArray.html)
[ISketchPatternFeatureData::PatternFeatureArray Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~PatternFeatureArray.html)
[ISketchPatternFeatureData::BodyPattern Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~BodyPattern.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0

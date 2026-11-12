---
title: "IGetPatternFaceArray Method (ILinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILinearPatternFeatureData"
member: "IGetPatternFaceArray"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~IGetPatternFaceArray.html"
---

# IGetPatternFaceArray Method (ILinearPatternFeatureData)

Gets the seed faces in this linear pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetPatternFaceArray() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILinearPatternFeatureData
Dim value As System.Object

value = instance.IGetPatternFaceArray()
```

### C#

```csharp
System.object IGetPatternFaceArray()
```

### C++/CLI

```cpp
System.Object^ IGetPatternFaceArray();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of seed [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html)
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.html)
[ILinearPatternFeatureData::GetPatternFaceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~GetPatternFaceCount.html)
[ILinearPatternFeatureData::ISetPatternFaceArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~ISetPatternFaceArray.html)
[ILinearPatternFeatureData::PatternFaceArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~PatternFaceArray.html)
[ILinearPatternFeatureData::BodyPattern Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~BodyPattern.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

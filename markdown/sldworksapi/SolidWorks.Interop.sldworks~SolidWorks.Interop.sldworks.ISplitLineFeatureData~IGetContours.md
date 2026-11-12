---
title: "IGetContours Method (ISplitLineFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISplitLineFeatureData"
member: "IGetContours"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~IGetContours.html"
---

# IGetContours Method (ISplitLineFeatureData)

Gets the selected contours for this split line feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetContours( _
   ByVal Count As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISplitLineFeatureData
Dim Count As System.Integer
Dim value As System.Object

value = instance.IGetContours(Count)
```

### C#

```csharp
System.object IGetContours(
   System.int Count
)
```

### C++/CLI

```cpp
System.Object^ IGetContours(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of selected contours

### Return Value

- in-process, unmanaged C++: Pointer to an array of contours of these types:
- - [Sketch contour](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchContour.html)
  - [Sketch region](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRegion.html)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [ISplitLineFeatureData::GetContoursCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplitLineFeatureData~GetContoursCount.html) before calling this method to determine the size of the array for this method.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISplitLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData.html)
[ISplitLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData_members.html)
[ISplitLineFeatureData::ISetContours Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~ISetContours.html)
[ISplitLineFeatureData::Contours Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~Contours.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0

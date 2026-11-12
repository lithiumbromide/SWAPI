---
title: "IGetContours Method (IExtrudeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2"
member: "IGetContours"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~IGetContours.html"
---

# IGetContours Method (IExtrudeFeatureData2)

Gets the selected contours for this extrude feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetContours( _
   ByVal Count As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData2
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

- in-process, unmanaged C++: Pointer to an array of contours ([sketch contours](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchContour.html) and [sketch regions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRegion.html)) of size count

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IExtrudeFeatureData2::GetContoursCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExtrudeFeatureData2~GetContoursCount.html) before calling this method.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html)
[IExtrudeFeatureData2::ISetContours Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~ISetContours.html)
[IExtrudeFeatureData2::Contours Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~Contours.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0

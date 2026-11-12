---
title: "ISetContours Method (IRevolveFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IRevolveFeatureData2"
member: "ISetContours"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~ISetContours.html"
---

# ISetContours Method (IRevolveFeatureData2)

Sets the selected contours for this revolve feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetContours( _
   ByVal Count As System.Integer, _
   ByRef Contours As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IRevolveFeatureData2
Dim Count As System.Integer
Dim Contours As System.Object

instance.ISetContours(Count, Contours)
```

### C#

```csharp
void ISetContours(
   System.int Count,
   ref System.object Contours
)
```

### C++/CLI

```cpp
void ISetContours(
   System.int Count,
   System.Object^% Contours
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of selected contours
- `Contours`: - in-process, unmanaged C++: Pointer to an array of selected contours ([sketch contours](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchContour.html) and [sketch regions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRegion.html)) of size Count

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IRevolveFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2.html)
[IRevolveFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2_members.html)
[IRevolveFeatureData2::GetContoursCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~GetContoursCount.html)
[IRevolveFeatureData2::IGetContours Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~IGetContours.html)
[IRevolveFeatureData2::Contours Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~Contours.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0

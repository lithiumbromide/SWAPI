---
title: "ISetContours Method (IExtrudeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2"
member: "ISetContours"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~ISetContours.html"
---

# ISetContours Method (IExtrudeFeatureData2)

Sets the selected contours for this extrude feature.

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
Dim instance As IExtrudeFeatureData2
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
- `Contours`: - in-process, unmanaged C++: Pointer to an array of selected contours of size Count

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html)
[IExtrudeFeatureData2::GetContoursCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetContoursCount.html)
[IExtrudeFeatureData2::IGetContours Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~IGetContours.html)
[IExtrudeFeatureData2::Contours Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~Contours.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0

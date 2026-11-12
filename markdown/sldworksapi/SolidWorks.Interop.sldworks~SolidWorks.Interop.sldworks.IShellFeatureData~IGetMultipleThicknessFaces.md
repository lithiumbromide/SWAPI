---
title: "IGetMultipleThicknessFaces Method (IShellFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IShellFeatureData"
member: "IGetMultipleThicknessFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~IGetMultipleThicknessFaces.html"
---

# IGetMultipleThicknessFaces Method (IShellFeatureData)

Gets the multiple-thickness faces in this shell feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetMultipleThicknessFaces( _
   ByVal Count As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IShellFeatureData
Dim Count As System.Integer
Dim value As System.Object

value = instance.IGetMultipleThicknessFaces(Count)
```

### C#

```csharp
System.object IGetMultipleThicknessFaces(
   System.int Count
)
```

### C++/CLI

```cpp
System.Object^ IGetMultipleThicknessFaces(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of multiple-thickness faces

### Return Value

- in-process, unmanaged C++: Pointer to an array of multiple-thickness [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) of size Count

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IShellFeatureData::GetMultipleThicknessFacesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IShellFeatureData~GetMultipleThicknessFacesCount.html) before calling this method to get the size of the array for this method.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IShellFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData.html)
[IShellFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData_members.html)
[IShellFeatureData::GetMultipleThicknessAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~GetMultipleThicknessAtIndex.html)
[IShellFeatureData::ISetMultipleThicknessFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~ISetMultipleThicknessFaces.html)
[IShellFeatureData::SetMultipleThicknessAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~SetMultipleThicknessAtIndex.html)
[IShellFeatureData::MultipleThicknessFaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~MultipleThicknessFaces.html)
[IShellFeatureData::Thickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~Thickness.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

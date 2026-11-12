---
title: "IGetFacesForReplacement Method (IReplaceFaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IReplaceFaceFeatureData"
member: "IGetFacesForReplacement"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~IGetFacesForReplacement.html"
---

# IGetFacesForReplacement Method (IReplaceFaceFeatureData)

Gets the faces to replace in this feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFacesForReplacement( _
   ByVal Count As System.Integer _
) As Face2
```

### Visual Basic (Usage)

```vb
Dim instance As IReplaceFaceFeatureData
Dim Count As System.Integer
Dim value As Face2

value = instance.IGetFacesForReplacement(Count)
```

### C#

```csharp
Face2 IGetFacesForReplacement(
   System.int Count
)
```

### C++/CLI

```cpp
Face2^ IGetFacesForReplacement(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of faces to replace

### Return Value

- in-process, unmanaged C++: Pointer to an array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) to replace of size Count
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IReplaceFaceFeatureData::GetFacesForReplacementCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IReplaceFaceFeatureData~GetFacesForReplacementCount.html) before calling this method to get the value for Count.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IReplaceFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData.html)
[IReplaceFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData_members.html)
[IReplaceFeatureFeatureData::ISetFacesForReplacement Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~ISetFacesForReplacement.html)
[IReplaceFeatureFeatureData::FacesForReplacement Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~FacesForReplacement.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

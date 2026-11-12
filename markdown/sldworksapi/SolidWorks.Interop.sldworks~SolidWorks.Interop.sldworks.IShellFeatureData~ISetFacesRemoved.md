---
title: "ISetFacesRemoved Method (IShellFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IShellFeatureData"
member: "ISetFacesRemoved"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~ISetFacesRemoved.html"
---

# ISetFacesRemoved Method (IShellFeatureData)

Sets the faces to remove in this shell feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetFacesRemoved( _
   ByVal Count As System.Integer, _
   ByRef FaceArray As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IShellFeatureData
Dim Count As System.Integer
Dim FaceArray As System.Object

instance.ISetFacesRemoved(Count, FaceArray)
```

### C#

```csharp
void ISetFacesRemoved(
   System.int Count,
   ref System.object FaceArray
)
```

### C++/CLI

```cpp
void ISetFacesRemoved(
   System.int Count,
   System.Object^% FaceArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of faces
- `FaceArray`: - in-process, unmanaged C++: Pointer to an array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) to remove of size Count

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IShellFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData.html)
[IShellFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData_members.html)
[IShellFeatureData::IGetFacesRemoved Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~IGetFacesRemoved.html)
[IShellFeatureData::FacesRemoved Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~FacesRemoved.html)
[IShellFeatureData::FacesRemovedCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~FacesRemovedCount.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

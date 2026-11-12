---
title: "IGetFacesRemoved Method (IShellFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IShellFeatureData"
member: "IGetFacesRemoved"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~IGetFacesRemoved.html"
---

# IGetFacesRemoved Method (IShellFeatureData)

Gets the faces removed in this shell feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFacesRemoved( _
   ByVal Count As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IShellFeatureData
Dim Count As System.Integer
Dim value As System.Object

value = instance.IGetFacesRemoved(Count)
```

### C#

```csharp
System.object IGetFacesRemoved(
   System.int Count
)
```

### C++/CLI

```cpp
System.Object^ IGetFacesRemoved(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of removed faces

### Return Value

- in-process, unmanaged C++: Pointer to an array of removed [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) of size Count

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IShellFeatureData::FacesRemovedCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IShellFeatureData~FacesRemovedCount.html) before calling this method to get the size of the array for this method.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IShellFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData.html)
[IShellFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData_members.html)
[IShellFeatureData::ISetFacesRemoved Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~ISetFacesRemoved.html)
[IShellFeatureData::FacesRemoved Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~FacesRemoved.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

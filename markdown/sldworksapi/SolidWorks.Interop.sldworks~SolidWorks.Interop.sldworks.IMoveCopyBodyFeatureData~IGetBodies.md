---
title: "IGetBodies Method (IMoveCopyBodyFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMoveCopyBodyFeatureData"
member: "IGetBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~IGetBodies.html"
---

# IGetBodies Method (IMoveCopyBodyFeatureData)

Gets the bodies to move or rotate and copy.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetBodies( _
   ByVal NCount As System.Integer _
) As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IMoveCopyBodyFeatureData
Dim NCount As System.Integer
Dim value As Body2

value = instance.IGetBodies(NCount)
```

### C#

```csharp
Body2 IGetBodies(
   System.int NCount
)
```

### C++/CLI

```cpp
Body2^ IGetBodies(
   System.int NCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NCount`: Number of bodies to move or rotate and copy

### Return Value

- in-process, unmanaged C++: Pointer to an array of [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) of size Count

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IMoveCopyBodyFeatureData::GetBodiesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMoveCopyBodyFeatureData~GetBodiesCount.html) before calling this method.

Use:

- [IMoveCopyBodyFeatureData::Copy](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMoveCopyBodyFeatureData~Copy.html) to get whether to copy the bodies
- [IMoveCopyBodyFeatureData::TransformType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMoveCopyBodyFeatureData~TransformType.html) to get whether to move or rotate the bodies

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IMoveCopyBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData.html)
[IMoveCopyBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData_members.html)
[IMoveCopyBodyFeatureData::ISetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~ISetBodies.html)
[IMoveCopyBodyFeatureData::Bodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~Bodies.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0

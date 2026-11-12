---
title: "ISetBodies Method (IMoveCopyBodyFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMoveCopyBodyFeatureData"
member: "ISetBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~ISetBodies.html"
---

# ISetBodies Method (IMoveCopyBodyFeatureData)

Sets the bodies to move or rotate and copy.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetBodies( _
   ByVal NCount As System.Integer, _
   ByRef PBodies As Body2 _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMoveCopyBodyFeatureData
Dim NCount As System.Integer
Dim PBodies As Body2

instance.ISetBodies(NCount, PBodies)
```

### C#

```csharp
void ISetBodies(
   System.int NCount,
   ref Body2 PBodies
)
```

### C++/CLI

```cpp
void ISetBodies(
   System.int NCount,
   Body2^% PBodies
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NCount`: Number of bodies to move or rotate and copy
- `PBodies`: - in-process, unmanaged C++: Pointer to an array of [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) of size Count

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Use:

- [IMoveCopyBodyFeatureData::Copy](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMoveCopyBodyFeatureData~Copy.html) to get whether to copy the bodies
- [IMoveCopyBodyFeatureData::TransformType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMoveCopyBodyFeatureData~TransformType.html) to get whether to move or rotate the bodies

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IMoveCopyBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData.html)
[IMoveCopyBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData_members.html)
[IMoveCopyBodyFeatureData::GetBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~GetBodiesCount.html)
[IMoveCopyBodyFeatureData::IGetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~IGetBodies.html)
[IMoveCopyBodyFeatureData::Bodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~Bodies.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0

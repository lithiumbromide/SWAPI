---
title: "ISetBodies Method (IScaleFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IScaleFeatureData"
member: "ISetBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~ISetBodies.html"
---

# ISetBodies Method (IScaleFeatureData)

Sets the bodies that are scaled in a multibody part.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetBodies( _
   ByVal Count As System.Integer, _
   ByRef BodyArr As Body2 _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IScaleFeatureData
Dim Count As System.Integer
Dim BodyArr As Body2

instance.ISetBodies(Count, BodyArr)
```

### C#

```csharp
void ISetBodies(
   System.int Count,
   ref Body2 BodyArr
)
```

### C++/CLI

```cpp
void ISetBodies(
   System.int Count,
   Body2^% BodyArr
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of bodies that are scaled
- `BodyArr`: - in-process, unmanaged C++: Pointer to an array of [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) that are scaled of size Count

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IScaleFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData.html)
[IScaleFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData_members.html)
[IScaleFeatureData::GetBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~GetBodiesCount.html)
[IScaleFeatureData::IGetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~IGetBodies.html)
[IScaleFeatureData::Bodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~Bodies.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0

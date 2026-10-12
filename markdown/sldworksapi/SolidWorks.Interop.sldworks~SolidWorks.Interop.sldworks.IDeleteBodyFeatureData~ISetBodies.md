---
title: "ISetBodies Method (IDeleteBodyFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDeleteBodyFeatureData"
member: "ISetBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData~ISetBodies.html"
---

# ISetBodies Method (IDeleteBodyFeatureData)

Sets the bodies to delete.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetBodies( _
   ByVal Count As System.Integer, _
   ByRef Bodies As Body2 _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IDeleteBodyFeatureData
Dim Count As System.Integer
Dim Bodies As Body2

instance.ISetBodies(Count, Bodies)
```

### C#

```csharp
void ISetBodies(
   System.int Count,
   ref Body2 Bodies
)
```

### C++/CLI

```cpp
void ISetBodies(
   System.int Count,
   Body2^% Bodies
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of bodies
- `Bodies`: - in-process, unmanaged C++: Pointer to an array of [IBody2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) objects of size count

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IDeleteBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData.html)
[IDeleteBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData_members.html)
[IDeleteBodyBodyFeatureData::GetBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData~GetBodiesCount.html)
[IDeleteBodyBodyFeatureData::IGetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData~IGetBodies.html)
[IDeleteBodyBodyFeatureData::Bodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData~Bodies.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0

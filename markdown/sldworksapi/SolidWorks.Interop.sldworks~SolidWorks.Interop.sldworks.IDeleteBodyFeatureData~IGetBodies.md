---
title: "IGetBodies Method (IDeleteBodyFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDeleteBodyFeatureData"
member: "IGetBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData~IGetBodies.html"
---

# IGetBodies Method (IDeleteBodyFeatureData)

Gets the bodies to delete.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetBodies( _
   ByVal Count As System.Integer _
) As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IDeleteBodyFeatureData
Dim Count As System.Integer
Dim value As Body2

value = instance.IGetBodies(Count)
```

### C#

```csharp
Body2 IGetBodies(
   System.int Count
)
```

### C++/CLI

```cpp
Body2^ IGetBodies(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of bodies

### Return Value

- in-process, unmanaged C++: Pointer to an array of [IBody2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) objects of size count

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IDeleteBodiesFeatureData::GetBodiesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDeleteBodyFeatureData~GetBodiesCount.html) before calling this method to get the number of bodies to delete.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IDeleteBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData.html)
[IDeleteBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData_members.html)
[IDeleteBodyFeatureData::ISetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData~ISetBodies.html)
[IDeleteBodyFeatureData::Bodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData~Bodies.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0

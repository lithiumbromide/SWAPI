---
title: "IGetBodies Method (IBodyFolder)"
project: "SOLIDWORKS API Help"
interface: "IBodyFolder"
member: "IGetBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~IGetBodies.html"
---

# IGetBodies Method (IBodyFolder)

Gets the bodies in the folder.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetBodies( _
   ByVal Count As System.Integer _
) As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IBodyFolder
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

- `Count`: Number of bodies in the folder

### Return Value

- in-process, unmanaged C++: Pointer to an array of [IBody2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) objects

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

This method gets the bodies in the folder; it does not get the bodies in any subfolders. See [Accessing Bodies in Body Folders](sldworksAPIProgGuide.chm::/OVERVIEW/Accessing_Bodies_in_Body_Folders.htm) for details about the BodyFolder interface.

To get the number of bodies in the folder, use [IBodyFolder::GetBodyCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBodyFolder~GetBodyCount.html) before using this method.

## See Also

[IBodyFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder.html)
[IBodyFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder_members.html)
[IBodyFolder::GetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~GetBodies.html)

## Availability

SOLIDWORKS 2005 SP2, Revision Number 13

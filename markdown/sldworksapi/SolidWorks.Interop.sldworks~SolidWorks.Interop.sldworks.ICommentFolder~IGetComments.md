---
title: "IGetComments Method (ICommentFolder)"
project: "SOLIDWORKS API Help"
interface: "ICommentFolder"
member: "IGetComments"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommentFolder~IGetComments.html"
---

# IGetComments Method (ICommentFolder)

Gets all of the comments in this folder.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetComments( _
   ByVal Count As System.Integer _
) As Comment
```

### Visual Basic (Usage)

```vb
Dim instance As ICommentFolder
Dim Count As System.Integer
Dim value As Comment

value = instance.IGetComments(Count)
```

### C#

```csharp
Comment IGetComments(
   System.int Count
)
```

### C++/CLI

```cpp
Comment^ IGetComments(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of comments in the folder

### Return Value

- in-process, unmanaged C++: Pointer to an array of [IComment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComment.html) objects

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Examples

Before calling this method, call [ICommentFolder::GetCommentCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommentFolder~GetCommentCount.html) before to determine the size of the array.

## See Also

[ICommentFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommentFolder.html)
[ICommentFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommentFolder_members.html)
[ICommentFolder::GetComments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommentFolder~GetComments.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14

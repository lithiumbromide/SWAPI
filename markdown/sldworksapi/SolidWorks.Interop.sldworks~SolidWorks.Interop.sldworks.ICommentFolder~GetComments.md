---
title: "GetComments Method (ICommentFolder)"
project: "SOLIDWORKS API Help"
interface: "ICommentFolder"
member: "GetComments"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommentFolder~GetComments.html"
---

# GetComments Method (ICommentFolder)

Gets all of the comments in this folder.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetComments() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICommentFolder
Dim value As System.Object

value = instance.GetComments()
```

### C#

```csharp
System.object GetComments()
```

### C++/CLI

```cpp
System.Object^ GetComments();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of all of the comments in the folder

## VBA Syntax

See [CommentFolder::GetComments](ms-its:sldworksapivb6.chm::/sldworks~CommentFolder~GetComments.html).

## Examples

[Get Comments in Comments Folder (C#)](Get_Comments_in_Comments_Folder_Example_CSharp.htm)
[Get Comments in Comments Folder (VB.NET)](Get_Comments_in_Comments_Folder_Example_VBNET.htm)
[Get Comments in Comments Folder (VBA)](Get_Comments_in_Comments_Folder_Example_VB.htm)

## See Also

[ICommentFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommentFolder.html)
[ICommentFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommentFolder_members.html)
[ICommentFolder::IGetComments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommentFolder~IGetComments.html)
[ICommentFolder::GetCommentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommentFolder~GetCommentCount.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14

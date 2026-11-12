---
title: "GetCommentCount Method (ICommentFolder)"
project: "SOLIDWORKS API Help"
interface: "ICommentFolder"
member: "GetCommentCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommentFolder~GetCommentCount.html"
---

# GetCommentCount Method (ICommentFolder)

Gets the number of comments in this folder.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCommentCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICommentFolder
Dim value As System.Integer

value = instance.GetCommentCount()
```

### C#

```csharp
System.int GetCommentCount()
```

### C++/CLI

```cpp
System.int GetCommentCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of comments in the folder

## VBA Syntax

See [CommentFolder::GetCommentCount](ms-its:sldworksapivb6.chm::/sldworks~CommentFolder~GetCommentCount.html).

## Examples

[Get Comments in Comments Folder (C#)](Get_Comments_in_Comments_Folder_Example_CSharp.htm)
[Get Comments in Comments Folder (VB.NET)](Get_Comments_in_Comments_Folder_Example_VBNET.htm)
[Get Comments in Comments Folder (VBA)](Get_Comments_in_Comments_Folder_Example_VB.htm)

## Remarks

Call this method before calling [ICommentFolder::IGetComments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommentFolder~IGetComments.html) to determine the size of the array for that method.

## See Also

[ICommentFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommentFolder.html)
[ICommentFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommentFolder_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14

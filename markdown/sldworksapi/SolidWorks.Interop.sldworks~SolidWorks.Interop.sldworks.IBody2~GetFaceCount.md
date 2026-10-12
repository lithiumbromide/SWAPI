---
title: "GetFaceCount Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "GetFaceCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetFaceCount.html"
---

# GetFaceCount Method (IBody2)

Gets the number of faces in this body.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFaceCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim value As System.Integer

value = instance.GetFaceCount()
```

### C#

```csharp
System.int GetFaceCount()
```

### C++/CLI

```cpp
System.int GetFaceCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of faces

## VBA Syntax

See [Body2::GetFaceCount](ms-its:sldworksapivb6.chm::/sldworks~Body2~GetFaceCount.html).

## Examples

[Process Body (C#)](Process_Body_Example_CSharp.htm)
[Process Body (VB.NET)](Process_Body_Example_VBNET.htm)
[Process Body (VBA)](Process_Body_Example_VB.htm)
[Fill Holes in Part (C#)](Fill_Holes_in_Part_Example_CSharp.htm)
[Fill Holes in Part (VB.NET)](Fill_Holes_in_Part_Example_VBNET.htm)
[Fill Holes in Part (VBA)](Fill_Holes_in_Part_Example_VB.htm)

## Remarks

Call this method before calling [IBody2::IGetFaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IGetFaces.html) to determine the size of the array for that method.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::GetFirstFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetFirstFace.html)
[IBody2::IGetFirstFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetFirstFace.html)
[IBody2::EnumFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~EnumFaces.html)
[IBody2::IDeleteFaces3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteFaces3.html)
[IBody2::IDeleteBlends2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteBlends2.html)
[IBody2::DeleteBlends2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteBlends2.html)
[IBody2::GetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetFaces.html)
[IBody2::IGetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetFaces.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

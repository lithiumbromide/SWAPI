---
title: "IsTemporaryBody Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "IsTemporaryBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IsTemporaryBody.html"
---

# IsTemporaryBody Method (IBody2)

Gets whether the body is a temporary body.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsTemporaryBody() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim value As System.Boolean

value = instance.IsTemporaryBody()
```

### C#

```csharp
System.bool IsTemporaryBody()
```

### C++/CLI

```cpp
System.bool IsTemporaryBody();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True the body is a temporary body, false if not

## VBA Syntax

See [Body2::IsTemporaryBody](ms-its:sldworksapivb6.chm::/sldworks~Body2~IsTemporaryBody.html).

## Examples

[Delete Faces (VBA)](Delete_Faces_Example_VB.htm)
[Create Loft Body (C#)](Create_Loft_Body_Example_CSharp.htm)
[Create Loft Body (VB.NET)](Create_Loft_Body_Example_VBNET.htm)
[Create Loft Body (VBA)](Create_Loft_Body_Example_VB.htm)
[Delete Blended Faces (C#)](Delete_Blended_Faces_Example_CSharp.htm)
[Delete Blended Faces (VB.NET)](Delete_Blended_Faces_Example_VBNET.htm)
[Delete Blended Faces (VBA)](Delete_Blended_Faces_Example_VB.htm)

## Remarks

You can select an entity from a temporary body. You can also assign colors to faces on temporary bodies and to entire temporary bodies. See [IBody2::Display3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~Display3.html) and [IFace2::MaterialPropertyValues](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~MaterialPropertyValues.html) or [IFace2::IMaterialPropertyValues](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~IMaterialPropertyValues.html) and [IBody2::MaterialPropertyValues2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~MaterialPropertyValues2.html) or [IBody2::IMaterialPropertyValues2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IMaterialPropertyValues2.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12

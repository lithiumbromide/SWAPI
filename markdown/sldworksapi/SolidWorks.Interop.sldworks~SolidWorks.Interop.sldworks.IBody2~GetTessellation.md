---
title: "GetTessellation Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "GetTessellation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetTessellation.html"
---

# GetTessellation Method (IBody2)

Gets the [ITessellation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITessellation.html) object.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTessellation( _
   ByVal FaceList As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim FaceList As System.Object
Dim value As System.Object

value = instance.GetTessellation(FaceList)
```

### C#

```csharp
System.object GetTessellation(
   System.object FaceList
)
```

### C++/CLI

```cpp
System.Object^ GetTessellation(
   System.Object^ FaceList
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FaceList`: Array of faces to tessellate; if this is empty, then SOLIDWORKS will tessellate the body

### Return Value

Object for the tessellation

## VBA Syntax

See [Body2::GetTessellation](ms-its:sldworksapivb6.chm::/sldworks~Body2~GetTessellation.html).

## Examples

[Create and Convert Non-manifold Bodies (C#)](Create_and_Convert_Non-manifold_Bodies_Example_CSharp.htm)
[Create and Convert Non-manifold Bodies (VB.NET)](Create_and_Convert_Non-manifold_Bodies_Example_VBNET.htm)
[Create and Convert Non-manifold Bodies (VBA)](Create_and_Convert_Non-manifold_Bodies_Example_VB.htm)

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::IGetTessellation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetTessellation.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

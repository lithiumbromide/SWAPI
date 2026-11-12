---
title: "IGetFirstFace Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "IGetFirstFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetFirstFace.html"
---

# IGetFirstFace Method (IBody2)

Finds the first face in a body and returns the face.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFirstFace() As Face2
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim value As Face2

value = instance.IGetFirstFace()
```

### C#

```csharp
Face2 IGetFirstFace()
```

### C++/CLI

```cpp
Face2^ IGetFirstFace();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

First [face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) in the body

## VBA Syntax

See [Body2::IGetFirstFace](ms-its:sldworksapivb6.chm::/sldworks~Body2~IGetFirstFace.html).

## Examples

[Traverse Bodies (C++)](Traverse_Bodies_Example_CPlusPlusCLI.htm)

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::GetFaceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetFaceCount.html)
[IBody2::GetFirstFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetFirstFace.html)
[IBody2::EnumFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~EnumFaces.html)
[IBody2::IDeleteBlends2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteBlends2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

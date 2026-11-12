---
title: "GetFaces Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "GetFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetFaces.html"
---

# GetFaces Method (IBody2)

Gets all of the faces on the body.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFaces() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim value As System.Object

value = instance.GetFaces()
```

### C#

```csharp
System.object GetFaces()
```

### C++/CLI

```cpp
System.Object^ GetFaces();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) on the body

## VBA Syntax

See [Body2::GetFaces](ms-its:sldworksapivb6.chm::/sldworks~Body2~GetFaces.html).

## Remarks

You can use this method instead of using [IBody2::GetFirstFace](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~GetFirstFace.html) and [IFace2::GetNextFace](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetNextFace.html) to get all of the faces on a body.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::IGetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetFaces.html)
[IBody2::GetFaceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetFaceCount.html)
[IBody2::IGetFirstFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetFirstFace.html)
[IBody2::GetFirstFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetFirstFace.html)

## Availability

SOLIDWORKS 2008 SP1, Revision Number 16.1

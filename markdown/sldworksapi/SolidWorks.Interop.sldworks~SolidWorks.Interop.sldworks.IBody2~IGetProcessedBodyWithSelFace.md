---
title: "IGetProcessedBodyWithSelFace Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "IGetProcessedBodyWithSelFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetProcessedBodyWithSelFace.html"
---

# IGetProcessedBodyWithSelFace Method (IBody2)

Gets a processed body.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetProcessedBodyWithSelFace() As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim value As Body2

value = instance.IGetProcessedBodyWithSelFace()
```

### C#

```csharp
Body2 IGetProcessedBodyWithSelFace()
```

### C++/CLI

```cpp
Body2^ IGetProcessedBodyWithSelFace();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the [IBody2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) object; this body is a copy of the body for this part

## VBA Syntax

See [Body2::IGetProcessedBodyWithSelFace](ms-its:sldworksapivb6.chm::/sldworks~Body2~IGetProcessedBodyWithSelFace.html).

## Remarks

This method requires that you preselect a face.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::GetProcessedBody2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetProcessedBody2.html)
[IBody2::GetProcessedBodyWithSelFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetProcessedBodyWithSelFace.html)
[IGetSelectedFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetSelectedFaces.html)
[IBody2::IGetNextSelectedFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetNextSelectedFace.html)
[IBody2::IGetFirstFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetFirstFace.html)
[IBody2::GetSelectedFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetSelectedFaces.html)
[IBody2::GetNextSelectedFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetNextSelectedFace.html)
[IBody2::GetFirstSelectedFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetFirstSelectedFace.html)
[IBody2::GetSelectedFaceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetSelectedFaceCount.html)

## Availability

SOLIDWORKS 2001Plus FCS Revision Number 10.0

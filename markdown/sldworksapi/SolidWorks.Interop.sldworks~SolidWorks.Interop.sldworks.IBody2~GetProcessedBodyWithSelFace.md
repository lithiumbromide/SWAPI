---
title: "GetProcessedBodyWithSelFace Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "GetProcessedBodyWithSelFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetProcessedBodyWithSelFace.html"
---

# GetProcessedBodyWithSelFace Method (IBody2)

Gets a processed body.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetProcessedBodyWithSelFace() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim value As System.Object

value = instance.GetProcessedBodyWithSelFace()
```

### C#

```csharp
System.object GetProcessedBodyWithSelFace()
```

### C++/CLI

```cpp
System.Object^ GetProcessedBodyWithSelFace();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Body, which is a copy of the body for this part

## VBA Syntax

See [Body2::GetProcessedBodyWithSelFace](ms-its:sldworksapivb6.chm::/sldworks~Body2~GetProcessedBodyWithSelFace.html).

## Examples

[Get Selected Faces on Processed Body (C#)](Get_Selected_Faces_on_Process_Body_Example_CSharp.htm)
[Get Selected Faces on Processed Body (VB.NET)](Get_Selected_Faces_on_Process_Body_Example_VBNET.htm)
[Get Selected Faces on Processed Body (VBA)](Get_Selected_Faces_on_Process_Body_Example_VB.htm)

## Remarks

This method requires that you preselect one or more faces.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::GetProcessedBody2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetProcessedBody2.html)
[IBody2::IGetProcessedBodyWithSelFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetProcessedBodyWithSelFace.html)
[GetFirstSelectedFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetFirstSelectedFace.html)
[IBody2::GetNextSelectedFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetNextSelectedFace.html)
[IBody2::GetSelectedFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetSelectedFaces.html)
[IBody2::IGetFirstSelectedFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetFirstSelectedFace.html)
[IBody2::IGetNextSelectedFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetNextSelectedFace.html)
[IBody2::IGetSelectedFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetSelectedFaces.html)
[IBody2::GetSelectedFaceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetSelectedFaceCount.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

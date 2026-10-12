---
title: "GetNextSelectedFace Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "GetNextSelectedFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetNextSelectedFace.html"
---

# GetNextSelectedFace Method (IBody2)

Gets the next selected face. For use with [IBody2::GetProcessedBodyWithSelFace](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~GetProcessedBodyWithSelFace.html) and intended for IGES routines.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNextSelectedFace() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim value As System.Object

value = instance.GetNextSelectedFace()
```

### C#

```csharp
System.object GetNextSelectedFace()
```

### C++/CLI

```cpp
System.Object^ GetNextSelectedFace();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Selected face

## VBA Syntax

See [Body2::GetNextSelectedFace](ms-its:sldworksapivb6.chm::/sldworks~Body2~GetNextSelectedFace.html).

## Remarks

Do not use this method for general selection handling. If you want to handle items selected by the user or items selected with [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html), use [ISelectionMgr::GetSelectedObject6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectedObject6.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::IGetNextSelectedFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetNextSelectedFace.html)
[IBody2::GetFirstSelectedFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetFirstSelectedFace.html)
[IBody2::GetSelectedFaceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetSelectedFaceCount.html)
[IBody2::GetProcessedBodyWithSelFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetProcessedBodyWithSelFace.html)
[IBody2::GetSelectedFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetSelectedFaces.html)
[IBody2::IGetFirstSelectedFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetFirstSelectedFace.html)
[IBody2::IGetProcessedBodyWithSelFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetProcessedBodyWithSelFace.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

---
title: "GetFirstSelectedFace Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "GetFirstSelectedFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetFirstSelectedFace.html"
---

# GetFirstSelectedFace Method (IBody2)

Gets the first selected face on this body. For use with [IBody2::GetProcessedBodyWithSelFace](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~GetProcessedBodyWithSelFace.html) and intended for IGES routines.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstSelectedFace() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim value As System.Object

value = instance.GetFirstSelectedFace()
```

### C#

```csharp
System.object GetFirstSelectedFace()
```

### C++/CLI

```cpp
System.Object^ GetFirstSelectedFace();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

First selected face

## VBA Syntax

See [Body2::GetFirstSelectedFace](ms-its:sldworksapivb6.chm::/sldworks~Body2~GetFirstSelectedFace.html).

## Remarks

Do not use this method for general selection handling. If you want to handle items selected by the user or items selected with [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html), use [ISelectionMgr::GetSelectedObject6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectedObject6.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::IGetFirstSelectedFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetFirstSelectedFace.html)
[IBody2::GetNextSelectedFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetNextSelectedFace.html)
[IBody2::GetSelectedFaceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetSelectedFaceCount.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

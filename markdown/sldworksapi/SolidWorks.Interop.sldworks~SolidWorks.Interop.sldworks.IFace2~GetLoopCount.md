---
title: "GetLoopCount Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "GetLoopCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetLoopCount.html"
---

# GetLoopCount Method (IFace2)

Gets the number of loops in this face.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLoopCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim value As System.Integer

value = instance.GetLoopCount()
```

### C#

```csharp
System.int GetLoopCount()
```

### C++/CLI

```cpp
System.int GetLoopCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of loops in this face

## VBA Syntax

See [Face2::GetLoopCount](ms-its:sldworksapivb6.chm::/sldworks~Face2~GetLoopCount.html).

## Examples

[Find Outside Edges of Face (VBA)](Find_Outside_Edges_of_Face_Example_VB.htm)
[Get Loops (VBA)](Get_Loops_Example_VB.htm)

## Remarks

Call this method before calling [IFace2::IGetLoops](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~IGetLoops.html) to determine the size of the array for that method.

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[ILoop2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.html)
[IFace2::GetFirstLoop Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetFirstLoop.html)
[IFace2::IGetFirstLoop Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetFirstLoop.html)
[ILoop2::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetNext.html)
[ILoop2::IGetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetNext.html)
[IFace2::GetLoops Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetLoops.html)
[IFace2::IGetLoops Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetLoops.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

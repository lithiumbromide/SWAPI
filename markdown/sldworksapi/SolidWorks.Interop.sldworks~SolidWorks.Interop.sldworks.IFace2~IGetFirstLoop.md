---
title: "IGetFirstLoop Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "IGetFirstLoop"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetFirstLoop.html"
---

# IGetFirstLoop Method (IFace2)

Gets the first loop in this face, which is not necessarily the outer loop.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFirstLoop() As Loop2
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim value As Loop2

value = instance.IGetFirstLoop()
```

### C#

```csharp
Loop2 IGetFirstLoop()
```

### C++/CLI

```cpp
Loop2^ IGetFirstLoop();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the first [loop](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2.html)

## VBA Syntax

See [Face2::IGetFirstLoop](ms-its:sldworksapivb6.chm::/sldworks~Face2~IGetFirstLoop.html).

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::GetFirstLoop Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetFirstLoop.html)
[IFace2::GetLoopCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetLoopCount.html)
[ILoop2::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetNext.html)
[ILoop2::IGetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetNext.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

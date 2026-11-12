---
title: "EnumLoops Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "EnumLoops"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~EnumLoops.html"
---

# EnumLoops Method (IFace2)

Enumerates the loops in a face.

## Syntax

### Visual Basic (Declaration)

```vb
Function EnumLoops() As EnumLoops2
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim value As EnumLoops2

value = instance.EnumLoops()
```

### C#

```csharp
EnumLoops2 EnumLoops()
```

### C++/CLI

```cpp
EnumLoops2^ EnumLoops();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the [loops enumeration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumLoops2.html)

## VBA Syntax

See [Face2::EnumLoops](ms-its:sldworksapivb6.chm::/sldworks~Face2~EnumLoops.html).

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::GetFirstLoop Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetFirstLoop.html)
[IFace2::GetLoopCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetLoopCount.html)
[IFace2::IGetFirstLoop Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetFirstLoop.html)
[IFace2::RemoveInnerLoops Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveInnerLoops.html)
[IFace2::IRemoveInnerLoops Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IRemoveInnerLoops.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

---
title: "IGetFace Method (ILoop2)"
project: "SOLIDWORKS API Help"
interface: "ILoop2"
member: "IGetFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetFace.html"
---

# IGetFace Method (ILoop2)

Gets the face containing this loop.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFace() As Face2
```

### Visual Basic (Usage)

```vb
Dim instance As ILoop2
Dim value As Face2

value = instance.IGetFace()
```

### C#

```csharp
Face2 IGetFace()
```

### C++/CLI

```cpp
Face2^ IGetFace();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

## VBA Syntax

See [Loop2::IGetFace](ms-its:sldworksapivb6.chm::/sldworks~Loop2~IGetFace.html).

## See Also

[ILoop2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.html)
[ILoop2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2_members.html)
[ILoop2::GetFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetFace.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

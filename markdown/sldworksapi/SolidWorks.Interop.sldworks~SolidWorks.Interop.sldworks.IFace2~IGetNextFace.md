---
title: "IGetNextFace Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "IGetNextFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetNextFace.html"
---

# IGetNextFace Method (IFace2)

Gets the next face in a body.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetNextFace() As Face2
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim value As Face2

value = instance.IGetNextFace()
```

### C#

```csharp
Face2 IGetNextFace()
```

### C++/CLI

```cpp
Face2^ IGetNextFace();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the next [face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) in a body

## VBA Syntax

See [Face2::IGetNextFace](ms-its:sldworksapivb6.chm::/sldworks~Face2~IGetNextFace.html).

## Examples

[Traverse Bodies (C++)](Traverse_Bodies_Example_CPlusPlusCLI.htm)

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::GetNextFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetNextFace.html)
[IBody2::GetFirstFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetFirstFace.html)
[IBody2::GetFirstSelectedFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetFirstSelectedFace.html)
[IBody2::IGetFirstFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetFirstFace.html)
[IBody2::IGetFirstSelectedFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetFirstSelectedFace.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

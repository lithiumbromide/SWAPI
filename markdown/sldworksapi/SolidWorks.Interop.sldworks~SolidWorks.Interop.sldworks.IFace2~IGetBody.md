---
title: "IGetBody Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "IGetBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetBody.html"
---

# IGetBody Method (IFace2)

Gets the body containing this face.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetBody() As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim value As Body2

value = instance.IGetBody()
```

### C#

```csharp
Body2 IGetBody()
```

### C++/CLI

```cpp
Body2^ IGetBody();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## VBA Syntax

See [Face2::IGetBody](ms-its:sldworksapivb6.chm::/sldworks~Face2~IGetBody.html).

## Examples

[Enumerate Bodies (C++)](Enumerate_Bodies_Example_CPlusPlus_COM.htm)

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::GetBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetBody.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number

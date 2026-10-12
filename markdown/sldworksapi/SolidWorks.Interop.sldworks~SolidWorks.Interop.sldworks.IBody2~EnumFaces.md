---
title: "EnumFaces Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "EnumFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~EnumFaces.html"
---

# EnumFaces Method (IBody2)

Returns an enumerated list of the faces in a body.

## Syntax

### Visual Basic (Declaration)

```vb
Function EnumFaces() As EnumFaces2
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim value As EnumFaces2

value = instance.EnumFaces()
```

### C#

```csharp
EnumFaces2 EnumFaces()
```

### C++/CLI

```cpp
EnumFaces2^ EnumFaces();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Enumerated list of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) (see **Remarks**)

## VBA Syntax

See [Body2::EnumFaces](ms-its:sldworksapivb6.chm::/sldworks~Body2~EnumFaces.html).

## Examples

[Enumerate Bodies (C++)](Enumerate_Bodies_Example_CPlusPlus_COM.htm)

## Remarks

OLE automation applications should use [IBody2::GetFirstFace](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetNextFace.html) and [IFace2::GetNextFace](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IGetFirstFace.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

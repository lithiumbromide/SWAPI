---
title: "CreateNewSurface Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "CreateNewSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateNewSurface.html"
---

# CreateNewSurface Method (IBody2)

Creates a handle for a new surface to serve as geometry for a face to be added to the body.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateNewSurface() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim value As System.Object

value = instance.CreateNewSurface()
```

### C#

```csharp
System.object CreateNewSurface()
```

### C++/CLI

```cpp
System.Object^ CreateNewSurface();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

New surface

## VBA Syntax

See [Body2::CreateNewSurface](ms-its:sldworksapivb6.chm::/sldworks~Body2~CreateNewSurface.html).

## Remarks

This method is the first in a set of related functions that construct a body from trimmed surfaces. Internally, this function also creates a list that SOLIDWORKS uses as a place-holder for trimming curves used to trim the surface to the desired shape.

Any existing object created by this method is destroyed if you call this method again.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::ICreateNewSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateNewSurface.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

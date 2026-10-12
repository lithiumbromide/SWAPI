---
title: "ICreateTempBodyFromSurfaces Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "ICreateTempBodyFromSurfaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateTempBodyFromSurfaces.html"
---

# ICreateTempBodyFromSurfaces Method (IBody2)

Creates a temporary body from a list of existing trimmed surfaces.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateTempBodyFromSurfaces() As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim value As Body2

value = instance.ICreateTempBodyFromSurfaces()
```

### C#

```csharp
Body2 ICreateTempBodyFromSurfaces()
```

### C++/CLI

```cpp
Body2^ ICreateTempBodyFromSurfaces();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Temporary [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## VBA Syntax

See [Body2::ICreateTempBodyFromSurfaces](ms-its:sldworksapivb6.chm::/sldworks~Body2~ICreateTempBodyFromSurfaces.html).

## Remarks

This method is the final call to a set of related functions (same as [IBody2::CreateBodyFromSurfaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~CreateBodyFromSurfaces.html)) that are designed to construct a temporary body from trimmed surfaces.

The first call in this process should be to [IPartDoc::CreateNewBody2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~ICreateNewBody2.html), so as to arrange for a placeholder for all the trimmed surfaces.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::CreateTempBodyFromSurfaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateTempBodyFromSurfaces.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

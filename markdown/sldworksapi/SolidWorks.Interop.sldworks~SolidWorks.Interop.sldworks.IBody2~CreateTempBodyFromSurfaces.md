---
title: "CreateTempBodyFromSurfaces Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "CreateTempBodyFromSurfaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateTempBodyFromSurfaces.html"
---

# CreateTempBodyFromSurfaces Method (IBody2)

Creates a temporary body from a list of existing trimmed surfaces.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateTempBodyFromSurfaces() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim value As System.Object

value = instance.CreateTempBodyFromSurfaces()
```

### C#

```csharp
System.object CreateTempBodyFromSurfaces()
```

### C++/CLI

```cpp
System.Object^ CreateTempBodyFromSurfaces();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Body

## VBA Syntax

See [Body2::CreateTempBodyFromSurfaces](ms-its:sldworksapivb6.chm::/sldworks~Body2~CreateTempBodyFromSurfaces.html).

## Remarks

This method is the final call to a set of related functions (same as [IBody2::CreateBodyFromSurfaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~CreateBodyFromSurfaces.html)) that are designed to construct a temporary body from trimmed surfaces.

The first call in this process should be to [IPartDoc::CreateNewBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~CreateNewBody.html), so as to arrange for a placeholder for all the trimmed surfaces.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::ICreateTempBodyFromSurfaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateTempBodyFromSurfaces.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

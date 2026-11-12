---
title: "EnumRelatedBodies2 Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "EnumRelatedBodies2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~EnumRelatedBodies2.html"
---

# EnumRelatedBodies2 Method (IPartDoc)

Creates an enumerated list of bodies.

## Syntax

### Visual Basic (Declaration)

```vb
Function EnumRelatedBodies2() As EnumBodies2
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim value As EnumBodies2

value = instance.EnumRelatedBodies2()
```

### C#

```csharp
EnumBodies2 EnumRelatedBodies2()
```

### C++/CLI

```cpp
EnumBodies2^ EnumRelatedBodies2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Enumerated list of bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumBodies2.html)

## VBA Syntax

See [PartDoc::EnumRelatedBodies2](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~EnumRelatedBodies2.html).

## Remarks

The list contains only those bodies associated with reference surfaces. The list does not include the part body itself.

A reference surface feature can consist of one or more surfaces sewn together. Each reference surface feature has two [IBody2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) objects:

- One represents the front face or faces
- One represents the back face or faces

Each IBody2 object has one or more faces depending on whether the reference surface feature is a set of knitted surfaces or a single underlying surface. The corresponding faces for each body pair should have normal vectors that are opposite.

To use the enumerated list, see [IEnumBodies2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumBodies2.html) functions.

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IPartDoc::EnumBodies3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~EnumBodies3.html)
[IPartDoc::EnumRelatedSectionedBodies2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~EnumRelatedSectionedBodies2.html)
[IPartDoc::GetRelatedBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetRelatedBodies.html)
[IPartDoc::GetRelatedSectionedBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetRelatedSectionedBodies.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

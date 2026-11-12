---
title: "GetRelatedBodies Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "GetRelatedBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetRelatedBodies.html"
---

# GetRelatedBodies Method (IPartDoc)

Creates a list of all the related bodies in a part.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRelatedBodies() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim value As System.Object

value = instance.GetRelatedBodies()
```

### C#

```csharp
System.object GetRelatedBodies()
```

### C++/CLI

```cpp
System.Object^ GetRelatedBodies();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of related bodies

## VBA Syntax

See [PartDoc::GetRelatedBodies](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~GetRelatedBodies.html).

## Remarks

The list contains only those bodies associated with reference surfaces. What results is a list of bodies, which is related to the model, but it does not include the part body itself.

A reference surface feature can consist of one or more surfaces knitted together. Each reference surface feature has two [IBody2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) objects:

- One for the front faces
- One for the back faces

Each IBody2 object has one or more faces depending on whether the reference surface feature is a set of knitted surfaces or a single underlying surface. The corresponding faces for each body pair should have normal vectors that are opposite.

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IPartDoc::EnumBodies3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~EnumBodies3.html)
[IPartDoc::EnumRelatedSectionedBodies2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~EnumRelatedSectionedBodies2.html)
[IPartDoc::EnumRelatedBodies2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~EnumRelatedBodies2.html)
[IPartDoc::GetRelatedSectionedBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetRelatedSectionedBodies.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0

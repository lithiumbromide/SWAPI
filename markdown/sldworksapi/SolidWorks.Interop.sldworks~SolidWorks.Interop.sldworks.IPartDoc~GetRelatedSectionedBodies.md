---
title: "GetRelatedSectionedBodies Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "GetRelatedSectionedBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetRelatedSectionedBodies.html"
---

# GetRelatedSectionedBodies Method (IPartDoc)

Gets all of the related sectioned bodies in a part.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRelatedSectionedBodies( _
   ByVal ViewIn As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim ViewIn As System.Object
Dim value As System.Object

value = instance.GetRelatedSectionedBodies(ViewIn)
```

### C#

```csharp
System.object GetRelatedSectionedBodies(
   System.object ViewIn
)
```

### C++/CLI

```cpp
System.Object^ GetRelatedSectionedBodies(
   System.Object^ ViewIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ViewIn`: [Model view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView.html)

### Return Value

Array of related sectioned bodies.

## VBA Syntax

See [PartDoc::GetRelatedSectionedBodies](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~GetRelatedSectionedBodies.html).

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IPartDoc::EnumBodies3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~EnumBodies3.html)
[IPartDoc::EnumRelatedBodies2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~EnumRelatedBodies2.html)
[IPartDoc::EnumRelatedSectionedBodies2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~EnumRelatedSectionedBodies2.html)
[IPartDoc::GetRelatedBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetRelatedBodies.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0

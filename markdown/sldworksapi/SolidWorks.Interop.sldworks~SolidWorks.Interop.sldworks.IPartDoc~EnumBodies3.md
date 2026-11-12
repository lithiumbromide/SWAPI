---
title: "EnumBodies3 Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "EnumBodies3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~EnumBodies3.html"
---

# EnumBodies3 Method (IPartDoc)

Enumerates the bodies in this part.

## Syntax

### Visual Basic (Declaration)

```vb
Function EnumBodies3( _
   ByVal BodyType As System.Integer, _
   ByVal BVisibleOnly As System.Boolean _
) As EnumBodies2
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim BodyType As System.Integer
Dim BVisibleOnly As System.Boolean
Dim value As EnumBodies2

value = instance.EnumBodies3(BodyType, BVisibleOnly)
```

### C#

```csharp
EnumBodies2 EnumBodies3(
   System.int BodyType,
   System.bool BVisibleOnly
)
```

### C++/CLI

```cpp
EnumBodies2^ EnumBodies3(
   System.int BodyType,
   System.bool BVisibleOnly
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BodyType`: Type of body as defined in [swBodyType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBodyType_e.html)
- `BVisibleOnly`: True gets only visible bodies, false gets all bodies

### Return Value

[Enumerated list of bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumBodies2.html)

## VBA Syntax

See [PartDoc::EnumBodies3](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~EnumBodies3.html).

## Remarks

To use the enumerated list, see [IEnumBodies2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumBodies2.html) functions.

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IPartDoc::EnumRelatedBodies2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~EnumRelatedBodies2.html)
[IPartDoc::EnumRelatedSectionedBodies2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~EnumRelatedSectionedBodies2.html)
[IPartDoc::GetRelatedBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetRelatedBodies.html)
[IPartDoc::GetRelatedSectionedBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetRelatedSectionedBodies.html)
[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0

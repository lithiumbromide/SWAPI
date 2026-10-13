---
title: "EnumBodies3 Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "EnumBodies3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~EnumBodies3.html"
---

# EnumBodies3 Method (IComponent2)

Gets the bodies in the component in a multibody part.

## Syntax

### Visual Basic (Declaration)

```vb
Function EnumBodies3( _
   ByVal BodyType As System.Integer, _
   ByVal VisibleOnly As System.Boolean _
) As EnumBodies2
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim BodyType As System.Integer
Dim VisibleOnly As System.Boolean
Dim value As EnumBodies2

value = instance.EnumBodies3(BodyType, VisibleOnly)
```

### C#

```csharp
EnumBodies2 EnumBodies3(
   System.int BodyType,
   System.bool VisibleOnly
)
```

### C++/CLI

```cpp
EnumBodies2^ EnumBodies3(
   System.int BodyType,
   System.bool VisibleOnly
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BodyType`: Type of body as defined by [swBodyType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBodyType_e.html)
- `VisibleOnly`: True to get visible bodies only, false to get all bodies

### Return Value

[Enumerated list of bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumBodies2.html)

## VBA Syntax

See [Component2::EnumBodies3](ms-its:sldworksapivb6.chm::/sldworks~Component2~EnumBodies3.html).

## Remarks

This method only supports solid and sheet (surface) types.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::EnumRelatedBodies Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~EnumRelatedBodies.html)
[IComponent2::EnumSectionedBodies Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~EnumSectionedBodies.html)
[IComponent2::GetBodies3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetBodies3.html)
[IComponent2::GetBody Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetBody.html)
[IComponent2::IGetBody Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetBody.html)
[IPartDoc::EnumBodies3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~EnumBodies3.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0

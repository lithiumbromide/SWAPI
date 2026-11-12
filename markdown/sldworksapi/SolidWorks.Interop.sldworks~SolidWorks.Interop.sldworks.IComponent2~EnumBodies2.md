---
title: "EnumBodies2 Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "EnumBodies2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~EnumBodies2.html"
---

# EnumBodies2 Method (IComponent2)

Obsolete. Superseded by [IComponent2::EnumBodies3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~EnumBodies3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function EnumBodies2( _
   ByVal BodyType As System.Integer _
) As EnumBodies2
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim BodyType As System.Integer
Dim value As EnumBodies2

value = instance.EnumBodies2(BodyType)
```

### C#

```csharp
EnumBodies2 EnumBodies2(
   System.int BodyType
)
```

### C++/CLI

```cpp
EnumBodies2^ EnumBodies2(
   System.int BodyType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BodyType`: Type of body as defined by [swBodyType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBodyType_e.html)

### Return Value

[Enumerated list of bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumBodies2.html)

## VBA Syntax

See [Component2::EnumBodies2](ms-its:sldworksapivb6.chm::/sldworks~Component2~EnumBodies2.html).

## Remarks

This method only supports solid and sheet (surface) body types.

The difference between this method and the now obsolete IComponent2::EnumBodies is that the new method supports lightweight components. The now obsolete IComponent2::EnumBodies does not.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::GetBodies3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetBodies3.html)
[IComponent2::GetBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetBody.html)
[IComponent2::IGetBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetBody.html)

## Availability

SOLIDWORKS 2006 SP2, Revision Number 14.2

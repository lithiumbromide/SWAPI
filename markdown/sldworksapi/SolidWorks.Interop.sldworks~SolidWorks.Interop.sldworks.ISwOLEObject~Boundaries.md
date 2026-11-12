---
title: "Boundaries Property (ISwOLEObject)"
project: "SOLIDWORKS API Help"
interface: "ISwOLEObject"
member: "Boundaries"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~Boundaries.html"
---

# Boundaries Property (ISwOLEObject)

Gets or sets the boundaries for this OLE object.

## Syntax

### Visual Basic (Declaration)

```vb
Property Boundaries As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwOLEObject
Dim value As System.Object

instance.Boundaries = value

value = instance.Boundaries
```

### C#

```csharp
System.object Boundaries {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Boundaries {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of these coordinates:

- Drawings: sheet coordinates
- Parts or assemblies: screen pixel coordinates

## VBA Syntax

See [SwOLEObject::Boundaries](ms-its:sldworksapivb6.chm::/sldworks~SwOLEObject~Boundaries.html).

## See Also

[ISwOLEObject Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject.html)
[ISwOLEObject Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject_members.html)
[ISwOLEObject::IGetBoundaries Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~IGetBoundaries.html)
[ISwOLEObject::ISetBoundaries Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~ISetBoundaries.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0

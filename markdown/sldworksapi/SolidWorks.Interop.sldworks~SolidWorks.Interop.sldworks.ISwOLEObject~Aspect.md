---
title: "Aspect Property (ISwOLEObject)"
project: "SOLIDWORKS API Help"
interface: "ISwOLEObject"
member: "Aspect"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~Aspect.html"
---

# Aspect Property (ISwOLEObject)

Gets the viewing aspect for this OLE object.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Aspect As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwOLEObject
Dim value As System.Integer

value = instance.Aspect
```

### C#

```csharp
System.int Aspect {get;}
```

### C++/CLI

```cpp
property System.int Aspect {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Viewing aspect as defined in the DVASPECT enumeration (see Remarks)

## VBA Syntax

See [SwOLEObject::Aspect](ms-its:sldworksapivb6.chm::/sldworks~SwOLEObject~Aspect.html).

## Examples

See the [ISwOLEObject](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject.html) examples.

## Remarks

The ViewingAspect argument uses the DVASPECT enumeration, which has the following values:

- DVASPECT_CONTENT = 1
- DVASPECT_THUMBNAIL = 2
- DVASPECT_ICON = 4
- DVASPECT_DOCPRINT = 8

See the MSDN documentation for additional details about the DVASPECT enumeration.

## See Also

[ISwOLEObject Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject.html)
[ISwOLEObject Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0

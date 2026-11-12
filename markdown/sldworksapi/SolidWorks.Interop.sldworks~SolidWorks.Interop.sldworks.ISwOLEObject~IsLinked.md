---
title: "IsLinked Property (ISwOLEObject)"
project: "SOLIDWORKS API Help"
interface: "ISwOLEObject"
member: "IsLinked"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~IsLinked.html"
---

# IsLinked Property (ISwOLEObject)

Gets whether the OLE objects are linked to external files or not.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IsLinked As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwOLEObject
Dim value As System.Boolean

value = instance.IsLinked
```

### C#

```csharp
System.bool IsLinked {get;}
```

### C++/CLI

```cpp
property System.bool IsLinked {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the OLE objects are linked to external files, false if they are embedded

## VBA Syntax

See [SwOLEObject::IsLinked](ms-its:sldworksapivb6.chm::/sldworks~SwOLEObject~IsLinked.html).

## Examples

See the [ISwOLEObject](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject.html) examples.

## Examples

[Determine If OLE Objects are Linked or Embedded (VBA)](Determine_if_OLE_Objects_are_Linked_or_Embedded_Example_VB.htm)

## See Also

[ISwOLEObject Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject.html)
[ISwOLEObject Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject_members.html)
[ISwOLEObject::FileName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~FileName.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0

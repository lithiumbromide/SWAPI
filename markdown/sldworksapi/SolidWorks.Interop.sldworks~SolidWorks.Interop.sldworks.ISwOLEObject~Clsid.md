---
title: "Clsid Property (ISwOLEObject)"
project: "SOLIDWORKS API Help"
interface: "ISwOLEObject"
member: "Clsid"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~Clsid.html"
---

# Clsid Property (ISwOLEObject)

Gets the class ID of this OLE object.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Clsid As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwOLEObject
Dim value As System.String

value = instance.Clsid
```

### C#

```csharp
System.string Clsid {get;}
```

### C++/CLI

```cpp
property System.String^ Clsid {
   System.String^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Either an alpha-numeric string or the class ID of the host application

## VBA Syntax

See [SwOLEObject::Clsid](ms-its:sldworksapivb6.chm::/sldworks~SwOLEObject~Clsid.html).

## Examples

See the [ISwOLEObject](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject.html) examples.

## See Also

[ISwOLEObject Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject.html)
[ISwOLEObject Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0

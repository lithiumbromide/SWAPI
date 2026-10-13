---
title: "Buffer Property (ISwOLEObject)"
project: "SOLIDWORKS API Help"
interface: "ISwOLEObject"
member: "Buffer"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~Buffer.html"
---

# Buffer Property (ISwOLEObject)

Gets the data for this OLE object.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Buffer As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwOLEObject
Dim value As System.Object

value = instance.Buffer
```

### C#

```csharp
System.object Buffer {get;}
```

### C++/CLI

```cpp
property System.Object^ Buffer {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of buffer data

## VBA Syntax

See [SwOLEObject::Buffer](ms-its:sldworksapivb6.chm::/sldworks~SwOLEObject~Buffer.html).

## See Also

[ISwOLEObject Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject.html)
[ISwOLEObject Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject_members.html)
[ISwOLEObject::IGetBuffer Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~IGetBuffer.html)
[ISwOLEObject::BufferSize Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~BufferSize.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0

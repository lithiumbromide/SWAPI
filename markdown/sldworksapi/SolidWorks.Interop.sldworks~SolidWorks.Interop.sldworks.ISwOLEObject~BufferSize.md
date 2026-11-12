---
title: "BufferSize Property (ISwOLEObject)"
project: "SOLIDWORKS API Help"
interface: "ISwOLEObject"
member: "BufferSize"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~BufferSize.html"
---

# BufferSize Property (ISwOLEObject)

Gets the size of the OLE object data.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property BufferSize As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwOLEObject
Dim value As System.Integer

value = instance.BufferSize
```

### C#

```csharp
System.int BufferSize {get;}
```

### C++/CLI

```cpp
property System.int BufferSize {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Size of the OLE object data

## VBA Syntax

See [SwOLEObject::BufferSize](ms-its:sldworksapivb6.chm::/sldworks~SwOLEObject~BufferSize.html).

## Examples

See the [ISwOLEObject](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject.html) examples.

## Remarks

Call this method before calling [ISwOLEObject::IGetBuffer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISwOLEObject~IGetBuffer.html) to get the size of the array for that method.

## See Also

[ISwOLEObject Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject.html)
[ISwOLEObject Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject_members.html)
[ISwOLEObject::Buffer Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~Buffer.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0

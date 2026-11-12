---
title: "IGetBuffer Method (ISwOLEObject)"
project: "SOLIDWORKS API Help"
interface: "ISwOLEObject"
member: "IGetBuffer"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~IGetBuffer.html"
---

# IGetBuffer Method (ISwOLEObject)

Gets the data for this OLE object.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IGetBuffer( _
   ByVal OleBufferSize As System.Integer, _
   ByRef BOleData As System.Byte _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISwOLEObject
Dim OleBufferSize As System.Integer
Dim BOleData As System.Byte

instance.IGetBuffer(OleBufferSize, BOleData)
```

### C#

```csharp
void IGetBuffer(
   System.int OleBufferSize,
   out System.byte BOleData
)
```

### C++/CLI

```cpp
void IGetBuffer(
   System.int OleBufferSize,
   [Out] System.byte BOleData
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `OleBufferSize`: Size of the OLE buffer
- `BOleData`: Byte array for the buffer data

## VBA Syntax

See [SwOLEObject::IGetBuffer](ms-its:sldworksapivb6.chm::/sldworks~SwOLEObject~IGetBuffer.html).

## Remarks

Before calling this method, call [ISwOLEObject::BufferSize](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISwOLEObject~BufferSize.html) to get the value for OleBufferSize.

## See Also

[ISwOLEObject Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject.html)
[ISwOLEObject Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject_members.html)
[ISwOLEObject::Buffer Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~Buffer.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0

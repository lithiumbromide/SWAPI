---
title: "IGetOLEObjectSettings Method (ISheet)"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: "IGetOLEObjectSettings"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~IGetOLEObjectSettings.html"
---

# IGetOLEObjectSettings Method (ISheet)

Obsolete. Superseded by [ISwOLEObjectAspect](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISwOLEObject~Aspect.html), [ISwOLEObject::Boundaries](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISwOLEObject~Boundaries.html), [ISWOLEObject::IGetBoundaries](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISwOLEObject~IGetBoundaries.html), [ISwOLEObject::ISetBoundaries](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISwOLEObject~ISetBoundaries.html), [ISwOLEObject::IGetBuffer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISwOLEObject~IGetBuffer.html), and [ISwOLEObject::Buffer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISwOLEObject~Buffer.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetOLEObjectSettings( _
   ByVal Index As System.Integer, _
   ByRef ByteCount As System.Integer, _
   ByRef Aspect As System.Integer, _
   ByRef Position As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
Dim Index As System.Integer
Dim ByteCount As System.Integer
Dim Aspect As System.Integer
Dim Position As System.Double
Dim value As System.Boolean

value = instance.IGetOLEObjectSettings(Index, ByteCount, Aspect, Position)
```

### C#

```csharp
System.bool IGetOLEObjectSettings(
   System.int Index,
   out System.int ByteCount,
   out System.int Aspect,
   out System.double Position
)
```

### C++/CLI

```cpp
System.bool IGetOLEObjectSettings(
   System.int Index,
   [Out] System.int ByteCount,
   [Out] System.int Aspect,
   [Out] System.double Position
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`:
- `ByteCount`:
- `Aspect`:
- `Position`:

## VBA Syntax

See [Sheet::IGetOLEObjectSettings](ms-its:sldworksapivb6.chm::/sldworks~Sheet~IGetOLEObjectSettings.html).

## See Also

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)

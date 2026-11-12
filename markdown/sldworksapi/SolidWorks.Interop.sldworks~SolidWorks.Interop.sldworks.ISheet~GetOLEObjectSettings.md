---
title: "GetOLEObjectSettings Method (ISheet)"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: "GetOLEObjectSettings"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetOLEObjectSettings.html"
---

# GetOLEObjectSettings Method (ISheet)

Obsolete. Superseded by I[SwOLEObjectAspect](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISwOLEObject~Aspect.html), [ISwOLEObject::Boundaries](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISwOLEObject~Boundaries.html), [ISWOLEObject::IGetBoundaries](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISwOLEObject~IGetBoundaries.html), [ISwOLEObject::ISetBoundaries](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISwOLEObject~ISetBoundaries.html), [ISwOLEObject::IGetBuffer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISwOLEObject~IGetBuffer.html), and [ISwOLEObject::Buffer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISwOLEObject~Buffer.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetOLEObjectSettings( _
   ByVal Index As System.Integer, _
   ByRef ByteCount As System.Integer, _
   ByRef Aspect As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
Dim Index As System.Integer
Dim ByteCount As System.Integer
Dim Aspect As System.Integer
Dim value As System.Object

value = instance.GetOLEObjectSettings(Index, ByteCount, Aspect)
```

### C#

```csharp
System.object GetOLEObjectSettings(
   System.int Index,
   out System.int ByteCount,
   out System.int Aspect
)
```

### C++/CLI

```cpp
System.Object^ GetOLEObjectSettings(
   System.int Index,
   [Out] System.int ByteCount,
   [Out] System.int Aspect
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`:
- `ByteCount`:
- `Aspect`:

## VBA Syntax

See [Sheet::GetOLEObjectSettings](ms-its:sldworksapivb6.chm::/sldworks~Sheet~GetOLEObjectSettings.html).

## See Also

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)

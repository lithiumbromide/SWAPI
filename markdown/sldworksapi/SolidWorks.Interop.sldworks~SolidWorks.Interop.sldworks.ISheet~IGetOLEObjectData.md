---
title: "IGetOLEObjectData Method (ISheet)"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: "IGetOLEObjectData"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~IGetOLEObjectData.html"
---

# IGetOLEObjectData Method (ISheet)

Obsolete. Superseded by [ISwOLEObject](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISwOLEObject.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetOLEObjectData( _
   ByVal Index As System.Integer, _
   ByRef Buffer As System.Byte _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
Dim Index As System.Integer
Dim Buffer As System.Byte
Dim value As System.Boolean

value = instance.IGetOLEObjectData(Index, Buffer)
```

### C#

```csharp
System.bool IGetOLEObjectData(
   System.int Index,
   out System.byte Buffer
)
```

### C++/CLI

```cpp
System.bool IGetOLEObjectData(
   System.int Index,
   [Out] System.byte Buffer
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`:
- `Buffer`:

## VBA Syntax

See [Sheet::IGetOLEObjectData](ms-its:sldworksapivb6.chm::/sldworks~Sheet~IGetOLEObjectData.html).

## See Also

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)

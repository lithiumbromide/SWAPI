---
title: "GetOLEObjectData Method (ISheet)"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: "GetOLEObjectData"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetOLEObjectData.html"
---

# GetOLEObjectData Method (ISheet)

Obsolete. Superseded by [ISwOLEObject](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISwOLEObject.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetOLEObjectData( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
Dim Index As System.Integer
Dim value As System.Object

value = instance.GetOLEObjectData(Index)
```

### C#

```csharp
System.object GetOLEObjectData(
   System.int Index
)
```

### C++/CLI

```cpp
System.Object^ GetOLEObjectData(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`:

## VBA Syntax

See [Sheet::GetOLEObjectData](ms-its:sldworksapivb6.chm::/sldworks~Sheet~GetOLEObjectData.html).

## See Also

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)

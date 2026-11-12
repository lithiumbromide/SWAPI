---
title: "ICreateOLEObject Method (ISheet)"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: "ICreateOLEObject"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~ICreateOLEObject.html"
---

# ICreateOLEObject Method (ISheet)

Obsolete. Superseded by [IModelDocExtension::CreateOLEObject](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~CreateOLEObject.html) and [IModelDocExtension::ICreateOLEObject](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~ICreateOLEObject.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateOLEObject( _
   ByVal Aspect As System.Integer, _
   ByRef Position As System.Double, _
   ByVal ByteCount As System.Integer, _
   ByRef Buffer As System.Byte _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
Dim Aspect As System.Integer
Dim Position As System.Double
Dim ByteCount As System.Integer
Dim Buffer As System.Byte
Dim value As System.Boolean

value = instance.ICreateOLEObject(Aspect, Position, ByteCount, Buffer)
```

### C#

```csharp
System.bool ICreateOLEObject(
   System.int Aspect,
   ref System.double Position,
   System.int ByteCount,
   ref System.byte Buffer
)
```

### C++/CLI

```cpp
System.bool ICreateOLEObject(
   System.int Aspect,
   System.double% Position,
   System.int ByteCount,
   System.byte% Buffer
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Aspect`:
- `Position`:
- `ByteCount`:
- `Buffer`:

## VBA Syntax

See [Sheet::ICreateOLEObject](ms-its:sldworksapivb6.chm::/sldworks~Sheet~ICreateOLEObject.html).

## See Also

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)

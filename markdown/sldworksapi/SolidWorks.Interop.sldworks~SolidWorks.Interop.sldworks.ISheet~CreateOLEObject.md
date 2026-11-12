---
title: "CreateOLEObject Method (ISheet)"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: "CreateOLEObject"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~CreateOLEObject.html"
---

# CreateOLEObject Method (ISheet)

Obsolete. Superseded by [IModelDocExtension::CreateOLEObject](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~CreateOLEObject.html) and [IModelDocExtension::ICreateOLEObject](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~ICreateOLEObject.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateOLEObject( _
   ByVal Aspect As System.Integer, _
   ByVal Position As System.Object, _
   ByVal Buffer As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
Dim Aspect As System.Integer
Dim Position As System.Object
Dim Buffer As System.Object
Dim value As System.Boolean

value = instance.CreateOLEObject(Aspect, Position, Buffer)
```

### C#

```csharp
System.bool CreateOLEObject(
   System.int Aspect,
   System.object Position,
   System.object Buffer
)
```

### C++/CLI

```cpp
System.bool CreateOLEObject(
   System.int Aspect,
   System.Object^ Position,
   System.Object^ Buffer
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Aspect`:
- `Position`:
- `Buffer`:

## VBA Syntax

See [Sheet::CreateOLEObject](ms-its:sldworksapivb6.chm::/sldworks~Sheet~CreateOLEObject.html).

## See Also

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)

---
title: "IGetPersistReference Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "IGetPersistReference"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetPersistReference.html"
---

# IGetPersistReference Method (IModelDocExtension)

Obsolete. Superseded by [IModelDocExtension::IGetPersistReference3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~IGetPersistReference3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetPersistReference( _
   ByVal DipsObj As System.Object, _
   ByVal Count As System.Integer _
) As System.Byte
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim DipsObj As System.Object
Dim Count As System.Integer
Dim value As System.Byte

value = instance.IGetPersistReference(DipsObj, Count)
```

### C#

```csharp
System.byte IGetPersistReference(
   System.object DipsObj,
   System.int Count
)
```

### C++/CLI

```cpp
System.byte IGetPersistReference(
   System.Object^ DipsObj,
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DipsObj`:
- `Count`:

### Return Value

## VBA Syntax

See [ModelDocExtension::IGetPersistReference](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~IGetPersistReference.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

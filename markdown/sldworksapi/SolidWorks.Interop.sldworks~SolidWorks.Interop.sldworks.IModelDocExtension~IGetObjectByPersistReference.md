---
title: "IGetObjectByPersistReference Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "IGetObjectByPersistReference"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetObjectByPersistReference.html"
---

# IGetObjectByPersistReference Method (IModelDocExtension)

Obsolete. Superseded by [IModelDocExtension::IGetObjectByPersistReference3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~IGetObjectByPersistReference3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetObjectByPersistReference( _
   ByVal Count As System.Integer, _
   ByRef PersistId As System.Byte _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Count As System.Integer
Dim PersistId As System.Byte
Dim value As System.Object

value = instance.IGetObjectByPersistReference(Count, PersistId)
```

### C#

```csharp
System.object IGetObjectByPersistReference(
   System.int Count,
   ref System.byte PersistId
)
```

### C++/CLI

```cpp
System.Object^ IGetObjectByPersistReference(
   System.int Count,
   System.byte% PersistId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`:
- `PersistId`:

## VBA Syntax

See [ModelDocExtension::IGetObjectByPersistReference](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~IGetObjectByPersistReference.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

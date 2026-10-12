---
title: "GetObjectByPersistReference2 Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetObjectByPersistReference2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetObjectByPersistReference2.html"
---

# GetObjectByPersistReference2 Method (IModelDocExtension)

Obsolete. Superseded by [IModelDocExtension::GetObjectByPersistReference3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetObjectByPersistReference3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetObjectByPersistReference2( _
   ByVal PersistId As System.Object, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim PersistId As System.Object
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetObjectByPersistReference2(PersistId, ErrorCode)
```

### C#

```csharp
System.object GetObjectByPersistReference2(
   System.object PersistId,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetObjectByPersistReference2(
   System.Object^ PersistId,
   [Out] System.int ErrorCode
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PersistId`:
- `ErrorCode`: v

## VBA Syntax

See [ModelDocExtension::GetObjectByPersistReference2](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetObjectByPersistReference2.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

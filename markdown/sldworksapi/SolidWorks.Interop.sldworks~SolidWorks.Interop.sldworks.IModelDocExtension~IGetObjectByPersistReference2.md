---
title: "IGetObjectByPersistReference2 Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "IGetObjectByPersistReference2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetObjectByPersistReference2.html"
---

# IGetObjectByPersistReference2 Method (IModelDocExtension)

Obsolete. Superseded by [IModelDocExtension::IGetObjectByPersistReference3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~IGetObjectByPersistReference3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetObjectByPersistReference2( _
   ByVal Count As System.Integer, _
   ByRef PersistId As System.Byte, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Count As System.Integer
Dim PersistId As System.Byte
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.IGetObjectByPersistReference2(Count, PersistId, ErrorCode)
```

### C#

```csharp
System.object IGetObjectByPersistReference2(
   System.int Count,
   ref System.byte PersistId,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ IGetObjectByPersistReference2(
   System.int Count,
   System.byte% PersistId,
   [Out] System.int ErrorCode
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`:
- `PersistId`:
- `ErrorCode`:

## VBA Syntax

See [ModelDocExtension::IGetObjectByPersistReference2](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~IGetObjectByPersistReference2.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2007 SP3, Revision Number 15.3

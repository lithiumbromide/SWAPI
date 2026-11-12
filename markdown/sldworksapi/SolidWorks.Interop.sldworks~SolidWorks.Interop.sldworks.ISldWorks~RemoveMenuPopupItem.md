---
title: "RemoveMenuPopupItem Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "RemoveMenuPopupItem"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveMenuPopupItem.html"
---

# RemoveMenuPopupItem Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::RemoveMenuPopupItem2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~RemoveMenuPopupItem2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveMenuPopupItem( _
   ByVal DocType As System.Integer, _
   ByVal SelectType As System.Integer, _
   ByVal Item As System.String, _
   ByVal CallbackFcnAndModule As System.String, _
   ByVal CustomNames As System.String, _
   ByVal Unused As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim DocType As System.Integer
Dim SelectType As System.Integer
Dim Item As System.String
Dim CallbackFcnAndModule As System.String
Dim CustomNames As System.String
Dim Unused As System.Integer
Dim value As System.Boolean

value = instance.RemoveMenuPopupItem(DocType, SelectType, Item, CallbackFcnAndModule, CustomNames, Unused)
```

### C#

```csharp
System.bool RemoveMenuPopupItem(
   System.int DocType,
   System.int SelectType,
   System.string Item,
   System.string CallbackFcnAndModule,
   System.string CustomNames,
   System.int Unused
)
```

### C++/CLI

```cpp
System.bool RemoveMenuPopupItem(
   System.int DocType,
   System.int SelectType,
   System.String^ Item,
   System.String^ CallbackFcnAndModule,
   System.String^ CustomNames,
   System.int Unused
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DocType`:
- `SelectType`:
- `Item`:
- `CallbackFcnAndModule`:
- `CustomNames`:
- `Unused`:

## VBA Syntax

See [SldWorks::RemoveMenuPopupItem](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~RemoveMenuPopupItem.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

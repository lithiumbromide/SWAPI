---
title: "AddMenuPopupItem Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "AddMenuPopupItem"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuPopupItem.html"
---

# AddMenuPopupItem Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::AddMenuPopupItem2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~AddMenuPopupItem2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddMenuPopupItem( _
   ByVal DocType As System.Integer, _
   ByVal SelType As System.Integer, _
   ByVal Item As System.String, _
   ByVal CallbackFcnAndModule As System.String, _
   ByVal CustomNames As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim DocType As System.Integer
Dim SelType As System.Integer
Dim Item As System.String
Dim CallbackFcnAndModule As System.String
Dim CustomNames As System.String
Dim value As System.Integer

value = instance.AddMenuPopupItem(DocType, SelType, Item, CallbackFcnAndModule, CustomNames)
```

### C#

```csharp
System.int AddMenuPopupItem(
   System.int DocType,
   System.int SelType,
   System.string Item,
   System.string CallbackFcnAndModule,
   System.string CustomNames
)
```

### C++/CLI

```cpp
System.int AddMenuPopupItem(
   System.int DocType,
   System.int SelType,
   System.String^ Item,
   System.String^ CallbackFcnAndModule,
   System.String^ CustomNames
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DocType`:
- `SelType`:
- `Item`:
- `CallbackFcnAndModule`:
- `CustomNames`:

## VBA Syntax

See [SldWorks::AddMenuPopupItem](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~AddMenuPopupItem.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

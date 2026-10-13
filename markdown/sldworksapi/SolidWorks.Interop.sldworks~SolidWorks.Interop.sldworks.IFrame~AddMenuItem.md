---
title: "AddMenuItem Method (IFrame)"
project: "SOLIDWORKS API Help"
interface: "IFrame"
member: "AddMenuItem"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuItem.html"
---

# AddMenuItem Method (IFrame)

Obsolete. Superseded by [IFrame::AddMenuItem2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFrame~AddMenuItem2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddMenuItem( _
   ByVal Menu As System.String, _
   ByVal Item As System.String, _
   ByVal Position As System.Integer, _
   ByVal CallbackFcnAndModule As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFrame
Dim Menu As System.String
Dim Item As System.String
Dim Position As System.Integer
Dim CallbackFcnAndModule As System.String
Dim value As System.Boolean

value = instance.AddMenuItem(Menu, Item, Position, CallbackFcnAndModule)
```

### C#

```csharp
System.bool AddMenuItem(
   System.string Menu,
   System.string Item,
   System.int Position,
   System.string CallbackFcnAndModule
)
```

### C++/CLI

```cpp
System.bool AddMenuItem(
   System.String^ Menu,
   System.String^ Item,
   System.int Position,
   System.String^ CallbackFcnAndModule
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Menu`:
- `Item`:
- `Position`:
- `CallbackFcnAndModule`:

## VBA Syntax

See [Frame::AddMenuItem](ms-its:sldworksapivb6.chm::/sldworks~Frame~AddMenuItem.html).

## See Also

[IFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.html)
[IFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.html)

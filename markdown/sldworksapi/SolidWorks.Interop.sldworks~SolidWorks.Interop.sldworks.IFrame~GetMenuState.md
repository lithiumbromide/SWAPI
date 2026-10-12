---
title: "GetMenuState Method (IFrame)"
project: "SOLIDWORKS API Help"
interface: "IFrame"
member: "GetMenuState"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetMenuState.html"
---

# GetMenuState Method (IFrame)

Obsolete. Superseded by [IFrame::AddMenuItem2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFrame~AddMenuItem2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMenuState( _
   ByVal MenuItemString As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFrame
Dim MenuItemString As System.String
Dim value As System.Integer

value = instance.GetMenuState(MenuItemString)
```

### C#

```csharp
System.int GetMenuState(
   System.string MenuItemString
)
```

### C++/CLI

```cpp
System.int GetMenuState(
   System.String^ MenuItemString
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `MenuItemString`:

## VBA Syntax

See [Frame::GetMenuState](ms-its:sldworksapivb6.chm::/sldworks~Frame~GetMenuState.html).

## See Also

[IFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.html)
[IFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.html)

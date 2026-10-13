---
title: "RemoveUserMenu Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "RemoveUserMenu"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveUserMenu.html"
---

# RemoveUserMenu Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::RemoveMenu](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~RemoveMenu.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveUserMenu( _
   ByVal DocType As System.Integer, _
   ByVal MenuIdIn As System.Integer, _
   ByVal ModuleName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim DocType As System.Integer
Dim MenuIdIn As System.Integer
Dim ModuleName As System.String
Dim value As System.Boolean

value = instance.RemoveUserMenu(DocType, MenuIdIn, ModuleName)
```

### C#

```csharp
System.bool RemoveUserMenu(
   System.int DocType,
   System.int MenuIdIn,
   System.string ModuleName
)
```

### C++/CLI

```cpp
System.bool RemoveUserMenu(
   System.int DocType,
   System.int MenuIdIn,
   System.String^ ModuleName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DocType`:
- `MenuIdIn`:
- `ModuleName`:

## VBA Syntax

See [SldWorks::RemoveUserMenu](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~RemoveUserMenu.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

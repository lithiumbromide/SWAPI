---
title: "AddMenuItem Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "AddMenuItem"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuItem.html"
---

# AddMenuItem Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::AddMenuItem3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~AddMenuItem3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddMenuItem( _
   ByVal DocType As System.Integer, _
   ByVal Menu As System.String, _
   ByVal Postion As System.Integer, _
   ByVal CallbackModuleAndFcn As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim DocType As System.Integer
Dim Menu As System.String
Dim Postion As System.Integer
Dim CallbackModuleAndFcn As System.String
Dim value As System.Integer

value = instance.AddMenuItem(DocType, Menu, Postion, CallbackModuleAndFcn)
```

### C#

```csharp
System.int AddMenuItem(
   System.int DocType,
   System.string Menu,
   System.int Postion,
   System.string CallbackModuleAndFcn
)
```

### C++/CLI

```cpp
System.int AddMenuItem(
   System.int DocType,
   System.String^ Menu,
   System.int Postion,
   System.String^ CallbackModuleAndFcn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DocType`:
- `Menu`:
- `Postion`:
- `CallbackModuleAndFcn`:

## VBA Syntax

See [SldWorks::AddMenuItem](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~AddMenuItem.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

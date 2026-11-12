---
title: "CreateTaskpaneView Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "CreateTaskpaneView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CreateTaskpaneView.html"
---

# CreateTaskpaneView Method (ISldWorks)

Obsolete. Superseded by [ISldworks::CreateTaskpaneView2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~CreateTaskpaneView2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateTaskpaneView( _
   ByRef Bitmap As System.Integer, _
   ByVal ToolTip As System.String, _
   ByVal PHandler As System.Object _
) As TaskpaneView
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Bitmap As System.Integer
Dim ToolTip As System.String
Dim PHandler As System.Object
Dim value As TaskpaneView

value = instance.CreateTaskpaneView(Bitmap, ToolTip, PHandler)
```

### C#

```csharp
TaskpaneView CreateTaskpaneView(
   ref System.int Bitmap,
   System.string ToolTip,
   System.object PHandler
)
```

### C++/CLI

```cpp
TaskpaneView^ CreateTaskpaneView(
   System.int% Bitmap,
   System.String^ ToolTip,
   System.Object^ PHandler
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Bitmap`:
- `ToolTip`:
- `PHandler`:

## VBA Syntax

See [SldWorks::CreateTaskpaneView](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~CreateTaskpaneView.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

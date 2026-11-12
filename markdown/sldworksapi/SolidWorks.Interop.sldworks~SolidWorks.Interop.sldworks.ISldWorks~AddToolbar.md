---
title: "AddToolbar Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "AddToolbar"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbar.html"
---

# AddToolbar Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::AddToolbar4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~AddToolbar4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddToolbar( _
   ByVal ModuleName As System.String, _
   ByVal Title As System.String, _
   ByVal SmallBitmapHandle As System.Integer, _
   ByVal LargeBitmapHandle As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim ModuleName As System.String
Dim Title As System.String
Dim SmallBitmapHandle As System.Integer
Dim LargeBitmapHandle As System.Integer
Dim value As System.Integer

value = instance.AddToolbar(ModuleName, Title, SmallBitmapHandle, LargeBitmapHandle)
```

### C#

```csharp
System.int AddToolbar(
   System.string ModuleName,
   System.string Title,
   System.int SmallBitmapHandle,
   System.int LargeBitmapHandle
)
```

### C++/CLI

```cpp
System.int AddToolbar(
   System.String^ ModuleName,
   System.String^ Title,
   System.int SmallBitmapHandle,
   System.int LargeBitmapHandle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ModuleName`:
- `Title`:
- `SmallBitmapHandle`:
- `LargeBitmapHandle`:

## VBA Syntax

See [SldWorks::AddToolbar](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~AddToolbar.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

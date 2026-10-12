---
title: "AddToolbar2 Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "AddToolbar2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbar2.html"
---

# AddToolbar2 Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::AddToolbar4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~AddToolbar4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddToolbar2( _
   ByVal ModuleNameIn As System.String, _
   ByVal TitleIn As System.String, _
   ByVal SmallBitmapHandleIn As System.Integer, _
   ByVal LargeBitmapHandleIn As System.Integer, _
   ByVal MenuPosIn As System.Integer, _
   ByVal DecTemplateTypeIn As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim ModuleNameIn As System.String
Dim TitleIn As System.String
Dim SmallBitmapHandleIn As System.Integer
Dim LargeBitmapHandleIn As System.Integer
Dim MenuPosIn As System.Integer
Dim DecTemplateTypeIn As System.Integer
Dim value As System.Integer

value = instance.AddToolbar2(ModuleNameIn, TitleIn, SmallBitmapHandleIn, LargeBitmapHandleIn, MenuPosIn, DecTemplateTypeIn)
```

### C#

```csharp
System.int AddToolbar2(
   System.string ModuleNameIn,
   System.string TitleIn,
   System.int SmallBitmapHandleIn,
   System.int LargeBitmapHandleIn,
   System.int MenuPosIn,
   System.int DecTemplateTypeIn
)
```

### C++/CLI

```cpp
System.int AddToolbar2(
   System.String^ ModuleNameIn,
   System.String^ TitleIn,
   System.int SmallBitmapHandleIn,
   System.int LargeBitmapHandleIn,
   System.int MenuPosIn,
   System.int DecTemplateTypeIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ModuleNameIn`:
- `TitleIn`:
- `SmallBitmapHandleIn`:
- `LargeBitmapHandleIn`:
- `MenuPosIn`:
- `DecTemplateTypeIn`:

## VBA Syntax

See [SldWorks::AddToolbar2](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~AddToolbar2.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

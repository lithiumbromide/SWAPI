---
title: "Clone Method (IEnumBodies)"
project: "SOLIDWORKS API Help"
interface: "IEnumBodies"
member: "Clone"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumBodies~Clone.html"
---

# Clone Method (IEnumBodies)

Obsolete. Superseded by [IEnumBodies2::Clone](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumBodies2~Clone.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub Clone( _
   ByRef Ppenum As EnumBodies _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumBodies
Dim Ppenum As EnumBodies

instance.Clone(Ppenum)
```

### C#

```csharp
void Clone(
   out EnumBodies Ppenum
)
```

### C++/CLI

```cpp
void Clone(
   [Out] EnumBodies^ Ppenum
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Ppenum`:

## VBA Syntax

See [EnumBodies::Clone](ms-its:sldworksapivb6.chm::/sldworks~EnumBodies~Clone.html).

## See Also

[IEnumBodies Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumBodies.html)
[IEnumBodies Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumBodies_members.html)

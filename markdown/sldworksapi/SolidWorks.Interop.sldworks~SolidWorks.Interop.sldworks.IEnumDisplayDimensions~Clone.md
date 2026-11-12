---
title: "Clone Method (IEnumDisplayDimensions)"
project: "SOLIDWORKS API Help"
interface: "IEnumDisplayDimensions"
member: "Clone"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDisplayDimensions~Clone.html"
---

# Clone Method (IEnumDisplayDimensions)

Clones the display dimensions enumeration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Clone( _
   ByRef Ppenum As EnumDisplayDimensions _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumDisplayDimensions
Dim Ppenum As EnumDisplayDimensions

instance.Clone(Ppenum)
```

### C#

```csharp
void Clone(
   out EnumDisplayDimensions Ppenum
)
```

### C++/CLI

```cpp
void Clone(
   [Out] EnumDisplayDimensions^ Ppenum
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Ppenum`: Pointer to the cloned [display dimensions enumeration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumDisplayDimensions.html)

## VBA Syntax

See [EnumDisplayDimensions::Clone](ms-its:sldworksapivb6.chm::/sldworks~EnumDisplayDimensions~Clone.html).

## Remarks

For use in in-process DLLs only.

## See Also

[IEnumDisplayDimensions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDisplayDimensions.html)
[IEnumDisplayDimensions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDisplayDimensions_members.html)

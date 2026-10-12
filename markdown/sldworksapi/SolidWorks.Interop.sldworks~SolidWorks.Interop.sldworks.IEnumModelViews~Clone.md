---
title: "Clone Method (IEnumModelViews)"
project: "SOLIDWORKS API Help"
interface: "IEnumModelViews"
member: "Clone"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumModelViews~Clone.html"
---

# Clone Method (IEnumModelViews)

Clones the model views enumeration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Clone( _
   ByRef Ppenum As EnumModelViews _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumModelViews
Dim Ppenum As EnumModelViews

instance.Clone(Ppenum)
```

### C#

```csharp
void Clone(
   out EnumModelViews Ppenum
)
```

### C++/CLI

```cpp
void Clone(
   [Out] EnumModelViews^ Ppenum
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Ppenum`: Pointer to the model views enumeration

## VBA Syntax

See [EnumModelViews::Clone](ms-its:sldworksapivb6.chm::/sldworks~EnumModelViews~Clone.html).

## Remarks

For use in in-process DLLs only.

## See Also

[IEnumModelViews Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumModelViews.html)
[IEnumModelViews Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumModelViews_members.html)

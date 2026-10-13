---
title: "Skip Method (IEnumModelViews)"
project: "SOLIDWORKS API Help"
interface: "IEnumModelViews"
member: "Skip"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumModelViews~Skip.html"
---

# Skip Method (IEnumModelViews)

Skips the specified number of model views in the model views enumeration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Skip( _
   ByVal Celt As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumModelViews
Dim Celt As System.Integer

instance.Skip(Celt)
```

### C#

```csharp
void Skip(
   System.int Celt
)
```

### C++/CLI

```cpp
void Skip(
   System.int Celt
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Celt`: Number of model views to skip

## VBA Syntax

See [EnumModelViews::Skip](ms-its:sldworksapivb6.chm::/sldworks~EnumModelViews~Skip.html).

## Remarks

For use in in-process DLLs only.

## See Also

[IEnumModelViews Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumModelViews.html)
[IEnumModelViews Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumModelViews_members.html)

---
title: "Clone Method (IEnumComponents)"
project: "SOLIDWORKS API Help"
interface: "IEnumComponents"
member: "Clone"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumComponents~Clone.html"
---

# Clone Method (IEnumComponents)

Obsolete. Superseded by [IEnumComponents2::Clone](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumComponents2~Clone.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub Clone( _
   ByRef Ppenum As EnumComponents _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumComponents
Dim Ppenum As EnumComponents

instance.Clone(Ppenum)
```

### C#

```csharp
void Clone(
   out EnumComponents Ppenum
)
```

### C++/CLI

```cpp
void Clone(
   [Out] EnumComponents^ Ppenum
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Ppenum`:

## VBA Syntax

See [EnumComponents::Clone](ms-its:sldworksapivb6.chm::/sldworks~EnumComponents~Clone.html).

## See Also

[IEnumComponents Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumComponents.html)
[IEnumComponents Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumComponents_members.html)

---
title: "Clone Method (IEnumDocuments2)"
project: "SOLIDWORKS API Help"
interface: "IEnumDocuments2"
member: "Clone"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDocuments2~Clone.html"
---

# Clone Method (IEnumDocuments2)

Clones the documents enumeration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Clone( _
   ByRef Ppenum As EnumDocuments2 _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumDocuments2
Dim Ppenum As EnumDocuments2

instance.Clone(Ppenum)
```

### C#

```csharp
void Clone(
   out EnumDocuments2 Ppenum
)
```

### C++/CLI

```cpp
void Clone(
   [Out] EnumDocuments2^ Ppenum
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Ppenum`: Pointer to the cloned [documents enumeration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumDocuments2.html)

## VBA Syntax

See [EnumDocuments2::Clone](ms-its:sldworksapivb6.chm::/sldworks~EnumDocuments2~Clone.html).

## Remarks

For use in in-process DLLs only.

## See Also

[IEnumDocuments2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDocuments2.html)
[IEnumDocuments2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDocuments2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

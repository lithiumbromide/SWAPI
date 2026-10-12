---
title: "Skip Method (IEnumDocuments2)"
project: "SOLIDWORKS API Help"
interface: "IEnumDocuments2"
member: "Skip"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDocuments2~Skip.html"
---

# Skip Method (IEnumDocuments2)

Skips the specified number of documents in the documents enumeration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Skip( _
   ByVal Celt As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumDocuments2
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

- `Celt`: Number of documents to skip

## VBA Syntax

See [EnumDocuments2::Skip](ms-its:sldworksapivb6.chm::/sldworks~EnumDocuments2~Skip.html).

## Remarks

For use in in-process DLLs only.

## See Also

[IEnumDocuments2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDocuments2.html)
[IEnumDocuments2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDocuments2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

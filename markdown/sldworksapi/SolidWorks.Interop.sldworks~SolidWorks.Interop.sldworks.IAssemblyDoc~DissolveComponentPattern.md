---
title: "DissolveComponentPattern Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "DissolveComponentPattern"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~DissolveComponentPattern.html"
---

# DissolveComponentPattern Method (IAssemblyDoc)

Dissolves the selected component patterns.

## Syntax

### Visual Basic (Declaration)

```vb
Function DissolveComponentPattern() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim value As System.Boolean

value = instance.DissolveComponentPattern()
```

### C#

```csharp
System.bool DissolveComponentPattern()
```

### C++/CLI

```cpp
System.bool DissolveComponentPattern();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the selected component patterns are dissolved, false if not

## VBA Syntax

See [AssemblyDoc::DissolveComponentPattern](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~DissolveComponentPattern.html).

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12

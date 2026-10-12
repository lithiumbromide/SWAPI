---
title: "DissolveSubAssembly Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "DissolveSubAssembly"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~DissolveSubAssembly.html"
---

# DissolveSubAssembly Method (IAssemblyDoc)

Dissolves the selected subassembly in this assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function DissolveSubAssembly() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim value As System.Boolean

value = instance.DissolveSubAssembly()
```

### C#

```csharp
System.bool DissolveSubAssembly()
```

### C++/CLI

```cpp
System.bool DissolveSubAssembly();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the subassembly was successfully dissolved, false if not

## VBA Syntax

See [AssemblyDoc::DissolveSubAssembly](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~DissolveSubAssembly.html).

## Remarks

You must preselect the subassembly to dissolve when you run this method.

This method automatically deletes any features that need to be deleted as a result of the dissolve operation, without input from the user.

This method closes any component files when called in an assembly. If the components were modified, then those modifications are not automatically saved. You must save any modifications before the files are closed.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

---
title: "ExitIsolate Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "ExitIsolate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ExitIsolate.html"
---

# ExitIsolate Method (IAssemblyDoc)

Exits [isolating the selected components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~Isolate.html) and returns the assembly to its original display state.

## Syntax

### Visual Basic (Declaration)

```vb
Function ExitIsolate() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim value As System.Boolean

value = instance.ExitIsolate()
```

### C#

```csharp
System.bool ExitIsolate()
```

### C++/CLI

```cpp
System.bool ExitIsolate();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if isolating the selected component exits and the assembly returns to its original display state, false if not

## VBA Syntax

See [AssemblyDoc::ExitIsolate](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~ExitIsolate.html).

## Examples

[Isolate Component (C#)](Isolate_Component_Example_CSharp.htm)
[Isolate Component (VB.NET)](Isolate_Component_Example_VBNET.htm)
[Isolate Component (VBA)](Isolate_Component_Example_VB.htm)

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::SaveIsolate Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SaveIsolate.html)
[IAssemblyDoc::SetIsolateVisibility Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetIsolateVisibility.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0

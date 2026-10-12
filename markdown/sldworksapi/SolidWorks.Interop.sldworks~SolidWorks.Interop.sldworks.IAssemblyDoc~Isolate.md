---
title: "Isolate Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "Isolate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~Isolate.html"
---

# Isolate Method (IAssemblyDoc)

Isolates the selected components.

## Syntax

### Visual Basic (Declaration)

```vb
Function Isolate() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim value As System.Boolean

value = instance.Isolate()
```

### C#

```csharp
System.bool Isolate()
```

### C++/CLI

```cpp
System.bool Isolate();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the selected components are isolated, false if not

## VBA Syntax

See [AssemblyDoc::Isolate](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~Isolate.html).

## Examples

[Isolate Component (C#)](Isolate_Component_Example_CSharp.htm)
[Isolate Component (VB.NET)](Isolate_Component_Example_VBNET.htm)
[Isolate Component (VBA)](Isolate_Component_Example_VB.htm)

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::ExitIsolate Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ExitIsolate.html)
[IAssemblyDoc::SaveIsolate Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SaveIsolate.html)
[IAssemblyDoc::SetIsolateVisibility Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetIsolateVisibility.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0

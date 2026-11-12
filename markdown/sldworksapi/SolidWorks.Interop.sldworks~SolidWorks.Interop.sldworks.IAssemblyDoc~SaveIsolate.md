---
title: "SaveIsolate Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "SaveIsolate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SaveIsolate.html"
---

# SaveIsolate Method (IAssemblyDoc)

Saves the display characteristics of the [isolated components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~Isolate.html) to a new display state.

## Syntax

### Visual Basic (Declaration)

```vb
Function SaveIsolate( _
   ByVal Name As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim Name As System.String
Dim value As System.Boolean

value = instance.SaveIsolate(Name)
```

### C#

```csharp
System.bool SaveIsolate(
   System.string Name
)
```

### C++/CLI

```cpp
System.bool SaveIsolate(
   System.String^ Name
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Name of the new display state to which to save the characteristics of the isolated components

### Return Value

True if a new display state of the characteristics of the isolated components is created, false if not

## VBA Syntax

See [AssemblyDoc::SaveIsolate](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~SaveIsolate.html).

## Examples

[Isolate Component (C#)](Isolate_Component_Example_CSharp.htm)
[Isolate Component (VB.NET)](Isolate_Component_Example_VBNET.htm)
[Isolate Component (VBA)](Isolate_Component_Example_VB.htm)

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::ExitIsolate Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ExitIsolate.html)
[IAssemblyDoc::SetIsolateVisibility Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetIsolateVisibility.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0

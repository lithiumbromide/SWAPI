---
title: "AddPipingFitting Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "AddPipingFitting"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddPipingFitting.html"
---

# AddPipingFitting Method (IAssemblyDoc)

Adds a pipe fitting to the current piping assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddPipingFitting( _
   ByVal PathName As System.String, _
   ByVal ConfigName As System.String, _
   ByVal AlignmentIndex As System.Short _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim PathName As System.String
Dim ConfigName As System.String
Dim AlignmentIndex As System.Short
Dim value As System.Boolean

value = instance.AddPipingFitting(PathName, ConfigName, AlignmentIndex)
```

### C#

```csharp
System.bool AddPipingFitting(
   System.string PathName,
   System.string ConfigName,
   System.short AlignmentIndex
)
```

### C++/CLI

```cpp
System.bool AddPipingFitting(
   System.String^ PathName,
   System.String^ ConfigName,
   System.short AlignmentIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PathName`: Full name and directory location of part file used for this fitting
- `ConfigName`: Configuration within the fitting part file which should be used
- `AlignmentIndex`: Each fitting has a varying number of alignment positions; this value allows you to choose the alignment position

### Return Value

True if successful, false otherwise

## VBA Syntax

See [AssemblyDoc::AddPipingFitting](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~AddPipingFitting.html).

## Remarks

This method adds a piping fitting to the selected sketch point. The sketch must be the active sketch of the piping assembly.

The alignmentIndex argument controls the alignment of the fitting. For example, you can align a t-piece in two ways: passing 0 aligns the t-piece one way, and passing 1 aligns it the other way.

If the routing DLL is not available, then COM returns ITF_E_ROUTINGNOTLOADED.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::AddPipePenetration Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddPipePenetration.html)

## Availability

SOLIDWORKS 99, datecode 1999207

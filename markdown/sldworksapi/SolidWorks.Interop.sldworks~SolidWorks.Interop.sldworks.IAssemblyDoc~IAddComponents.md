---
title: "IAddComponents Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "IAddComponents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IAddComponents.html"
---

# IAddComponents Method (IAssemblyDoc)

Obsolete. Superseded by [IAssemblyDoc::IAddComponents2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~IAddComponents2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IAddComponents( _
   ByRef Count As System.Integer, _
   ByRef Names As System.String, _
   ByRef Transforms As System.Double _
) As Component
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim Count As System.Integer
Dim Names As System.String
Dim Transforms As System.Double
Dim value As Component

value = instance.IAddComponents(Count, Names, Transforms)
```

### C#

```csharp
Component IAddComponents(
   ref System.int Count,
   ref System.string Names,
   ref System.double Transforms
)
```

### C++/CLI

```cpp
Component^ IAddComponents(
   System.int% Count,
   System.String^% Names,
   System.double% Transforms
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`:
- `Names`:
- `Transforms`:

## VBA Syntax

See [AssemblyDoc::IAddComponents](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~IAddComponents.html).

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)

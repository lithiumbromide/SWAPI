---
title: "IsComponentTreeValid Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "IsComponentTreeValid"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IsComponentTreeValid.html"
---

# IsComponentTreeValid Method (IAssemblyDoc)

Checks the validity of the component tree for this assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsComponentTreeValid() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim value As System.Boolean

value = instance.IsComponentTreeValid()
```

### C#

```csharp
System.bool IsComponentTreeValid()
```

### C++/CLI

```cpp
System.bool IsComponentTreeValid();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the component tree is currently valid, false if the tree is currently invalid

## VBA Syntax

See [AssemblyDoc::IsComponentTreeValid](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~IsComponentTreeValid.html).

## Remarks

In certain cases, the current assembly component tree is invalid.

- You cannot query the assembly for a list of components [(IComponent2::GetChildren](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetChildren.html)) or use existing IComponent2 objects to make function calls.
- If you use the IComponent2 object's methods, then this method returns a NULL or empty value.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)

## Availability

SOLIDWORKS 99, datecode 1999207

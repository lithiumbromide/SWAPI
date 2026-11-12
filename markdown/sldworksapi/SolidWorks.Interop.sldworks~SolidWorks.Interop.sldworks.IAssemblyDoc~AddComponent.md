---
title: "AddComponent Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "AddComponent"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddComponent.html"
---

# AddComponent Method (IAssemblyDoc)

Obsolete. Superseded by [IAssemblyDoc::AddComponent4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~AddComponent4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddComponent( _
   ByVal CompName As System.String, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim CompName As System.String
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Boolean

value = instance.AddComponent(CompName, X, Y, Z)
```

### C#

```csharp
System.bool AddComponent(
   System.string CompName,
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
System.bool AddComponent(
   System.String^ CompName,
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CompName`:
- `X`:
- `Y`:
- `Z`:

## VBA Syntax

See [AssemblyDoc::AddComponent](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~AddComponent.html).

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)

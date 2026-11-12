---
title: "AddComponent2 Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "AddComponent2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddComponent2.html"
---

# AddComponent2 Method (IAssemblyDoc)

Obsolete. Superseded by [IAssemblyDoc::AddComponent4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~AddComponent4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddComponent2( _
   ByVal CompName As System.String, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim CompName As System.String
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Object

value = instance.AddComponent2(CompName, X, Y, Z)
```

### C#

```csharp
System.object AddComponent2(
   System.string CompName,
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
System.Object^ AddComponent2(
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

See [AssemblyDoc::AddComponent2](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~AddComponent2.html).

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)

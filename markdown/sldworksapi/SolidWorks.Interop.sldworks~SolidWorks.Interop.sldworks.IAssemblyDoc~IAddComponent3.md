---
title: "IAddComponent3 Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "IAddComponent3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IAddComponent3.html"
---

# IAddComponent3 Method (IAssemblyDoc)

Obsolete. Superseded by [IAssemblyDoc::AddComponent4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~AddComponent4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IAddComponent3( _
   ByVal CompName As System.String, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As Component2
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim CompName As System.String
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As Component2

value = instance.IAddComponent3(CompName, X, Y, Z)
```

### C#

```csharp
Component2 IAddComponent3(
   System.string CompName,
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
Component2^ IAddComponent3(
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

See [AssemblyDoc::IAddComponent3](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~IAddComponent3.html).

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)

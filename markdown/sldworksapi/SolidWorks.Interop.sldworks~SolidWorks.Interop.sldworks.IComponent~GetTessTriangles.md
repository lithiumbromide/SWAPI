---
title: "GetTessTriangles Method (IComponent)"
project: "SOLIDWORKS API Help"
interface: "IComponent"
member: "GetTessTriangles"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent~GetTessTriangles.html"
---

# GetTessTriangles Method (IComponent)

Obsolete. Superseded by [IComponent2::GetTessTriangles](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetTessTriangles.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTessTriangles( _
   ByVal NoConversion As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent
Dim NoConversion As System.Boolean
Dim value As System.Object

value = instance.GetTessTriangles(NoConversion)
```

### C#

```csharp
System.object GetTessTriangles(
   System.bool NoConversion
)
```

### C++/CLI

```cpp
System.Object^ GetTessTriangles(
   System.bool NoConversion
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NoConversion`:

## VBA Syntax

See [Component::GetTessTriangles](ms-its:sldworksapivb6.chm::/sldworks~Component~GetTessTriangles.html).

## See Also

[IComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent.html)
[IComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent_members.html)

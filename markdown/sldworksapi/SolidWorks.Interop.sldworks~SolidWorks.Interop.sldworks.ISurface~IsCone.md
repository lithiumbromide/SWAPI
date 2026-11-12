---
title: "IsCone Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "IsCone"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IsCone.html"
---

# IsCone Method (ISurface)

Gets whether the surface is a cone.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsCone() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim value As System.Boolean

value = instance.IsCone()
```

### C#

```csharp
System.bool IsCone()
```

### C++/CLI

```cpp
System.bool IsCone();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if surface is a cone, false if not

## VBA Syntax

See [Surface::IsCone](ms-its:sldworksapivb6.chm::/sldworks~Surface~IsCone.html).

## Examples

[Locate Apex of Conical Face (VBA)](Locate_Apex_of_Conical_Face_Example_VB.htm)
[Get Parameters of Conical Surface (VBA)](Get_Parameters_of_Conical_Surface_Example_VB.htm)
[Get Parameters of Conical Surface (VB.NET)](Get_Parameters_of_Conical_Surface_Example_VBNET.htm)
[Get Parameters of Conical Surface (C#)](Get_Parameters_of_Conical_Surface_Example_CSharp.htm)

## Remarks

Closed cone faces that have an apex point do not have an edge or coedge at the apex.

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[ISurface::IConeParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IConeParams.html)
[ISurface::ConeParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ConeParams.html)
[IModeler::CreateConicalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateConicalSurface2.html)
[IModeler::ICreateConicalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateConicalSurface2.html)

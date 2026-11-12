---
title: "SetAmbientLightProperties Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SetAmbientLightProperties"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SetAmbientLightProperties.html"
---

# SetAmbientLightProperties Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SetAmbientLightProperties](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetAmbientLightProperties.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetAmbientLightProperties( _
   ByVal Name As System.String, _
   ByVal Ambient As System.Double, _
   ByVal Diffuse As System.Double, _
   ByVal Specular As System.Double, _
   ByVal Colour As System.Integer, _
   ByVal Enabled As System.Boolean, _
   ByVal Fixed As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Name As System.String
Dim Ambient As System.Double
Dim Diffuse As System.Double
Dim Specular As System.Double
Dim Colour As System.Integer
Dim Enabled As System.Boolean
Dim Fixed As System.Boolean
Dim value As System.Boolean

value = instance.SetAmbientLightProperties(Name, Ambient, Diffuse, Specular, Colour, Enabled, Fixed)
```

### C#

```csharp
System.bool SetAmbientLightProperties(
   System.string Name,
   System.double Ambient,
   System.double Diffuse,
   System.double Specular,
   System.int Colour,
   System.bool Enabled,
   System.bool Fixed
)
```

### C++/CLI

```cpp
System.bool SetAmbientLightProperties(
   System.String^ Name,
   System.double Ambient,
   System.double Diffuse,
   System.double Specular,
   System.int Colour,
   System.bool Enabled,
   System.bool Fixed
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`:
- `Ambient`:
- `Diffuse`:
- `Specular`:
- `Colour`:
- `Enabled`:
- `Fixed`:

## VBA Syntax

See [ModelDoc::SetAmbientLightProperties](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SetAmbientLightProperties.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)

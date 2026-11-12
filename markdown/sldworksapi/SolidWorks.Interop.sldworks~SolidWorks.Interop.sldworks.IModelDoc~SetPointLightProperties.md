---
title: "SetPointLightProperties Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SetPointLightProperties"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SetPointLightProperties.html"
---

# SetPointLightProperties Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SetPointLightProperties](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetPointLightProperties.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetPointLightProperties( _
   ByVal Name As System.String, _
   ByVal Ambient As System.Double, _
   ByVal Diffuse As System.Double, _
   ByVal Specular As System.Double, _
   ByVal Colour As System.Integer, _
   ByVal Enabled As System.Boolean, _
   ByVal Fixed As System.Boolean, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
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
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Boolean

value = instance.SetPointLightProperties(Name, Ambient, Diffuse, Specular, Colour, Enabled, Fixed, X, Y, Z)
```

### C#

```csharp
System.bool SetPointLightProperties(
   System.string Name,
   System.double Ambient,
   System.double Diffuse,
   System.double Specular,
   System.int Colour,
   System.bool Enabled,
   System.bool Fixed,
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
System.bool SetPointLightProperties(
   System.String^ Name,
   System.double Ambient,
   System.double Diffuse,
   System.double Specular,
   System.int Colour,
   System.bool Enabled,
   System.bool Fixed,
   System.double X,
   System.double Y,
   System.double Z
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
- `X`:
- `Y`:
- `Z`:

## VBA Syntax

See [ModelDoc::SetPointLightProperties](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SetPointLightProperties.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)

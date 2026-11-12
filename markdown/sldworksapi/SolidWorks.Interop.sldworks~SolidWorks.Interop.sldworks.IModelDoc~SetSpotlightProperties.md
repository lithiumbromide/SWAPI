---
title: "SetSpotlightProperties Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SetSpotlightProperties"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SetSpotlightProperties.html"
---

# SetSpotlightProperties Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SetSpotlightProperties](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetSpotlightProperties.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetSpotlightProperties( _
   ByVal Name As System.String, _
   ByVal Ambient As System.Double, _
   ByVal Diffuse As System.Double, _
   ByVal Specular As System.Double, _
   ByVal Colour As System.Integer, _
   ByVal Enabled As System.Boolean, _
   ByVal Fixed As System.Boolean, _
   ByVal Posx As System.Double, _
   ByVal Posy As System.Double, _
   ByVal Posz As System.Double, _
   ByVal Targetx As System.Double, _
   ByVal Targety As System.Double, _
   ByVal Targetz As System.Double, _
   ByVal ConeAngle As System.Double _
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
Dim Posx As System.Double
Dim Posy As System.Double
Dim Posz As System.Double
Dim Targetx As System.Double
Dim Targety As System.Double
Dim Targetz As System.Double
Dim ConeAngle As System.Double
Dim value As System.Boolean

value = instance.SetSpotlightProperties(Name, Ambient, Diffuse, Specular, Colour, Enabled, Fixed, Posx, Posy, Posz, Targetx, Targety, Targetz, ConeAngle)
```

### C#

```csharp
System.bool SetSpotlightProperties(
   System.string Name,
   System.double Ambient,
   System.double Diffuse,
   System.double Specular,
   System.int Colour,
   System.bool Enabled,
   System.bool Fixed,
   System.double Posx,
   System.double Posy,
   System.double Posz,
   System.double Targetx,
   System.double Targety,
   System.double Targetz,
   System.double ConeAngle
)
```

### C++/CLI

```cpp
System.bool SetSpotlightProperties(
   System.String^ Name,
   System.double Ambient,
   System.double Diffuse,
   System.double Specular,
   System.int Colour,
   System.bool Enabled,
   System.bool Fixed,
   System.double Posx,
   System.double Posy,
   System.double Posz,
   System.double Targetx,
   System.double Targety,
   System.double Targetz,
   System.double ConeAngle
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
- `Posx`:
- `Posy`:
- `Posz`:
- `Targetx`:
- `Targety`:
- `Targetz`:
- `ConeAngle`:

## VBA Syntax

See [ModelDoc::SetSpotlightProperties](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SetSpotlightProperties.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)

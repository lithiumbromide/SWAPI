---
title: "GetAmbientLightProperties Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "GetAmbientLightProperties"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~GetAmbientLightProperties.html"
---

# GetAmbientLightProperties Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::GetAmbientLightProperties](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetAmbientLightProperties.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAmbientLightProperties( _
   ByVal Name As System.String, _
   ByRef Ambient As System.Double, _
   ByRef Diffuse As System.Double, _
   ByRef Specular As System.Double, _
   ByRef Colour As System.Integer, _
   ByRef Enabled As System.Boolean, _
   ByRef Fixed As System.Boolean _
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

value = instance.GetAmbientLightProperties(Name, Ambient, Diffuse, Specular, Colour, Enabled, Fixed)
```

### C#

```csharp
System.bool GetAmbientLightProperties(
   System.string Name,
   ref System.double Ambient,
   ref System.double Diffuse,
   ref System.double Specular,
   ref System.int Colour,
   ref System.bool Enabled,
   ref System.bool Fixed
)
```

### C++/CLI

```cpp
System.bool GetAmbientLightProperties(
   System.String^ Name,
   System.double% Ambient,
   System.double% Diffuse,
   System.double% Specular,
   System.int% Colour,
   System.bool% Enabled,
   System.bool% Fixed
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

See [ModelDoc::GetAmbientLightProperties](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~GetAmbientLightProperties.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)

---
title: "SolidBodyName Property (ICWSolidBody)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWSolidBody"
member: "SolidBodyName"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody~SolidBodyName.html"
---

# SolidBodyName Property (ICWSolidBody)

Gets the name of the solid body.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property SolidBodyName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICWSolidBody
Dim value As System.String

value = instance.SolidBodyName
```

### C#

```csharp
System.string SolidBodyName {get;}
```

### C++/CLI

```cpp
property System.String^ SolidBodyName {
   System.String^ get();
}
```

### Property Value

Name of solid body

## VBA Syntax

See [CWSolidBody::SolidBodyName](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWSolidBody~SolidBodyName.html).

## Examples

[Change Beam to Solid Body and Back (C#)](Change_Beam_to_Solid_Body_and_Back_Example_CSharp.htm)
[Change Beam to Solid Body and Back (VB.NET)](Change_Beam_to_Solid_Body_and_Back_Example_VBNET.htm)
[Change Beam to Solid Body and Back (VBA)](Change_Beam_to_Solid_Body_and_Back_Example_VB.htm)

## See Also

[ICWSolidBody Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody.html)
[ICWSolidBody Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0

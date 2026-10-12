---
title: "ConvertToBeamBody Method (ICWSolidBody)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWSolidBody"
member: "ConvertToBeamBody"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody~ConvertToBeamBody.html"
---

# ConvertToBeamBody Method (ICWSolidBody)

Treat a solid body as a beam.

## Syntax

### Visual Basic (Declaration)

```vb
Function ConvertToBeamBody() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWSolidBody
Dim value As System.Integer

value = instance.ConvertToBeamBody()
```

### C#

```csharp
System.int ConvertToBeamBody()
```

### C++/CLI

```cpp
System.int ConvertToBeamBody();
```

### Return Value

0 to treat a solid body as a beam, 1 to not

## VBA Syntax

See [CWSolidBody::ConvertToBeamBody](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWSolidBody~ConvertToBeamBody.html).

## Examples

[Change Beam to Solid Body and Back (C#)](Change_Beam_to_Solid_Body_and_Back_Example_CSharp.htm)
[Change Beam to Solid Body and Back (VB.NET)](Change_Beam_to_Solid_Body_and_Back_Example_VBNET.htm)
[Change Beam to Solid Body and Back (VBA)](Change_Beam_to_Solid_Body_and_Back_Example_VB.htm)

## See Also

[ICWSolidBody Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody.html)
[ICWSolidBody Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody_members.html)
[ICWBeamBody::ConvertToSolidBody Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~ConvertToSolidBody.html)

## Availability

SOLIDWORKS Simulation API 2010 SP0

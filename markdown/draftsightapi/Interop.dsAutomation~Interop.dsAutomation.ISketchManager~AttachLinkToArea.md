---
title: "AttachLinkToArea Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "AttachLinkToArea"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~AttachLinkToArea.html"
---

# AttachLinkToArea Method (ISketchManager)

Attaches the specified hyperlink to the specified rectangular area.

## Syntax

### Visual Basic

```vb
Function AttachLinkToArea( _
   ByVal StartCornerX As System.Double, _
   ByVal StartCornerY As System.Double, _
   ByVal StartCornerZ As System.Double, _
   ByVal OppositeCornerX As System.Double, _
   ByVal OppositeCornerY As System.Double, _
   ByVal OppositeCornerZ As System.Double, _
   ByVal HyperLinkAddress As System.String, _
   ByVal Description As System.String, _
   ByRef PolyLine3D As PolyLine3D _
) As HyperLink
```

### C#

```csharp
HyperLink AttachLinkToArea(
   System.double StartCornerX,
   System.double StartCornerY,
   System.double StartCornerZ,
   System.double OppositeCornerX,
   System.double OppositeCornerY,
   System.double OppositeCornerZ,
   System.string HyperLinkAddress,
   System.string Description,
   out PolyLine3D PolyLine3D
)
```

### JScript

```
function AttachLinkToArea(
   StartCornerX : System.double,
   StartCornerY : System.double,
   StartCornerZ : System.double,
   OppositeCornerX : System.double,
   OppositeCornerY : System.double,
   OppositeCornerZ : System.double,
   HyperLinkAddress : System.String,
   Description : System.String,
   PolyLine3D : PolyLine3D
) : HyperLink;
```

### Managed Extensions for C++

```
HyperLink* AttachLinkToArea(
   System.double StartCornerX,
   System.double StartCornerY,
   System.double StartCornerZ,
   System.double OppositeCornerX,
   System.double OppositeCornerY,
   System.double OppositeCornerZ,
   System.string* HyperLinkAddress,
   System.string* Description,
   [PARAMFLAG::Out] PolyLine3D* PolyLine3D
)
```

### C++/CLI

```cpp
HyperLink^ AttachLinkToArea(
   System.double StartCornerX,
   System.double StartCornerY,
   System.double StartCornerZ,
   System.double OppositeCornerX,
   System.double OppositeCornerY,
   System.double OppositeCornerZ,
   System.String^ HyperLinkAddress,
   System.String^ Description,
   [Out] PolyLine3D^ PolyLine3D
)
```

### Parameters

- `StartCornerX`: x coordinate of start corner of rectangular area
- `StartCornerY`: y coordinate of start corner of rectangular area
- `StartCornerZ`: z coordinate of start corner of rectangular area
- `OppositeCornerX`: x coordinate of opposite corner of rectangular area
- `OppositeCornerY`: y coordinate of opposite corner of rectangular area
- `OppositeCornerZ`: z coordinate of opposite corner of rectangular area
- `HyperLinkAddress`: Address of the hyperlink
- `Description`: Description of the hyperlink
- `PolyLine3D`: [3D PolyLine](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D.html) entity on the URLLAYER Layer

### Return Value

[Hyperlink](Interop.dsAutomation~Interop.dsAutomation.IHyperLink.html)

## Examples

[Create and Attach Hyperlink (C#)](Create_and_Attach_Hyperlink_Example_CSharp.htm)
[Create and Attach Hyperlink (VB.NET)](Create_and_Attach_Hyperlink_Example_VBNET.htm)
[Create and Attach Hyperlink (VBA)](Create_and_Attach_Hyperlink_Example_VBA.htm)
[Insert HyperLink (JavaScript)](Insert_HyperLink_Example_JS.htm)

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)

## Availability

DraftSight V1R1.3

---
title: "SetPosition Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "SetPosition"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetPosition.html"
---

# SetPosition Method (IGtol)

Sets the position of this GTol.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetPosition( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double

instance.SetPosition(X, Y, Z)
```

### C#

```csharp
void SetPosition(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
void SetPosition(
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: X location for the GTol
- `Y`: Y location of the GTol
- `Z`: Z location of the GTol

## VBA Syntax

See [Gtol::SetPosition](ms-its:sldworksapivb6.chm::/sldworks~Gtol~SetPosition.html).

## Examples

The position is the upper-left corner of the GTol.

## Examples

[Get Gtol Witness Line (VBA)](Get_GTol_Witness_Line_Example_VB.htm)
[Get Gtol Witness Line (VB.NET)](Get_GTol_Witness_Line_Example_VBNET.htm)
[Get Gtol Witness Line (C#)](Get_GTol_Witness_Line_Example_CSharp.htm)

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)

---
title: "ICreateBlendSurface Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "ICreateBlendSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateBlendSurface.html"
---

# ICreateBlendSurface Method (IBody2)

Creates a constant radius rolling-ball blend surface (also known as a pipe surface) between two side surfaces.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateBlendSurface( _
   ByVal Surface1 As Surface, _
   ByVal Range1 As System.Double, _
   ByVal Surface2 As Surface, _
   ByVal Range2 As System.Double, _
   ByRef StartVec As System.Double, _
   ByRef EndVec As System.Double, _
   ByVal HaveHelpVec As System.Integer, _
   ByRef HelpVec As System.Double, _
   ByVal HaveHelpBox As System.Integer, _
   ByRef HelpBox As System.Double _
) As Surface
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim Surface1 As Surface
Dim Range1 As System.Double
Dim Surface2 As Surface
Dim Range2 As System.Double
Dim StartVec As System.Double
Dim EndVec As System.Double
Dim HaveHelpVec As System.Integer
Dim HelpVec As System.Double
Dim HaveHelpBox As System.Integer
Dim HelpBox As System.Double
Dim value As Surface

value = instance.ICreateBlendSurface(Surface1, Range1, Surface2, Range2, StartVec, EndVec, HaveHelpVec, HelpVec, HaveHelpBox, HelpBox)
```

### C#

```csharp
Surface ICreateBlendSurface(
   Surface Surface1,
   System.double Range1,
   Surface Surface2,
   System.double Range2,
   ref System.double StartVec,
   ref System.double EndVec,
   System.int HaveHelpVec,
   ref System.double HelpVec,
   System.int HaveHelpBox,
   ref System.double HelpBox
)
```

### C++/CLI

```cpp
Surface^ ICreateBlendSurface(
   Surface^ Surface1,
   System.double Range1,
   Surface^ Surface2,
   System.double Range2,
   System.double% StartVec,
   System.double% EndVec,
   System.int HaveHelpVec,
   System.double% HelpVec,
   System.int HaveHelpBox,
   System.double% HelpBox
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Surface1`: First side [surface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface.html)
- `Range1`: Signed offset of Surface1
- `Surface2`: Second side [surface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface.html)
- `Range2`: Signed offset of Surface2
- `StartVec`: Array of 3 doubles representing a point close to the start of the blend spine
- `EndVec`: Array of 3 doubles representing a point close to the end of the blend spine
- `HaveHelpVec`: Optional; True if help vector is provided
- `HelpVec`: Array of 3 doubles representing the direction of the help vector
- `HaveHelpBox`: Optional; True if box is provided
- `HelpBox`: Array of 6 doubles bounding the area of interest

### Return Value

Newly created [surface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface.html)

## VBA Syntax

See [Body2::ICreateBlendSurface](ms-its:sldworksapivb6.chm::/sldworks~Body2~ICreateBlendSurface.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::CreateBlendSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateBlendSurface.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

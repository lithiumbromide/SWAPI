---
title: "SetParameters Method (IDetailCircle)"
project: "SOLIDWORKS API Help"
interface: "IDetailCircle"
member: "SetParameters"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~SetParameters.html"
---

# SetParameters Method (IDetailCircle)

Sets the location and size of this detail circle.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetParameters( _
   ByVal XPosition As System.Double, _
   ByVal YPosition As System.Double, _
   ByVal Radius As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDetailCircle
Dim XPosition As System.Double
Dim YPosition As System.Double
Dim Radius As System.Double
Dim value As System.Boolean

value = instance.SetParameters(XPosition, YPosition, Radius)
```

### C#

```csharp
System.bool SetParameters(
   System.double XPosition,
   System.double YPosition,
   System.double Radius
)
```

### C++/CLI

```cpp
System.bool SetParameters(
   System.double XPosition,
   System.double YPosition,
   System.double Radius
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `XPosition`: x location of the detail circle
- `YPosition`: y location of the detail circle
- `Radius`: Size of the radius of the detail circle

### Return Value

True if the detail circle is created at the specified location and at the specified size, false if not

## VBA Syntax

See [DetailCircle::SetParameters](ms-its:sldworksapivb6.chm::/sldworks~DetailCircle~SetParameters.html).

## Remarks

Use [IModelDoc2::EditRebuild3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~EditRebuild3.html) to update the drawing, including the detail circle.

## See Also

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.html)
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0

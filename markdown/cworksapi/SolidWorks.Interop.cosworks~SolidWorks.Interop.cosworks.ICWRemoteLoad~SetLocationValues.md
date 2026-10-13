---
title: "SetLocationValues Method (ICWRemoteLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRemoteLoad"
member: "SetLocationValues"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~SetLocationValues.html"
---

# SetLocationValues Method (ICWRemoteLoad)

Sets the coordinates of the point of application of this remote load.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetLocationValues( _
   ByVal DXValue As System.Double, _
   ByVal DYValue As System.Double, _
   ByVal DZValue As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRemoteLoad
Dim DXValue As System.Double
Dim DYValue As System.Double
Dim DZValue As System.Double

instance.SetLocationValues(DXValue, DYValue, DZValue)
```

### C#

```csharp
void SetLocationValues(
   System.double DXValue,
   System.double DYValue,
   System.double DZValue
)
```

### C++/CLI

```cpp
void SetLocationValues(
   System.double DXValue,
   System.double DYValue,
   System.double DZValue
)
```

### Parameters

- `DXValue`: X-coordinate
- `DYValue`: Y-coordinate
- `DZValue`: Z-coordinate

## VBA Syntax

See [CWRemoteLoad::SetLocationValues](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRemoteLoad~SetLocationValues.html).

## Examples

[Add Remote Load (C#)](Add_Remote_Load_Example_CSharp.htm)
[Add Remote Load (VB.NET)](Add_Remote_Load_Example_VBNET.htm)
[Add Remote Load (VBA)](Add_Remote_Load_Example_VB.htm)

## See Also

[ICWRemoteLoad Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad.html)
[ICWRemoteLoad Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad_members.html)
[ICWRemoteLoad::GetLocationValues Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~GetLocationValues.html)
[ICWRemoteLoad::LocationUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~LocationUnit.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0

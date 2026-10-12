---
title: "GetLocationValues Method (ICWRemoteLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRemoteLoad"
member: "GetLocationValues"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~GetLocationValues.html"
---

# GetLocationValues Method (ICWRemoteLoad)

Gets the coordinates of the point of application of this remote load.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetLocationValues( _
   ByRef DXValue As System.Double, _
   ByRef DYValue As System.Double, _
   ByRef DZValue As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRemoteLoad
Dim DXValue As System.Double
Dim DYValue As System.Double
Dim DZValue As System.Double

instance.GetLocationValues(DXValue, DYValue, DZValue)
```

### C#

```csharp
void GetLocationValues(
   out System.double DXValue,
   out System.double DYValue,
   out System.double DZValue
)
```

### C++/CLI

```cpp
void GetLocationValues(
   [Out] System.double DXValue,
   [Out] System.double DYValue,
   [Out] System.double DZValue
)
```

### Parameters

- `DXValue`: X-coordinate
- `DYValue`: Y-coordinate
- `DZValue`: Z-coordinate

## VBA Syntax

See [CWRemoteLoad::GetLocationValues](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRemoteLoad~GetLocationValues.html).

## Examples

[Add Remote Load (C#)](Add_Remote_Load_Example_CSharp.htm)
[Add Remote Load (VB.NET)](Add_Remote_Load_Example_VBNET.htm)
[Add Remote Load (VBA)](Add_Remote_Load_Example_VB.htm)

## See Also

[ICWRemoteLoad Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad.html)
[ICWRemoteLoad Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad_members.html)
[ICWRemoteLoad::SetLocationValues Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~SetLocationValues.html)
[ICWRemoteLoad::LocationUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~LocationUnit.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0

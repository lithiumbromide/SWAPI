---
title: "LocationUnit Property (ICWRemoteLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRemoteLoad"
member: "LocationUnit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~LocationUnit.html"
---

# LocationUnit Property (ICWRemoteLoad)

Gets or sets the units of remote location.

## Syntax

### Visual Basic (Declaration)

```vb
Property LocationUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRemoteLoad
Dim value As System.Integer

instance.LocationUnit = value

value = instance.LocationUnit
```

### C#

```csharp
System.int LocationUnit {get; set;}
```

### C++/CLI

```cpp
property System.int LocationUnit {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Units as defined in [swsLinearUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsLinearUnit_e.html)

## VBA Syntax

See [CWRemoteLoad::LocationUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRemoteLoad~LocationUnit.html).

## Examples

[Add Remote Load (C#)](Add_Remote_Load_Example_CSharp.htm)
[Add Remote Load (VB.NET)](Add_Remote_Load_Example_VBNET.htm)
[Add Remote Load (VBA)](Add_Remote_Load_Example_VB.htm)

## See Also

[ICWRemoteLoad Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad.html)
[ICWRemoteLoad Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad_members.html)
[ICWRemoteLoad::GetLocationValues Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~GetLocationValues.html)
[ICWRemoteLoad::SetLocationValues Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~SetLocationValues.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0

---
title: "LoadType Property (ICWRemoteLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRemoteLoad"
member: "LoadType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~LoadType.html"
---

# LoadType Property (ICWRemoteLoad)

Gets or sets the type of remote load.

## Syntax

### Visual Basic (Declaration)

```vb
Property LoadType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRemoteLoad
Dim value As System.Integer

instance.LoadType = value

value = instance.LoadType
```

### C#

```csharp
System.int LoadType {get; set;}
```

### C++/CLI

```cpp
property System.int LoadType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Type of remote load as defined by [swsRemoteLoadType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsRemoteLoadType_e.html)

## VBA Syntax

See [CWRemoteLoad::LoadType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRemoteLoad~LoadType.html).

## Examples

[Add Remote Load (VBA)](Add_Remote_Load_Example_VB.htm)
[Add Remote Load (VB.NET)](Add_Remote_Load_Example_VBNET.htm)
[Add Remote Load (C#)](Add_Remote_Load_Example_CSharp.htm)

## Remarks

For linear and nonlinear static studies only, instead of setting this property, set [ICWRemoteLoad::ConnectionType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~ConnectionType.html).

## See Also

[ICWRemoteLoad Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad.html)
[ICWRemoteLoad Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0

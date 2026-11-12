---
title: "ForceUnit Property (ICWRemoteLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRemoteLoad"
member: "ForceUnit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~ForceUnit.html"
---

# ForceUnit Property (ICWRemoteLoad)

Sets the units of force for this remote load.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property ForceUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRemoteLoad

instance.ForceUnit = value
```

### C#

```csharp
System.int ForceUnit {set;}
```

### C++/CLI

```cpp
property System.int ForceUnit {
   void set (    System.int value);
}
```

### Property Value

Units of force as defined in [swsForceUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsForceUnit_e.html)

## VBA Syntax

See [CWRemoteLoad::ForceUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRemoteLoad~ForceUnit.html).

## Examples

[Add a Remote Load with Distributed Coupling (VBA)](Add_Remote_Load_with_Distributed_Connection_Example_VB.htm)

## Remarks

This property is valid only if [ICWRemoteLoad::AllowDistributedCoupling](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~AllowDistributedCoupling.html) returns true. If it returns false, use [ICWRemoteLoad::ForceOrTranslationUnit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~ForceOrTranslationUnit.html).

## See Also

[ICWRemoteLoad Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad.html)
[ICWRemoteLoad Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad_members.html)
[ICWRemoteLoad::SetForceOrTranslationValuesEx Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~SetForceOrTranslationValuesEx.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0

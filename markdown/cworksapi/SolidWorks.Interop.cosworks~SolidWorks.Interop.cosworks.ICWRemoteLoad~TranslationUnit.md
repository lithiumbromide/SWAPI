---
title: "TranslationUnit Property (ICWRemoteLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRemoteLoad"
member: "TranslationUnit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~TranslationUnit.html"
---

# TranslationUnit Property (ICWRemoteLoad)

Sets the units of translation for this remote load.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property TranslationUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRemoteLoad

instance.TranslationUnit = value
```

### C#

```csharp
System.int TranslationUnit {set;}
```

### C++/CLI

```cpp
property System.int TranslationUnit {
   void set (    System.int value);
}
```

### Property Value

Units of translation as defined by [swsLinearUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsLinearUnit_e.html)

## VBA Syntax

See [CWRemoteLoad::TranslationUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRemoteLoad~TranslationUnit.html).

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

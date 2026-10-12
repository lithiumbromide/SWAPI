---
title: "ForceOrTranslationUnit Property (ICWRemoteLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRemoteLoad"
member: "ForceOrTranslationUnit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~ForceOrTranslationUnit.html"
---

# ForceOrTranslationUnit Property (ICWRemoteLoad)

Sets the units of force or translation for this remote load.

## Syntax

### Visual Basic (Declaration)

```vb
Property ForceOrTranslationUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRemoteLoad
Dim value As System.Integer

instance.ForceOrTranslationUnit = value

value = instance.ForceOrTranslationUnit
```

### C#

```csharp
System.int ForceOrTranslationUnit {get; set;}
```

### C++/CLI

```cpp
property System.int ForceOrTranslationUnit {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

| If a remote... | Then the value returned is defined in... |
| --- | --- |
| Force | swsForceUnit_e |
| Translation | swsLinearUnit_e |

## VBA Syntax

See [CWRemoteLoad::ForceOrTranslationUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRemoteLoad~ForceOrTranslationUnit.html).

## Examples

[Add Remote Load (C#)](Add_Remote_Load_Example_CSharp.htm)
[Add Remote Load (VB.NET)](Add_Remote_Load_Example_VBNET.htm)
[Add Remote Load (VBA)](Add_Remote_Load_Example_VB.htm)

## Remarks

This property is valid only if [ICWRemoteLoad::AllowDistributedCoupling](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~AllowDistributedCoupling.html) returns false. If it returns true, use [ICWRemoteLoad::ForceUnit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~ForceUnit.html) and [ICWRemoteLoad::TranslationUnit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~TranslationUnit.html).

## See Also

[ICWRemoteLoad Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad.html)
[ICWRemoteLoad Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad_members.html)
[ICWRemoteLoad::GetForceOrTranslationValues Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~GetForceOrTranslationValues.html)
[ICWRemoteLoad::SetForceOrTranslationValues Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~SetForceOrTranslationValues.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0

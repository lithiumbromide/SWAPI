---
title: "SetReferenceGeometry Method (ICWRestraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRestraint"
member: "SetReferenceGeometry"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~SetReferenceGeometry.html"
---

# SetReferenceGeometry Method (ICWRestraint)

Sets the direction reference for this restraint.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetReferenceGeometry( _
   ByVal DispRefEntity As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRestraint
Dim DispRefEntity As System.Object

instance.SetReferenceGeometry(DispRefEntity)
```

### C#

```csharp
void SetReferenceGeometry(
   System.object DispRefEntity
)
```

### C++/CLI

```cpp
void SetReferenceGeometry(
   System.Object^ DispRefEntity
)
```

### Parameters

- `DispRefEntity`: Face, edge, plane, or oxis

## VBA Syntax

See [CWRestraint::SetReferenceGeometry](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRestraint~SetReferenceGeometry.html).

## Remarks

This method is valid only if [ICWRestraint::RestraintType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~RestraintType.html) is set to [swsRestraintType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRestraintType_e.html).swsRestraintTypeReferenceGeometry.

## See Also

[ICWRestraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint.html)
[ICWRestraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint_members.html)
[ICWRestraint::SetTranslationComponentsValues Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~SetTranslationComponentsValues.html)
[ICWRestraint::SetRotationComponentsValues Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~SetRotationComponentsValues.html)
[ICWRestraint::GetTranslationComponentsValues Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~GetTranslationComponentsValues.html)
[ICWRestraint::GetRotationComponentsValues Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint~GetRotationComponentsValues.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0

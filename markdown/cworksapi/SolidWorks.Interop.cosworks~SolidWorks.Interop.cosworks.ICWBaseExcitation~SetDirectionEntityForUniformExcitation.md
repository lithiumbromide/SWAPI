---
title: "SetDirectionEntityForUniformExcitation Method (ICWBaseExcitation)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBaseExcitation"
member: "SetDirectionEntityForUniformExcitation"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~SetDirectionEntityForUniformExcitation.html"
---

# SetDirectionEntityForUniformExcitation Method (ICWBaseExcitation)

Sets the face, edge, or plane in whose direction the base excitation is uniformly applied to all restrained locations.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetDirectionEntityForUniformExcitation( _
   ByVal RefEntity As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBaseExcitation
Dim RefEntity As System.Object

instance.SetDirectionEntityForUniformExcitation(RefEntity)
```

### C#

```csharp
void SetDirectionEntityForUniformExcitation(
   System.object RefEntity
)
```

### C++/CLI

```cpp
void SetDirectionEntityForUniformExcitation(
   System.Object^ RefEntity
)
```

### Parameters

- `RefEntity`: Face, edge, or plane of excitation direction (see **Remarks**)

## VBA Syntax

See [CWBaseExcitation::SetDirectionEntityForUniformExcitation](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBaseExcitation~SetDirectionEntityForUniformExcitation.html).

## Remarks

This method applies only to base excitations that are created using [ICWLoadsAndRestraintsManager::AddUniformBaseExcitation](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWLoadsAndRestraintsManager~AddUniformBaseExcitation.html).

You can specify the direction of uniform base excitation by calling either:

- this method

- or -

- [ICWBaseExcitation::SetExcitationDirections](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBaseExcitation~SetExcitationDirections.html) and [ICWBaseExcitation::SetExcitationDirectionValues](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBaseExcitation~SetExcitationDirectionValues.html) to explicitly specify the excitation direction components and values

## See Also

[ICWBaseExcitation Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation.html)
[ICWBaseExcitation Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0

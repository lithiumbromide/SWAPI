---
title: "SetMassValues Method (ICWRemoteLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRemoteLoad"
member: "SetMassValues"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~SetMassValues.html"
---

# SetMassValues Method (ICWRemoteLoad)

Obsolete. Superseded by [ICWRemoteLoad::SetMassValues2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~SetMassValues2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetMassValues( _
   ByVal BInclude As System.Integer, _
   ByVal Var As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRemoteLoad
Dim BInclude As System.Integer
Dim Var As System.Object

instance.SetMassValues(BInclude, Var)
```

### C#

```csharp
void SetMassValues(
   System.int BInclude,
   System.object Var
)
```

### C++/CLI

```cpp
void SetMassValues(
   System.int BInclude,
   System.Object^ Var
)
```

### Parameters

- `BInclude`: 1 to include mass in the remote load, 0 to not
- `Var`: Array of mass component values for this remote load; valid only if BInclude = 1 (see **Remarks**)

## VBA Syntax

See [CWRemoteLoad::SetMassValues](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRemoteLoad~SetMassValues.html).

## Remarks

This method works only if [ICWRemoteLoad::LoadType](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWRemoteLoad~LoadType.html) = swsRemoteLoadType_e.swsRemoteLoadType_RigidLoadOrMass.

Array of mass components:

**[** m`, Lxx, Lyy, Lzz, Lxy, Lyz, Lxz` **]**

where:

- m = Remote mass value
- Lxx = Mass moment of inertia with respect to axis X
- Lyy = Mass moment of inertia with respect to axis Y
- Lzz = Mass moment of inertia with respect to axis Z
- Lxy = Product of inertias with respect to axes X and Y
- Lyz = Product of inertias with respect to axes Y and Z
- Lxz = Product of inertias with respect to axes X and Z

## See Also

[ICWRemoteLoad Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad.html)
[ICWRemoteLoad Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad_members.html)
[ICWRemoteLoad::GetMassValues Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~GetMassValues.html)
[ICWRemoteLoad::MassUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~MassUnit.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0

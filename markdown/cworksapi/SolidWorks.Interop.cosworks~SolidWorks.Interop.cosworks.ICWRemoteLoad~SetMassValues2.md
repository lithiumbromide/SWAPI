---
title: "SetMassValues2 Method (ICWRemoteLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRemoteLoad"
member: "SetMassValues2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~SetMassValues2.html"
---

# SetMassValues2 Method (ICWRemoteLoad)

Sets the components of mass in this remote load.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetMassValues2( _
   ByVal BInclude As System.Boolean, _
   ByVal Var As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRemoteLoad
Dim BInclude As System.Boolean
Dim Var As System.Object

instance.SetMassValues2(BInclude, Var)
```

### C#

```csharp
void SetMassValues2(
   System.bool BInclude,
   System.object Var
)
```

### C++/CLI

```cpp
void SetMassValues2(
   System.bool BInclude,
   System.Object^ Var
)
```

### Parameters

- `BInclude`: -1 or trie to include mass in the remote load, 0 or false to not
- `Var`: Array of mass component values for this remote load; valid only if BInclude = -1 (see **Remarks**)

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

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30

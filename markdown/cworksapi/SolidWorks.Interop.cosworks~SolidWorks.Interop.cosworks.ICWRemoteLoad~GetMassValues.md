---
title: "GetMassValues Method (ICWRemoteLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRemoteLoad"
member: "GetMassValues"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~GetMassValues.html"
---

# GetMassValues Method (ICWRemoteLoad)

Obsolete. Superseded by [ICWRemoteLoad::GetMassValues2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~GetMassValues2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMassValues( _
   ByRef BInclude As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRemoteLoad
Dim BInclude As System.Integer
Dim value As System.Object

value = instance.GetMassValues(BInclude)
```

### C#

```csharp
System.object GetMassValues(
   out System.int BInclude
)
```

### C++/CLI

```cpp
System.Object^ GetMassValues(
   [Out] System.int BInclude
)
```

### Parameters

- `BInclude`: 1 to include mass in the remote load, 0 to not

### Return Value

Array of remote mass component values; valid only if BInclude = 1 (see **Remarks**)

## VBA Syntax

See [CWRemoteLoad::GetMassValues](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRemoteLoad~GetMassValues.html).

## Remarks

This method is valid only if [ICWRemoteLoad::LoadType](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWRemoteLoad~LoadType.html) = swsRemoteLoadType_e.swsRemoteLoadType_RigidLoadOrMass.

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
[ICWRemoteLoad::SetMassValues Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~SetMassValues.html)
[ICWRemoteLoad::MassUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~MassUnit.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0

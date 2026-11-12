---
title: "GetMassValues2 Method (ICWRemoteLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRemoteLoad"
member: "GetMassValues2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~GetMassValues2.html"
---

# GetMassValues2 Method (ICWRemoteLoad)

Gets the components of mass in this remote load.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMassValues2( _
   ByRef BInclude As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRemoteLoad
Dim BInclude As System.Boolean
Dim value As System.Object

value = instance.GetMassValues2(BInclude)
```

### C#

```csharp
System.object GetMassValues2(
   out System.bool BInclude
)
```

### C++/CLI

```cpp
System.Object^ GetMassValues2(
   [Out] System.bool BInclude
)
```

### Parameters

- `BInclude`: -1 or true to include mass in the remote load, 0 or false to not

### Return Value

Array of remote mass component values; valid only if BInclude = -1 (see **Remarks**)

## Remarks

This method returns booleans or integers in out parameter BInclude, depending on its prior declaration.

If BInclude is cast as a:

- Boolean, true or false is returned in the out parameter.
- Long or integer, -1 (=true) or 0 (=false) is returned in the out parameter.

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

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
